from __future__ import annotations

import argparse
from array import array
import json
import math
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

from runtime_v2.models.music_beat import analyze_music
from runtime_v2.models.provision import provision
from runtime_v2.models.registry import ModelRegistry, inferred_repo_root

PINNED_BEAT_MODEL = "music.beat.beat-this-onnx.v1"


def _click_wav(path: Path, *, bpm: float = 120.0, seconds: float = 8.0, rate: int = 22050) -> None:
    total = int(seconds * rate)
    data = array("h", [0]) * total
    period = int(rate * 60.0 / bpm)
    width = int(0.025 * rate)
    for start in range(0, total, period):
        for i in range(start, min(total, start + width)):
            t = (i - start) / rate
            data[i] = int(
                22000
                * math.sin(2 * math.pi * 1000 * t)
                * max(0.0, 1.0 - t / 0.025)
            )
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(data.tobytes())


def run_micro_tests(repo_root: Path) -> dict:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "runtime_v2/tests"],
        cwd=repo_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "status": "PASS" if proc.returncode == 0 else "FAIL",
        "returncode": proc.returncode,
        "stdout_tail": proc.stdout[-6000:],
        "stderr_tail": proc.stderr[-6000:],
    }


def run_real_onnx_checkpoint(*, provision_model: bool = False) -> dict:
    registry = ModelRegistry.load_default()
    if provision_model:
        provision(PINNED_BEAT_MODEL)

    resolution = registry.resolve(PINNED_BEAT_MODEL)
    if not resolution.available or resolution.resolved != PINNED_BEAT_MODEL:
        return {
            "status": "NOT_READY",
            "model": PINNED_BEAT_MODEL,
            "resolution": {
                "resolved": resolution.resolved,
                "available": resolution.available,
                "used_fallback": resolution.used_fallback,
                "reason": resolution.reason,
            },
        }

    with tempfile.TemporaryDirectory(prefix="aive-v2-onnx-") as td:
        fixture = Path(td) / "click-120bpm.wav"
        _click_wav(fixture)
        evidence = analyze_music(fixture, registry=registry)

    bpm = evidence.get("bpm")
    beats = evidence.get("beat_positions_seconds") or []
    passed = (
        evidence.get("engine") == "beat_this_onnx"
        and isinstance(bpm, (int, float))
        and 112.0 <= float(bpm) <= 128.0
        and len(beats) >= 6
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "model": PINNED_BEAT_MODEL,
        "engine": evidence.get("engine"),
        "bpm": bpm,
        "beat_count": len(beats),
        "model_resolution": evidence.get("model_resolution"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Run bounded Runtime V2 verification without a full production"
    )
    ap.add_argument(
        "--skip-tests",
        action="store_true",
        help="Skip the Runtime V2 pytest micro-suite.",
    )
    ap.add_argument(
        "--require-onnx",
        action="store_true",
        help="Fail unless the pinned Beat This ONNX CPU checkpoint passes.",
    )
    ap.add_argument(
        "--provision-model",
        action="store_true",
        help="Download/verify the pinned ONNX model before the real CPU checkpoint.",
    )
    args = ap.parse_args()

    repo_root = inferred_repo_root()
    report = {
        "schema": "aivideoedit.runtime-v2-verification.v1",
        "repo_root": str(repo_root),
        "micro_tests": (
            {"status": "SKIPPED"}
            if args.skip_tests
            else run_micro_tests(repo_root)
        ),
        "onnx_checkpoint": run_real_onnx_checkpoint(
            provision_model=args.provision_model
        ),
        "full_production": {
            "status": "NOT_RUN",
            "reason": "reserved for explicit integration checkpoint",
        },
    }

    failures = report["micro_tests"].get("status") == "FAIL"
    if args.require_onnx and report["onnx_checkpoint"].get("status") != "PASS":
        failures = True
    report["status"] = "FAIL" if failures else "PASS"
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
