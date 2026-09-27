from __future__ import annotations

import importlib.util
import math
import os
import wave
from array import array
from pathlib import Path
from typing import Any

from .registry import ModelRegistry


def _read_wav_mono(path: Path) -> tuple[list[float], int]:
    with wave.open(str(path), "rb") as wf:
        channels = wf.getnchannels()
        width = wf.getsampwidth()
        rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
    if width != 2:
        raise ValueError("music beat micro-worker currently expects 16-bit PCM WAV")
    samples = array("h")
    samples.frombytes(frames)
    if channels == 1:
        mono = [float(x) / 32768.0 for x in samples]
    else:
        mono = []
        for i in range(0, len(samples), channels):
            frame = samples[i:i + channels]
            mono.append(sum(frame) / (32768.0 * len(frame)))
    return mono, rate


def _energy_envelope(
    samples: list[float],
    rate: int,
    hop_seconds: float = 0.01,
) -> tuple[list[float], float]:
    hop = max(1, int(rate * hop_seconds))
    env = []
    for start in range(0, len(samples), hop):
        chunk = samples[start:start + hop]
        if chunk:
            env.append(math.sqrt(sum(x * x for x in chunk) / len(chunk)))
    return env, hop / rate


def _onsets(env: list[float], hop_seconds: float) -> list[float]:
    if not env:
        return []
    avg = sum(env) / len(env)
    peak = max(env)
    threshold = avg + 0.35 * max(0.0, peak - avg)
    minimum_hops = max(1, int(0.18 / hop_seconds))
    hits: list[int] = []
    last = -minimum_hops
    for i in range(1, len(env) - 1):
        if (
            env[i] >= threshold
            and env[i] >= env[i - 1]
            and env[i] > env[i + 1]
            and i - last >= minimum_hops
        ):
            hits.append(i)
            last = i
    return [round(i * hop_seconds, 4) for i in hits]


def _bpm_from_onsets(onsets: list[float]) -> float | None:
    intervals = [
        b - a
        for a, b in zip(onsets, onsets[1:])
        if 0.25 <= b - a <= 2.0
    ]
    if not intervals:
        return None
    intervals.sort()
    median = intervals[len(intervals) // 2]
    bpm = 60.0 / median
    while bpm < 60:
        bpm *= 2
    while bpm > 200:
        bpm /= 2
    return round(bpm, 2)


def analyze_dsp(path: Path) -> dict[str, Any]:
    samples, rate = _read_wav_mono(path)
    env, hop_seconds = _energy_envelope(samples, rate)
    beats = _onsets(env, hop_seconds)
    bpm = _bpm_from_onsets(beats)
    return {
        "schema": "aivideoedit.music-analysis-evidence.v1",
        "engine": "deterministic_dsp",
        "sample_rate": rate,
        "bpm": bpm,
        "beat_positions_seconds": beats,
        "confidence": 0.75 if bpm is not None and len(beats) >= 4 else 0.35,
        "authority": "evidence_only",
    }


def analyze_onnx(path: Path, model_path: Path) -> dict[str, Any]:
    import numpy as np
    import onnxruntime as ort

    samples, rate = _read_wav_mono(path)
    session = ort.InferenceSession(
        str(model_path),
        providers=["CPUExecutionProvider"],
    )
    input_meta = session.get_inputs()[0]
    waveform = np.asarray(samples, dtype=np.float32)[None, :]
    output = session.run(None, {input_meta.name: waveform})[0]
    activation = np.asarray(output).reshape(-1)
    if activation.size == 0:
        raise RuntimeError("ONNX beat model returned an empty activation")
    threshold = float(activation.mean() + 0.5 * activation.std())
    candidate = [
        i
        for i in range(1, len(activation) - 1)
        if activation[i] >= threshold
        and activation[i] >= activation[i - 1]
        and activation[i] > activation[i + 1]
    ]
    duration = len(samples) / rate
    hop = duration / max(1, len(activation))
    beats = [round(i * hop, 4) for i in candidate]
    bpm = _bpm_from_onsets(beats)
    return {
        "schema": "aivideoedit.music-analysis-evidence.v1",
        "engine": "onnxruntime",
        "model": str(model_path),
        "sample_rate": rate,
        "bpm": bpm,
        "beat_positions_seconds": beats,
        "confidence": 0.85 if bpm is not None and len(beats) >= 4 else 0.5,
        "authority": "evidence_only",
    }


def analyze_repo_dsp(path: Path, source: str) -> dict[str, Any]:
    repo_root = Path(os.environ["AIVIDEOEDIT_REPO_ROOT"]).resolve()
    module_path = (repo_root / source).resolve()
    spec = importlib.util.spec_from_file_location(
        "aivideoedit_audio_map",
        module_path,
    )
    if not spec or not spec.loader:
        raise RuntimeError("cannot load existing AIVideoEdit audio_map")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    doc = module.analyze(path)
    rhythm = doc.get("rhythm", {})
    return {
        "schema": "aivideoedit.music-analysis-evidence.v1",
        "engine": "existing_aivideoedit_audio_map",
        "sample_rate": doc.get("audio", {}).get("analysis_sample_rate"),
        "bpm": rhythm.get("bpm"),
        "beat_positions_seconds": rhythm.get("beats_sec", []),
        "downbeat_positions_seconds": rhythm.get("downbeats_sec", []),
        "confidence": 0.9 if rhythm.get("bpm") else 0.5,
        "authority": "evidence_only",
        "canonical_audiomap": doc,
    }


def analyze_music(
    path: str | Path,
    registry: ModelRegistry | None = None,
) -> dict[str, Any]:
    path = Path(path)
    registry = registry or ModelRegistry.load_default()
    resolution = registry.resolve_capability("music_and_beat_analysis")
    if not resolution.available:
        raise RuntimeError(resolution.reason)
    runtime = resolution.record.get("runtime")
    if runtime == "onnxruntime":
        model_path = Path(
            os.environ[str(resolution.record["path_env"])]
        ).expanduser()
        evidence = analyze_onnx(path, model_path)
    elif runtime == "repo_python":
        evidence = analyze_repo_dsp(path, str(resolution.record["source"]))
    else:
        evidence = analyze_dsp(path)
    evidence["model_resolution"] = {
        "requested": resolution.requested,
        "resolved": resolution.resolved,
        "used_fallback": resolution.used_fallback,
        "reason": resolution.reason,
    }
    return evidence
