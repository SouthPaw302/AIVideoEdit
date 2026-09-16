#!/usr/bin/env python3
"""Render Scene 03 Assembly06 from the full eligible media pool + approved main FX.

Design goals:
- Preserve the locked 98.000 s / 2352-frame / 24 fps timeline.
- Treat Assembly05's 29 segments as the current cut, not a source-library ceiling.
- Add eligible promoted/non-hero Scene 03 coverage when it is present in media-root.
- Use only current-main FX whose registry gate_status is approved.
- Preserve already-gated Scene 03 GIF/matched-angle assets as source coverage.
- Fail closed on hard-rejected media, unavailable/proof-required main FX, or missing
  required Assembly05 coverage unless --allow-missing is explicitly supplied.

Heavy media is intentionally not stored in GitHub. Restore/download the Scene 03
media workspace first, then pass --media-root, --score and --captions-ass.
"""
from __future__ import annotations

import argparse
import difflib
import importlib.util
import json
import math
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import cv2
import numpy as np

FPS = 24
WIDTH = 1280
HEIGHT = 720
TOTAL_FRAMES = 2352
DURATION = 98.0
SCENE_DIR = Path(__file__).resolve().parent
REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_MEDIA_PLAN = SCENE_DIR / "ASSEMBLY05_MEDIA_PLAN.json"
DEFAULT_FX_PLAN = SCENE_DIR / "SCENE03_FX_EXECUTION_PLAN.json"
DEFAULT_AUDIT = SCENE_DIR / "SCENE03_MEDIA_AUDIT.json"
REGISTRY_PATH = REPO_ROOT / "general/reusable/fx_v2/registry.json"
RUNTIME_PATH = REPO_ROOT / "general/reusable/fx_v2/runtime.py"
PROMOTED_PATH = REPO_ROOT / "general/reusable/fx_v2/promoted_effects.py"

MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".mkv", ".avi"}
INTERIOR_TOKENS = {"apartment", "hallway", "corridor", "elevator", "lobby", "interior"}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def normalize_name(name: str) -> str:
    s = Path(name).stem.lower()
    s = re.sub(r"^s3_gen_", "", s)
    s = re.sub(r"_fx_angle_loop$", "", s)
    s = re.sub(r"_angle_[ab]$", "", s)
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s


def token_set(name: str) -> set[str]:
    return {t for t in normalize_name(name).split("_") if len(t) > 2}


def build_media_index(root: Path) -> tuple[list[Path], dict[str, list[Path]]]:
    files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in MEDIA_SUFFIXES]
    by_norm: dict[str, list[Path]] = {}
    for p in files:
        by_norm.setdefault(normalize_name(p.name), []).append(p)
    return files, by_norm


def fuzzy_score(requested: str, candidate: Path) -> float:
    a = normalize_name(requested)
    b = normalize_name(candidate.name)
    seq = difflib.SequenceMatcher(None, a, b).ratio()
    ta, tb = token_set(a), token_set(b)
    jac = len(ta & tb) / max(1, len(ta | tb))
    contain = 1.0 if a in b or b in a else 0.0
    return max(seq * 0.72 + jac * 0.28, 0.82 * contain + 0.18 * jac)


def resolve_source(requested: str, all_files: list[Path], by_norm: dict[str, list[Path]]) -> Path | None:
    n = normalize_name(requested)
    exact = by_norm.get(n, [])
    if exact:
        return sorted(exact, key=lambda p: (p.suffix.lower() not in {".gif", ".mp4"}, len(p.as_posix())))[0]

    # A hero still may have an already-proved GIF companion; prefer that as coverage.
    m = re.fullmatch(r"s3h(0[1-8])", n)
    if m:
        hid = f"S3H{m.group(1)}"
        wanted = normalize_name(f"{hid}_FX_ANGLE_LOOP.gif")
        if wanted in by_norm:
            return by_norm[wanted][0]

    scored = [(fuzzy_score(requested, p), p) for p in all_files]
    scored.sort(key=lambda x: x[0], reverse=True)
    if scored and scored[0][0] >= 0.58:
        return scored[0][1]
    return None


def fit_frame(frame: np.ndarray) -> np.ndarray:
    if frame is None or frame.size == 0:
        raise RuntimeError("Empty frame")
    h, w = frame.shape[:2]
    if w == WIDTH and h == HEIGHT:
        return frame
    src_ar = w / max(h, 1)
    dst_ar = WIDTH / HEIGHT
    if abs(src_ar - dst_ar) < 0.02:
        return cv2.resize(frame, (WIDTH, HEIGHT), interpolation=cv2.INTER_LANCZOS4)
    scale = min(WIDTH / w, HEIGHT / h)
    nw, nh = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
    resized = cv2.resize(frame, (nw, nh), interpolation=cv2.INTER_LANCZOS4)
    left = (WIDTH - nw) // 2
    right = WIDTH - nw - left
    top = (HEIGHT - nh) // 2
    bottom = HEIGHT - nh - top
    return cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_REFLECT_101)


class FrameSource:
    def __init__(self, path: Path):
        self.path = path
        self.static: np.ndarray | None = None
        self.cap: cv2.VideoCapture | None = None
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            self.static = cv2.imread(str(path), cv2.IMREAD_COLOR)
            if self.static is None:
                raise RuntimeError(f"Cannot read image: {path}")
        else:
            self.cap = cv2.VideoCapture(str(path))
            if not self.cap.isOpened():
                raise RuntimeError(f"Cannot open animated/video source: {path}")

    def next(self) -> np.ndarray:
        if self.static is not None:
            return self.static.copy()
        assert self.cap is not None
        ok, frame = self.cap.read()
        if not ok:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ok, frame = self.cap.read()
        if not ok or frame is None:
            raise RuntimeError(f"Cannot decode frame from {self.path}")
        return frame

    def close(self) -> None:
        if self.cap is not None:
            self.cap.release()


@dataclass
class CoverageItem:
    requested: str
    path: Path
    weight: float
    required: bool
    origin: str


def largest_remainder(weights: list[float], total: int) -> list[int]:
    if not weights:
        return []
    s = sum(max(0.001, w) for w in weights)
    raw = [max(0.001, w) / s * total for w in weights]
    base = [int(math.floor(x)) for x in raw]
    remaining = total - sum(base)
    order = sorted(range(len(raw)), key=lambda i: raw[i] - base[i], reverse=True)
    for i in order[:remaining]:
        base[i] += 1
    return base


def role_to_shots(role: str) -> set[str]:
    out: set[str] = set()
    for token in role.split("/"):
        token = token.strip()
        m = re.fullmatch(r"S3H(0[1-8])", token)
        if m:
            out.add(f"S3-{m.group(1)}")
        elif re.fullmatch(r"S3-0[1-8]", token):
            out.add(token)
    return out


def collect_extra_requests(audit: dict[str, Any]) -> dict[str, list[str]]:
    result = {f"S3-{i:02d}": [] for i in range(1, 9)}
    for item in audit.get("known_named_generated_coverage", []):
        if not str(item.get("status", "")).startswith("eligible"):
            continue
        for sid in role_to_shots(str(item.get("map", ""))):
            result[sid].append(item["name"])
    for item in audit.get("legacy_promoted_assets_from_asset_manifest", []):
        if not str(item.get("status", "")).startswith("approved_by_promotion"):
            continue
        for sid in role_to_shots(str(item.get("mapped_role", ""))):
            result[sid].append(item["name"])
    for i in range(1, 9):
        result[f"S3-{i:02d}"].append(f"S3H{i:02d}.png")
    return result


def is_exterior_source(shot_id: str, source_name: str) -> bool:
    if shot_id not in {"S3-06", "S3-07", "S3-08"}:
        return False
    toks = token_set(source_name)
    if toks & INTERIOR_TOKENS:
        return False
    return True


def validate_fx_plan(plan: dict[str, Any], registry: dict[str, Any]) -> None:
    effects = registry["effects"]
    failures: list[str] = []
    for shot in plan["shots"]:
        for fx in shot.get("effects", []):
            eid = fx["id"]
            entry = effects.get(eid)
            if not entry:
                failures.append(f"{shot['shot_id']}: unknown FX id {eid}")
                continue
            if entry.get("gate_status") != "approved":
                failures.append(f"{shot['shot_id']}: {eid} gate_status={entry.get('gate_status')}")
    if failures:
        raise RuntimeError("FX plan failed current-main gate:\n" + "\n".join(failures))


def blend(a: np.ndarray, b: np.ndarray, amount: float) -> np.ndarray:
    amount = float(np.clip(amount, 0.0, 1.0))
    return cv2.addWeighted(a, 1.0 - amount, b, amount, 0)


def apply_fx_stack(
    frame: np.ndarray,
    shot: dict[str, Any],
    source_name: str,
    local_t: float,
    segment_duration: float,
    frame_index: int,
    runtime_mod: Any,
    promoted_mod: Any,
    fx_runtime: Any,
) -> np.ndarray:
    current = frame
    ctx = runtime_mod.FXContext(
        t=local_t,
        duration=max(segment_duration, 1.0 / FPS),
        frame_index=frame_index,
        fps=FPS,
        energy=float(shot.get("energy", 0.5)),
        transient=0.18,
        brightness=0.0,
    )
    for fx in shot.get("effects", []):
        if fx.get("requires_exterior") and not is_exterior_source(shot["shot_id"], source_name):
            continue
        mix = float(fx.get("mix", 1.0))
        if fx["engine"] == "runtime":
            params = {"id": fx["id"], "strength": float(fx.get("strength", 1.0))}
            if "roi" in fx:
                params["roi"] = fx["roi"]
            if "origin" in fx:
                params["origin"] = fx["origin"]
            effected = fx_runtime.apply(current, params, ctx)
        elif fx["engine"] == "promoted":
            effected = promoted_mod.apply_effect(
                fx["effect_name"],
                current,
                local_t,
                duration=max(segment_duration, 1.0 / FPS),
                energy=float(shot.get("energy", 0.5)),
                transient=0.18,
            )
        else:
            raise RuntimeError(f"Unknown FX engine: {fx['engine']}")
        current = blend(current, effected, mix)
    return current


def build_coverage(
    beat: dict[str, Any],
    extra_requests: dict[str, list[str]],
    all_files: list[Path],
    by_norm: dict[str, list[Path]],
    hard_exclusions: set[str],
    allow_missing: bool,
) -> tuple[list[CoverageItem], list[dict[str, Any]]]:
    sid = beat["beat"]
    requested: list[tuple[str, float, bool, str]] = []
    for seg in beat["segments"]:
        requested.append((seg["source"], float(seg["duration"]), True, "assembly05"))
    for name in extra_requests.get(sid, []):
        requested.append((name, 2.4, False, "full_media_audit"))

    seen_paths: set[str] = set()
    seen_norms: set[str] = set()
    coverage: list[CoverageItem] = []
    report: list[dict[str, Any]] = []
    for name, weight, required, origin in requested:
        n = normalize_name(name)
        if n in hard_exclusions:
            report.append({"requested": name, "status": "excluded_hard_reject", "origin": origin})
            continue
        if n in seen_norms:
            report.append({"requested": name, "status": "deduplicated_alias", "origin": origin})
            continue
        path = resolve_source(name, all_files, by_norm)
        if path is None:
            report.append({"requested": name, "status": "missing", "origin": origin, "required": required})
            if required and not allow_missing:
                raise FileNotFoundError(f"Required {sid} source not found under media-root: {name}")
            continue
        rp = str(path.resolve())
        if rp in seen_paths:
            report.append({"requested": name, "status": "deduplicated_same_file", "resolved": str(path), "origin": origin})
            continue
        seen_norms.add(n)
        seen_paths.add(rp)
        coverage.append(CoverageItem(name, path, weight, required, origin))
        report.append({"requested": name, "status": "resolved", "resolved": str(path), "origin": origin})

    if not coverage:
        raise RuntimeError(f"No usable coverage resolved for {sid}")
    return coverage, report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--media-root", type=Path, required=True)
    ap.add_argument("--score", type=Path, required=True)
    ap.add_argument("--captions-ass", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--media-plan", type=Path, default=DEFAULT_MEDIA_PLAN)
    ap.add_argument("--fx-plan", type=Path, default=DEFAULT_FX_PLAN)
    ap.add_argument("--media-audit", type=Path, default=DEFAULT_AUDIT)
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    media_root = args.media_root.resolve()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    media_plan = json.loads(args.media_plan.read_text(encoding="utf-8"))
    fx_plan = json.loads(args.fx_plan.read_text(encoding="utf-8"))
    audit = json.loads(args.media_audit.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    validate_fx_plan(fx_plan, registry)

    runtime_mod = load_module("aivideoedit_fx_runtime", RUNTIME_PATH)
    promoted_mod = load_module("aivideoedit_promoted_effects", PROMOTED_PATH)
    fx_runtime = runtime_mod.FXRuntime(seed=302)

    all_files, by_norm = build_media_index(media_root)
    if not all_files:
        raise RuntimeError(f"No supported media files found under {media_root}")

    extra_requests = collect_extra_requests(audit)
    hard_exclusions = {normalize_name(x["name"]) for x in audit.get("hard_exclusions", [])}
    shot_plan = {x["shot_id"]: x for x in fx_plan["shots"]}

    coverage_report: dict[str, Any] = {
        "schema": "aivideoedit.scene03-assembly06-coverage-report.v1",
        "media_root": str(media_root),
        "full_media_policy": audit["policy"],
        "beats": [],
        "unresolved_anonymous_media": audit.get("anonymous_generated_files", {}),
    }

    render_jobs: list[tuple[str, CoverageItem, int, int]] = []
    expected_total = 0
    for beat in media_plan["beats"]:
        sid = beat["beat"]
        beat_frames = int(beat["frames"][1]) - int(beat["frames"][0]) + 1
        coverage, report = build_coverage(
            beat, extra_requests, all_files, by_norm, hard_exclusions, args.allow_missing
        )
        counts = largest_remainder([x.weight for x in coverage], beat_frames)
        if sum(counts) != beat_frames:
            raise RuntimeError(f"Frame allocation error in {sid}")
        beat_report = {
            "shot_id": sid,
            "locked_frames": beat_frames,
            "resolved_coverage_count": len(coverage),
            "sources": report,
            "allocated": [],
        }
        for item, count in zip(coverage, counts):
            beat_report["allocated"].append({
                "requested": item.requested,
                "resolved": str(item.path),
                "frames": count,
                "origin": item.origin,
            })
            render_jobs.append((sid, item, count, beat_frames))
        coverage_report["beats"].append(beat_report)
        expected_total += beat_frames

    if expected_total != TOTAL_FRAMES:
        raise RuntimeError(f"Locked timeline mismatch: expected {TOTAL_FRAMES}, got {expected_total}")

    report_path = output.with_suffix(".coverage.json")
    report_path.write_text(json.dumps(coverage_report, indent=2), encoding="utf-8")
    if args.dry_run:
        print(report_path)
        return 0

    picture = output.with_name(output.stem + "_PICTURE_ONLY.mp4")
    enc = subprocess.Popen(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{WIDTH}x{HEIGHT}",
            "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
            "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", str(picture),
        ],
        stdin=subprocess.PIPE,
    )
    if enc.stdin is None:
        raise RuntimeError("Could not open ffmpeg stdin")

    global_frame = 0
    try:
        for sid, item, count, _beat_frames in render_jobs:
            shot = shot_plan[sid]
            src = FrameSource(item.path)
            try:
                seg_duration = count / FPS
                for i in range(count):
                    frame = fit_frame(src.next())
                    t = i / FPS
                    frame = apply_fx_stack(
                        frame, shot, item.requested, t, seg_duration, global_frame,
                        runtime_mod, promoted_mod, fx_runtime,
                    )
                    enc.stdin.write(np.ascontiguousarray(frame).tobytes())
                    global_frame += 1
            finally:
                src.close()
    finally:
        enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError("ffmpeg picture encode failed")
    if global_frame != TOTAL_FRAMES:
        raise RuntimeError(f"Rendered {global_frame} frames, expected {TOTAL_FRAMES}")

    vf = f"ass={args.captions_ass.resolve().as_posix()}"
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(picture), "-i", str(args.score.resolve()),
        "-filter_complex", f"[0:v]{vf}[v];[1:a]atrim=0:{DURATION},asetpts=PTS-STARTPTS[a]",
        "-map", "[v]", "-map", "[a]", "-frames:v", str(TOTAL_FRAMES),
        "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k",
        "-movflags", "+faststart", str(output),
    ])
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
