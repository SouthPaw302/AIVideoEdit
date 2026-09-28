#!/usr/bin/env python3
"""Build Mountain Noir long-form picture from source-derived stills and MainV2 FX."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from general.reusable.fx_v2 import living_still_fx
from general.reusable.fx_v2.promoted_effects import apply_effect


PROJECT = ROOT / "projects" / "mountain-noir-after-midnight"
SOURCE = PROJECT / "assets" / "source-frames"
RENDER = PROJECT / "render" / "mainv2-living"
FPS = 24
LOOP_SECONDS = 4
WORK_SIZE = (640, 360)
OUT_SIZE = "1280:720"

GROUPS = {
    "irish-eyes": ["wet_road_rain_reflection", "atmospheric_fog", "threshold_reflection_lamp_flicker"],
    "leave-door": ["candlelight_micro_loop", "firelight_breath", "smoke_memory_forms"],
    "silver-coin": ["forest_breath", "warm_halation_bloom", "radial_light_shafts"],
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def run(args: list[str]) -> None:
    p = subprocess.run(args, text=True, capture_output=True, check=False)
    if p.returncode:
        raise RuntimeError((p.stderr or p.stdout or "ffmpeg failed").strip())


def effect_frame(source: np.ndarray, index: int, total: int, effects: list[str]) -> np.ndarray:
    phase = index / total
    frame = living_still_fx.camera_drift(source, {"phase": phase, "t": phase * LOOP_SECONDS}, pan_px=6.0, tilt_deg=0.22, zoom=0.012)
    for effect in effects:
        frame = apply_effect(effect, frame, phase * LOOP_SECONDS, LOOP_SECONDS, energy=0.46, transient=0.28)
    return frame


def render_loop(source: Path, output: Path, effects: list[str]) -> None:
    image = cv2.imread(str(source), cv2.IMREAD_COLOR)
    if image is None:
        raise RuntimeError(f"cannot read still: {source}")
    image = cv2.resize(image, WORK_SIZE, interpolation=cv2.INTER_AREA)
    width, height = WORK_SIZE
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{width}x{height}", "-r", str(FPS), "-i", "-",
        "-vf", f"scale={OUT_SIZE}:flags=lanczos,format=yuv420p",
        "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-movflags", "+faststart", str(output),
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    assert proc.stdin is not None
    total = FPS * LOOP_SECONDS
    try:
        for index in range(total):
            proc.stdin.write(effect_frame(image, index, total, effects).tobytes())
        proc.stdin.close()
        stderr = proc.stderr.read().decode("utf-8", errors="replace") if proc.stderr else ""
        if proc.wait() != 0:
            raise RuntimeError(stderr.strip() or f"loop encoder failed: {source.name}")
    except Exception:
        proc.kill()
        raise


def loop_sources() -> list[tuple[str, Path, list[str]]]:
    result = []
    excluded = {"irish-eyes-003s", "irish-eyes-194s", "silver-coin-205s"}
    for group, effects in GROUPS.items():
        for path in sorted((SOURCE / group).glob("*.png")):
            if path.stem in excluded:
                continue
            result.append((group, path, effects))
    if len(result) != 30:
        raise RuntimeError(f"expected 30 extracted stills, found {len(result)}")
    return result


def render_all_loops(limit: int | None = None, proof: bool = False) -> list[dict]:
    records = []
    sources = loop_sources()
    if proof:
        sources = [sources[0], sources[10], sources[20]]
    for index, (group, source, effects) in enumerate(sources):
        if limit is not None and index >= limit:
            break
        output = RENDER / "loops" / f"{index + 1:02d}_{source.stem}.mp4"
        render_loop(source, output, effects)
        records.append({"id": f"S{index + 1:02d}", "group": group, "source": str(source.relative_to(PROJECT)), "effects": effects, "loop": str(output.relative_to(PROJECT)), "sha256": sha256(output)})
        print(f"rendered {index + 1}/{len(sources)}: {output.name}", flush=True)
    return records


def make_proof(records: list[dict]) -> Path:
    proof = RENDER / "proof.mp4"
    clips = [PROJECT / x["loop"] for x in records]
    inputs = sum((["-stream_loop", "-1", "-i", str(path)] for path in clips), [])
    labels = "".join(f"[{i}:v]trim=duration=6,setpts=PTS-STARTPTS[v{i}];" for i in range(len(clips)))
    last = "v0"
    for i in range(1, len(clips)):
        labels += f"[{last}][v{i}]xfade=transition=fade:duration=1:offset={5 * i}[x{i}];"
        last = f"x{i}"
    font = "C\\:/Windows/Fonts/GARA.TTF"
    labels += f"[{last}]drawtext=fontfile='{font}':text='MOUNTAIN NOIR':x=(w-text_w)/2:y=h*0.84:fontsize=38:fontcolor=white@0.72:shadowcolor=black@0.55:shadowx=2:shadowy=2,drawtext=fontfile='{font}':text='@mountainnoir':x=48:y=h-62:fontsize=23:fontcolor=white@0.42[out]"
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", labels, "-map", "[out]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", str(proof)])
    return proof


def write_plan(records: list[dict], proof: Path) -> None:
    RENDER.mkdir(parents=True, exist_ok=True)
    plan = {
        "schema": "aivideoedit.mainv2-source-derived-living-plan.v1",
        "source_rule": "finalized song films are used only for extracted stills; their moving picture and audio are excluded",
        "frame_rate": FPS,
        "loop_seconds": LOOP_SECONDS,
        "sections": records,
        "proof": {"file_or_locator": str(proof.relative_to(PROJECT)), "sha256": sha256(proof)},
    }
    (RENDER / "SOURCE_DERIVED_LIVING_PLAN.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")


def build_audio() -> Path:
    audio = PROJECT / "assets" / "audio"
    temp = RENDER / "audio"
    temp.mkdir(parents=True, exist_ok=True)
    core = temp / "core-crossfaded.wav"
    tail_seed = temp / "el-viento-tail.wav"
    tail_loop = temp / "el-viento-extended-tail.wav"
    final = temp / "master-audio.wav"
    crossfade = 1.25
    core_duration = 187.12 + 198.84 + 207.44 + 158.64 - 3 * crossfade
    tail_duration = 900.0 - core_duration + 2.0
    tracks = [
        audio / "Irish eyes (Remastered).wav",
        audio / "Leave It by the Door.wav",
        audio / "Silver Coin (Remastered).wav",
        audio / "El Viento trae tu nombre Instrumental.wav",
    ]
    inputs = sum((["-i", str(track)] for track in tracks), [])
    graph = (
        f"[0:a][1:a]acrossfade=d={crossfade}:c1=qsin:c2=qsin[a01];"
        f"[a01][2:a]acrossfade=d={crossfade}:c1=qsin:c2=qsin[a02];"
        f"[a02][3:a]acrossfade=d={crossfade}:c1=qsin:c2=qsin[core]"
    )
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph, "-map", "[core]", "-c:a", "pcm_s16le", str(core)])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-sseof", "-12", "-i", str(tracks[3]), "-t", "12", "-c:a", "pcm_s16le", str(tail_seed)])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-stream_loop", "20", "-i", str(tail_seed), "-t", f"{tail_duration:.4f}", "-c:a", "pcm_s16le", str(tail_loop)])
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(core), "-i", str(tail_loop),
        "-filter_complex", "[0:a][1:a]acrossfade=d=2:c1=qsin:c2=qsin,afade=t=out:st=896:d=4[a]",
        "-map", "[a]", "-t", "900", "-c:a", "pcm_s16le", str(final),
    ])
    return final


def build_visual_master(records: list[dict]) -> Path:
    output = RENDER / "Mountain_Noir_After_Midnight_15min_PICTURE.mp4"
    fade = 1.0
    segment = (900.0 + fade * (len(records) - 1)) / len(records)
    inputs = sum((["-stream_loop", "-1", "-i", str(PROJECT / item["loop"])] for item in records), [])
    graph = "".join(f"[{i}:v]trim=duration={segment:.6f},setpts=PTS-STARTPTS[v{i}];" for i in range(len(records)))
    previous = "v0"
    for i in range(1, len(records)):
        offset = (segment - fade) * i
        graph += f"[{previous}][v{i}]xfade=transition=fade:duration={fade}:offset={offset:.6f}[x{i}];"
        previous = f"x{i}"
    font = "C\\:/Windows/Fonts/GARA.TTF"
    graph += (
        f"[{previous}]drawtext=fontfile='{font}':text='MOUNTAIN NOIR':x=(w-text_w)/2:y=h*0.84:fontsize=38:"
        "fontcolor=white@0.66:shadowcolor=black@0.55:shadowx=2:shadowy=2:alpha='0.40+0.22*sin(2*PI*t/17)',"
        f"drawtext=fontfile='{font}':text='@mountainnoir':x=48:y=h-62:fontsize=23:fontcolor=white@0.40[out]"
    )
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph,
        "-map", "[out]", "-an", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output),
    ])
    return output


def build_master(records: list[dict]) -> Path:
    picture = build_visual_master(records)
    audio = build_audio()
    master = PROJECT / "renders" / "Mountain_Noir_After_Midnight_15min_WORKPRINT_v2_MainV2.mp4"
    master.parent.mkdir(parents=True, exist_ok=True)
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(picture), "-i", str(audio),
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", "900", "-movflags", "+faststart", str(master),
    ])
    write_plan(records, master)
    return master


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--proof", action="store_true")
    args = ap.parse_args()
    records = render_all_loops(proof=args.proof)
    if args.proof:
        proof = make_proof(records)
        write_plan(records, proof)
        print(proof)
    else:
        print(build_master(records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
