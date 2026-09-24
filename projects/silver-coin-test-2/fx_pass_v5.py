#!/usr/bin/env python3
"""Shot-aware Silver Coin finishing pass using current-main FX V2 implementations.

The picture edit is input; this script changes neither shot timing nor source audio.
Each added motion layer is bounded to a scene ROI and the central performer is
protected from the background deformation. The IronFlame-style room orbit is a
project-specific use of the approved promoted rotating-architecture adapter.
"""
from __future__ import annotations

import argparse
import bisect
import json
import math
import subprocess
import sys
import wave
from pathlib import Path

import cv2
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / ".aivideoedit/os/general/reusable/fx_v2"))
from runtime import FXContext, FXRuntime  # noqa: E402
from promoted_effects import apply_effect  # noqa: E402


def audio_controls(path: Path, count: int, fps: int) -> tuple[np.ndarray, np.ndarray]:
    with wave.open(str(path), "rb") as wav:
        assert wav.getsampwidth() == 2 and wav.getnchannels() == 2
        sr = wav.getframerate()
        samples = np.frombuffer(wav.readframes(wav.getnframes()), dtype="<i2").reshape(-1, 2)
    mono = samples.astype(np.float32).mean(axis=1) / 32768.0
    energy = np.zeros(count, np.float32)
    for i in range(count):
        center = int((i + .5) / fps * sr)
        window = mono[max(0, center - 2048):min(len(mono), center + 2048)]
        energy[i] = float(np.sqrt(np.mean(window * window))) if len(window) else 0.0
    denom = max(float(np.percentile(energy, 95)), .001)
    energy = np.clip(energy / denom, 0, 1)
    smoothed = cv2.GaussianBlur(energy.reshape(1, -1), (1, 1), 0).reshape(-1)
    transient = np.clip((energy - np.roll(smoothed, 3)) * 3, 0, 1)
    transient[:3] = 0
    return energy, transient


def subject_mask(shape: tuple[int, int], centers: list[list[float]]) -> np.ndarray:
    h, w = shape
    mask = np.zeros((h, w), np.float32)
    for cx, cy, rx, ry in centers:
        cv2.ellipse(mask, (int(cx * w), int(cy * h)), (int(rx * w), int(ry * h)), 0, 0, 360, 1, -1)
    return cv2.GaussianBlur(mask, (0, 0), 12)


def transition_frame(runtime: FXRuntime, a: np.ndarray, b: np.ndarray, p: float, kind: str) -> np.ndarray:
    if kind == "doorway":
        out = runtime.doorway_depth_gate(a, b, p, door_roi=(.32, .06, .72, .98), strength=.72)
    elif kind == "ember":
        out = runtime.ember_to_light(a, b, p, origin=(.82, .36), strength=.9)
    else:
        out = runtime.light_peak_handoff(a, b, p, origin=(.78, .20), strength=.55)
    # Complete the handoff by the cut so it never snaps back to the old image.
    q = np.clip((p - .78) / .22, 0, 1)
    return cv2.addWeighted(out, 1 - q, b, q, 0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, default=HERE / "FX_PASS_v5.json")
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--start-frame", type=int, default=0)
    ap.add_argument("--end-frame", type=int)
    args = ap.parse_args()

    cfg = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    picture = json.loads((HERE / cfg["picture_manifest"]).read_text(encoding="utf-8-sig"))
    scenes = picture["scenes"]
    fps = int(picture["fps"])
    start_times = np.cumsum([0.0] + [float(s["duration"]) for s in scenes])
    starts = [int(round(t * fps)) for t in start_times]
    total = starts[-1]
    energy, transient = audio_controls(HERE / cfg["audio"], total, fps)
    cap = cv2.VideoCapture(str(args.input))
    assert cap.isOpened(), args.input
    input_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    end = min(args.end_frame or total, total, input_total)
    assert 0 <= args.start_frame < end <= total
    cap.set(cv2.CAP_PROP_POS_FRAMES, args.start_frame)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    assert (width, height) == (1280, 720), (width, height)
    small = (480, 270)
    runtime = FXRuntime(seed=int(cfg.get("seed", 302)))

    # A second reader provides the destination image for short motivated gates.
    lookahead = cv2.VideoCapture(str(args.input))
    transition_by_scene = {x["after"]: x for x in cfg["transitions"]}
    next_plates = {}
    for scene_id, spec in transition_by_scene.items():
        si = next(i for i, s in enumerate(scenes) if s["id"] == scene_id)
        frame_no = min(input_total - 1, starts[si + 1] + 3)
        lookahead.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ok, frame = lookahead.read()
        if not ok:
            raise RuntimeError(f"cannot fetch transition destination {scene_id}")
        next_plates[scene_id] = cv2.resize(frame, small, interpolation=cv2.INTER_AREA)
    lookahead.release()

    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
           "-s", f"{width}x{height}", "-r", str(fps), "-i", "-", "-an",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", str(args.output)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    scene_seen = None
    protect = None
    try:
        for fi in range(args.start_frame, end):
            ok, frame = cap.read()
            if not ok:
                raise RuntimeError(f"picture ended at frame {fi}")
            si = min(len(scenes) - 1, bisect.bisect_right(starts, fi) - 1)
            scene = scenes[si]
            sid = scene["id"]
            local = (fi - starts[si]) / fps
            if sid != scene_seen:
                scene_seen = sid
                protect = subject_mask((small[1], small[0]), cfg["protect"].get(sid, cfg["protect_default"]))
            ctx = FXContext(t=local, duration=float(cfg["loop_seconds"]), frame_index=fi,
                            fps=fps, energy=float(energy[fi]), transient=float(transient[fi]))
            source = cv2.resize(frame, small, interpolation=cv2.INTER_AREA)
            treated = source.copy()
            family = scene["family"]
            for effect in cfg["family_layers"].get(family, []):
                treated = runtime.apply(treated, effect, ctx, protect=protect)
            for effect in cfg["scene_layers"].get(sid, []):
                treated = runtime.apply(treated, effect, ctx, protect=protect)
            if sid in ("SC19", "SC27"):
                # IronFlame 2:15-inspired unstable architecture, stable performer.
                room = apply_effect("rotating_architecture_debris", treated, local, 4.0,
                                    float(energy[fi]), float(transient[fi]))
                treated = cv2.addWeighted(treated, .84, room, .16, 0)
            if sid in cfg["halation_scenes"]:
                treated = apply_effect("warm_halation_bloom", treated, local, 4.0,
                                       float(energy[fi]), float(transient[fi]))
            # Keep faces, anatomy, coins and fiddles fixed while surroundings move.
            alpha = np.clip(protect * .96, 0, 1)[..., None]
            treated = np.uint8(np.clip(treated.astype(np.float32) * (1 - alpha) + source.astype(np.float32) * alpha, 0, 255))
            if sid in ("SC01", "SC15"):
                beat = 0.5 + 0.5 * math.sin(local * 4.0)
                if beat > .82:
                    cx, cy = ((.475, .72) if sid == "SC01" else (.812, .305))
                    center = (int(cx * small[0]), int(cy * small[1]))
                    ring = np.zeros_like(treated)
                    cv2.circle(ring, center, int(14 + 5 * beat), (135, 205, 245), 2, cv2.LINE_AA)
                    treated = cv2.addWeighted(treated, 1.0, ring, .42, 0)
            spec = transition_by_scene.get(sid)
            if spec:
                duration_frames = int(round(float(spec["duration"]) * fps))
                edge = starts[si + 1]
                if edge - duration_frames <= fi < edge:
                    p = (fi - (edge - duration_frames) + 1) / duration_frames
                    treated = transition_frame(runtime, treated, next_plates[sid], p, spec["kind"])
            # Retain the full-resolution painting detail beneath the animated layer.
            full_fx = cv2.resize(treated, (width, height), interpolation=cv2.INTER_CUBIC)
            mix = .38 if sid in ("SC19", "SC27") else .46
            out = cv2.addWeighted(frame, 1 - mix, full_fx, mix, 0)
            flames = [x for x in cfg["scene_layers"].get(sid, []) if x["id"] == "FX2-FIRE-001"]
            if flames:
                fire_mask = runtime.roi_mask(frame.shape, flames[0]["roi"], blur=18)
                extra = (fire_mask * .25).astype(np.float32)[..., None]
                out = np.uint8(np.clip(out.astype(np.float32) * (1 - extra) + full_fx.astype(np.float32) * extra, 0, 255))
            if sid in ("SC19", "SC27"):
                angle = (1.8 if sid == "SC19" else 2.1) * math.sin(local * 1.55)
                matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1.018)
                room = cv2.warpAffine(out, matrix, (width, height), borderMode=cv2.BORDER_REFLECT_101)
                hero = cv2.resize(protect, (width, height), interpolation=cv2.INTER_CUBIC)[..., None]
                out = np.uint8(np.clip(room.astype(np.float32) * (1 - hero) + frame.astype(np.float32) * hero, 0, 255))
            proc.stdin.write(out.tobytes())
            if (fi + 1) % 240 == 0:
                print(f"FX frames {fi + 1}/{end}", flush=True)
    finally:
        cap.release()
        if proc.stdin:
            proc.stdin.close()
    rc = proc.wait()
    if rc:
        raise RuntimeError(f"ffmpeg exited {rc}")
    meta = {"schema": "aivideoedit.fx-pass-render.v1", "source": str(args.input),
            "manifest": str(args.manifest), "start_frame": args.start_frame,
            "end_frame": end, "frame_count": end - args.start_frame,
            "fx_runtime": "current-main FX V2", "resolution": [width, height], "fps": fps}
    args.output.with_suffix(args.output.suffix + ".json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
