#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

VIDEO_SHA = "162b3c5cf6c41cc1b85800a1e6111a94df3e3dd829935521aa8c90de15e51803"
AUDIO_SHA = "6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92"
FPS = 24
TRANSITION = 0.8


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def duration(path: Path) -> float:
    value = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        text=True,
    )
    return float(value.strip())


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def section_filter(index: int) -> str:
    crops = [
        "80+60*sin(2*PI*t/11):150+28*cos(2*PI*t/9)",
        "32+90*cos(2*PI*t/13):120+32*sin(2*PI*t/8)",
        "110+38*sin(2*PI*t/10):170+44*cos(2*PI*t/12)",
        "55+72*cos(2*PI*t/15):100+24*sin(2*PI*t/10)",
        "88+50*sin(2*PI*t/17):132+35*cos(2*PI*t/11)",
        "20+112*cos(2*PI*t/14):190+26*sin(2*PI*t/9)",
        "125+25*sin(2*PI*t/9):90+48*cos(2*PI*t/14)",
        "70+70*cos(2*PI*t/16):145+30*sin(2*PI*t/10)",
    ]
    looks = [
        "eq=contrast=1.08:brightness=0.02:saturation=1.16,colorbalance=rs=.03:gs=.01:bs=-.02",
        "hflip,eq=contrast=1.12:brightness=0.01:saturation=1.28,colorbalance=rs=.08:gs=.02:bs=-.06",
        "hue=s=0,eq=contrast=1.22:brightness=-.02",
        "eq=contrast=1.06:brightness=0.00:saturation=1.12,colorbalance=rs=-.04:gs=.03:bs=.10",
        "tmix=frames=3:weights=1 1 1,eq=contrast=1.04:brightness=.02:saturation=1.04",
        "eq=contrast=1.14:brightness=.04:saturation=1.42,colorbalance=rs=.10:gs=.03:bs=-.08",
        "hflip,eq=contrast=1.18:brightness=-.05:saturation=1.18,colorbalance=rs=.04:gs=-.02:bs=.12",
        "eq=contrast=1.05:brightness=.01:saturation=1.10,colorbalance=rs=.01:gs=.01:bs=.01",
    ][index]
    return f"scale=1440:1440:flags=lanczos,crop=1280:720:x='{crops[index].split(':')[0]}':y='{crops[index].split(':')[1]}',{looks},unsharp=5:5:0.18:3:3:0.0,fps=24,format=yuv420p"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()
    video = Path(args.video).resolve()
    audio = Path(args.audio).resolve()
    out = Path(args.out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    if sha256(video) != VIDEO_SHA:
        raise SystemExit("uploaded video hash mismatch")
    if sha256(audio) != AUDIO_SHA:
        raise SystemExit("canonical WAV hash mismatch")
    target = duration(audio)
    if abs(target - 207.44) > 0.08:
        raise SystemExit(f"unexpected audio duration: {target}")
    section_duration = (target + TRANSITION * 7) / 8
    sections = out / "sections"
    sections.mkdir(exist_ok=True)
    section_paths: list[Path] = []
    for i in range(8):
        p = sections / f"test2_section_{i+1:02d}.mp4"
        run([
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-stream_loop", "-1", "-i", str(video), "-t", f"{section_duration:.6f}",
            "-an", "-vf", section_filter(i), "-c:v", "libx264", "-preset", "medium",
            "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), str(p),
        ])
        section_paths.append(p)
    inputs: list[str] = []
    for p in section_paths:
        inputs += ["-i", str(p)]
    filters: list[str] = []
    current = "[0:v]"
    elapsed = section_duration
    transitions = ["fadeblack", "wipeleft", "circleopen", "slideleft", "fade", "hblur", "fadeblack"]
    for i in range(1, 8):
        label = f"[x{i}]"
        offset = elapsed - TRANSITION
        filters.append(f"{current}[{i}:v]xfade=transition={transitions[i-1]}:duration={TRANSITION}:offset={offset:.6f}{label}")
        current = label
        elapsed += section_duration - TRANSITION
    filters.append(f"{current}trim=duration={target:.6f},setpts=PTS-STARTPTS[v]")
    final = out / "Silver_Coin_Test2_1280x720_24fps.mp4"
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs,
        "-i", str(audio), "-filter_complex", ";".join(filters),
        "-map", "[v]", "-map", "8:a:0", "-c:v", "libx264", "-preset", "medium",
        "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac",
        "-b:a", "320k", "-ar", "48000", "-ac", "2", "-t", f"{target:.6f}",
        "-movflags", "+faststart", str(final),
    ])
    report = {
        "schema": "aivideoedit.test2-render-report.v1",
        "branch": "song/silver-coin-test-2",
        "visual_source": video.name,
        "visual_source_sha256": sha256(video),
        "audio_source": audio.name,
        "audio_source_sha256": sha256(audio),
        "excluded_old_media": True,
        "duration_seconds": duration(final),
        "resolution": [1280, 720],
        "fps": FPS,
        "output": final.name,
        "output_sha256": sha256(final),
        "chapters": 8,
        "transitions": transitions,
        "render_method": "source-only reframing, bounded crop drift, chapter looks, and xfade transitions",
    }
    (out / "TEST2_RENDER_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
