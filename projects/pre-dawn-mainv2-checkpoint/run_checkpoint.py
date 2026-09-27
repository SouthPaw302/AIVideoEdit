#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from runtime_v2.gatekeeper import evaluate_action
from runtime_v2.jev.decision import decide
from runtime_v2.models.music_beat import analyze_music
from runtime_v2.models.registry import ModelRegistry

PROJECT = Path(__file__).resolve().parent
OUT = PROJECT / "checkpoint_out"
OUT.mkdir(exist_ok=True)
AUDIO = PROJECT / "inputs/pre-dawn-in-paris.m4a"
IMAGE = PROJECT / "inputs/canon.jpg"
VIDEO = OUT / "pre-dawn-mainv2-full-proof.mp4"


def run(cmd: list[str]) -> str:
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise SystemExit(proc.returncode)
    return proc.stdout


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


registry = ModelRegistry.load_default()
music = analyze_music(AUDIO, registry=registry)
(OUT / "music_analysis.json").write_text(
    json.dumps(music, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

branch = os.environ.get("GITHUB_REF_NAME", "song/pre-dawn-mainv2-checkpoint")
gate = evaluate_action(
    repo=ROOT,
    action="checkpoint.render",
    mutation=False,
    expected_stage="REFERENCES_ANALYZED",
    current_branch=branch,
)
(OUT / "gatekeeper.json").write_text(
    json.dumps(gate.as_dict(), indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
if gate.decision != "PASS":
    raise SystemExit("Runtime Gatekeeper denied checkpoint render")

audio_probe = json.loads(
    run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(AUDIO),
        ]
    )
)
duration = float(audio_probe["format"]["duration"])

video_filter = (
    "scale=820:820:force_original_aspect_ratio=increase,"
    "crop=820:820,"
    "zoompan=z='min(1.0+0.000022*on,1.055)':"
    "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
    "d=1:s=720x720:fps=30,"
    "vignette=PI/5"
)

run(
    [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-framerate",
        "30",
        "-i",
        str(IMAGE),
        "-i",
        str(AUDIO),
        "-vf",
        video_filter,
        "-t",
        f"{duration:.3f}",
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "22",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "160k",
        "-movflags",
        "+faststart",
        "-shortest",
        str(VIDEO),
    ]
)

run(
    [
        "ffmpeg",
        "-y",
        "-i",
        str(VIDEO),
        "-vf",
        "fps=1/21,scale=240:240,tile=5x1",
        "-frames:v",
        "1",
        str(OUT / "contact-sheet.jpg"),
    ]
)

video_probe = json.loads(
    run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(VIDEO),
        ]
    )
)
streams = video_probe.get("streams", [])
video_stream = next((s for s in streams if s.get("codec_type") == "video"), {})
audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), {})
render_duration = float(video_probe["format"]["duration"])
duration_ok = abs(render_duration - duration) <= 0.75
render_ok = (
    video_stream.get("width") == 720
    and video_stream.get("height") == 720
    and bool(audio_stream)
    and duration_ok
)
onnx_ok = music.get("engine") == "beat_this_onnx"

jev = decide(
    {
        "gate": gate.decision,
        "checks": {
            "onnx_actual_track": onnx_ok,
            "render_qc": render_ok,
            "duration_match": duration_ok,
        },
        "next_action_permitted": render_ok and onnx_ok,
    }
)

report = {
    "schema": "aivideoedit.mainv2-checkpoint.v1",
    "project": "pre-dawn-mainv2-checkpoint",
    "branch": branch,
    "source_audio_duration_seconds": duration,
    "render_duration_seconds": render_duration,
    "music_engine": music.get("engine"),
    "bpm": music.get("bpm"),
    "beat_count": len(music.get("beat_positions_seconds") or []),
    "gatekeeper": gate.as_dict(),
    "jev": jev,
    "render_qc": {
        "pass": render_ok,
        "duration_match": duration_ok,
        "width": video_stream.get("width"),
        "height": video_stream.get("height"),
        "video_codec": video_stream.get("codec_name"),
        "audio_codec": audio_stream.get("codec_name"),
    },
    "sha256": {
        "audio": sha256(AUDIO),
        "canon": sha256(IMAGE),
        "video": sha256(VIDEO),
    },
}
(OUT / "checkpoint_report.json").write_text(
    json.dumps(report, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)
print(json.dumps(report, indent=2, sort_keys=True))

if not render_ok or not onnx_ok or jev.get("decision") not in {"PASS", "CONTINUE"}:
    raise SystemExit("checkpoint failed")
