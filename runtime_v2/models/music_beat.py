from __future__ import annotations

import importlib.util
import math
import os
import shutil
import subprocess
import tempfile
import wave
from array import array
from pathlib import Path
from typing import Any

from .registry import ModelRegistry, inferred_repo_root

BEAT_THIS_SAMPLE_RATE = 22050
BEAT_THIS_N_FFT = 1024
BEAT_THIS_HOP = 441
BEAT_THIS_N_MELS = 128
BEAT_THIS_F_MIN = 30.0
BEAT_THIS_F_MAX = 11000.0
BEAT_THIS_CHUNK = 1500
BEAT_THIS_BORDER = 6
BEAT_THIS_FPS = BEAT_THIS_SAMPLE_RATE / BEAT_THIS_HOP


def _read_wav_mono(path: Path) -> tuple[list[float], int]:
    with wave.open(str(path), "rb") as wf:
        channels = wf.getnchannels()
        width = wf.getsampwidth()
        rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
    if width != 2:
        raise ValueError("music worker expects 16-bit PCM WAV after decoding")
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


def _decode_for_beat_this(path: Path) -> tuple[list[float], int]:
    try:
        samples, rate = _read_wav_mono(path)
        if rate == BEAT_THIS_SAMPLE_RATE:
            return samples, rate
    except (wave.Error, ValueError, EOFError):
        pass

    if shutil.which("ffmpeg") is None:
        raise RuntimeError("Beat This preprocessing requires ffmpeg for decode/resample")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = Path(tmp.name)
    try:
        p = subprocess.run(
            [
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-i", str(path), "-vn", "-ac", "1", "-ar", str(BEAT_THIS_SAMPLE_RATE),
                "-c:a", "pcm_s16le", str(wav_path),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if p.returncode != 0:
            raise RuntimeError("ffmpeg decode/resample failed: " + p.stderr.strip())
        return _read_wav_mono(wav_path)
    finally:
        wav_path.unlink(missing_ok=True)


def _hz_to_mel_slaney(hz):
    import numpy as np
    hz = np.asarray(hz, dtype=np.float64)
    f_sp = 200.0 / 3.0
    mels = hz / f_sp
    min_log_hz = 1000.0
    min_log_mel = min_log_hz / f_sp
    logstep = np.log(6.4) / 27.0
    return np.where(
        hz >= min_log_hz,
        min_log_mel + np.log(np.maximum(hz, 1e-12) / min_log_hz) / logstep,
        mels,
    )


def _mel_to_hz_slaney(mel):
    import numpy as np
    mel = np.asarray(mel, dtype=np.float64)
    f_sp = 200.0 / 3.0
    hz = f_sp * mel
    min_log_hz = 1000.0
    min_log_mel = min_log_hz / f_sp
    logstep = np.log(6.4) / 27.0
    return np.where(
        mel >= min_log_mel,
        min_log_hz * np.exp(logstep * (mel - min_log_mel)),
        hz,
    )


def _beat_this_filterbank():
    import numpy as np
    mel_min = float(_hz_to_mel_slaney(BEAT_THIS_F_MIN))
    mel_max = float(_hz_to_mel_slaney(BEAT_THIS_F_MAX))
    mel_points = np.linspace(mel_min, mel_max, BEAT_THIS_N_MELS + 2)
    hz_points = _mel_to_hz_slaney(mel_points)
    freqs = np.arange(BEAT_THIS_N_FFT // 2 + 1, dtype=np.float64) * (
        BEAT_THIS_SAMPLE_RATE / BEAT_THIS_N_FFT
    )
    left = hz_points[:-2]
    center = hz_points[1:-1]
    right = hz_points[2:]
    up = (freqs[:, None] - left[None, :]) / np.maximum(center - left, 1e-12)[None, :]
    down = (right[None, :] - freqs[:, None]) / np.maximum(right - center, 1e-12)[None, :]
    return np.maximum(0.0, np.minimum(up, down)).astype(np.float32)


def beat_this_mel(samples: list[float]):
    import numpy as np
    audio = np.asarray(samples, dtype=np.float32)
    if audio.size < 2:
        raise ValueError("audio is too short for Beat This preprocessing")
    pad = BEAT_THIS_N_FFT // 2
    padded = np.pad(audio, (pad, pad), mode="reflect")
    frame_count = 1 + (len(padded) - BEAT_THIS_N_FFT) // BEAT_THIS_HOP
    if frame_count <= 0:
        raise ValueError("audio produced no Beat This spectrogram frames")
    window = (
        0.5
        * (
            1.0
            - np.cos(
                2.0
                * np.pi
                * np.arange(BEAT_THIS_N_FFT, dtype=np.float32)
                / BEAT_THIS_N_FFT
            )
        )
    ).astype(np.float32)
    frames = np.empty((frame_count, BEAT_THIS_N_FFT), dtype=np.float32)
    for i in range(frame_count):
        start = i * BEAT_THIS_HOP
        frames[i] = padded[start:start + BEAT_THIS_N_FFT] * window
    spectrum = np.abs(np.fft.rfft(frames, axis=1)).astype(np.float32) / math.sqrt(BEAT_THIS_N_FFT)
    mel_energy = spectrum @ _beat_this_filterbank()
    return np.log1p(1000.0 * np.maximum(mel_energy, 1e-10)).astype(np.float32)


def _chunk_starts(length: int) -> list[int]:
    starts = list(range(-BEAT_THIS_BORDER, length - BEAT_THIS_BORDER, BEAT_THIS_CHUNK - 2 * BEAT_THIS_BORDER))
    if not starts:
        starts = [-BEAT_THIS_BORDER]
    if length > BEAT_THIS_CHUNK - 2 * BEAT_THIS_BORDER:
        starts[-1] = length - (BEAT_THIS_CHUNK - BEAT_THIS_BORDER)
    return starts


def _split_spectrogram(spect):
    import numpy as np
    chunks = []
    starts = _chunk_starts(len(spect))
    for start in starts:
        actual_start = max(0, start)
        actual_end = min(start + BEAT_THIS_CHUNK, len(spect))
        current = spect[actual_start:actual_end]
        left_pad = max(0, -start)
        right_pad = max(0, min(BEAT_THIS_BORDER, start + BEAT_THIS_CHUNK - len(spect)))
        if left_pad or right_pad:
            current = np.pad(current, ((left_pad, right_pad), (0, 0)), mode="constant")
        chunks.append(current.astype(np.float32, copy=False))
    return starts, chunks


def infer_beat_this_spectrogram(spect, session):
    import numpy as np
    starts, chunks = _split_spectrogram(spect)
    predictions = []
    for chunk in chunks:
        outputs = session.run(
            ["beat", "downbeat"],
            {"input_spectrogram": chunk[None, :, :].astype(np.float32, copy=False)},
        )
        beat = np.asarray(outputs[0]).reshape(-1).astype(np.float32)
        downbeat = np.asarray(outputs[1]).reshape(-1).astype(np.float32)
        predictions.append((beat, downbeat))

    beat_full = np.full(len(spect), -1000.0, dtype=np.float32)
    downbeat_full = np.full(len(spect), -1000.0, dtype=np.float32)
    for idx in range(len(predictions) - 1, -1, -1):
        beat_chunk, downbeat_chunk = predictions[idx]
        start = starts[idx]
        if len(beat_chunk) < 2 * BEAT_THIS_BORDER:
            begin, end = 0, len(beat_chunk)
        else:
            begin, end = BEAT_THIS_BORDER, len(beat_chunk) - BEAT_THIS_BORDER
        for j in range(begin, end):
            target = start + j
            if 0 <= target < len(spect):
                beat_full[target] = beat_chunk[j]
                downbeat_full[target] = downbeat_chunk[j]
    return beat_full, downbeat_full


def _deduplicate_peaks(peaks: list[int], width: int = 1) -> list[int]:
    if not peaks:
        return []
    result = []
    p = float(peaks[0])
    count = 1
    for p2 in peaks[1:]:
        if p2 - p <= width:
            count += 1
            p += (p2 - p) / count
        else:
            result.append(int(math.floor(p + 0.5)))
            p = float(p2)
            count = 1
    result.append(int(math.floor(p + 0.5)))
    return result


def _peak_frames(logits) -> list[int]:
    values = list(float(x) for x in logits)
    peaks = []
    for i, value in enumerate(values):
        left = max(0, i - 3)
        right = min(len(values), i + 4)
        if value > 0.0 and value == max(values[left:right]):
            peaks.append(i)
    return _deduplicate_peaks(peaks, 1)


def postprocess_beat_this(beat_logits, downbeat_logits) -> tuple[list[float], list[float]]:
    beat_frames = _peak_frames(beat_logits)
    downbeat_frames = _peak_frames(downbeat_logits)
    beats = [round(frame / BEAT_THIS_FPS, 4) for frame in beat_frames]
    downbeats = [round(frame / BEAT_THIS_FPS, 4) for frame in downbeat_frames]
    if beats:
        downbeats = [min(beats, key=lambda beat: abs(beat - downbeat)) for downbeat in downbeats]
        downbeats = sorted(set(downbeats))
    return beats, downbeats


def _energy_envelope(samples: list[float], rate: int, hop_seconds: float = 0.01) -> tuple[list[float], float]:
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
        if env[i] >= threshold and env[i] >= env[i - 1] and env[i] > env[i + 1] and i - last >= minimum_hops:
            hits.append(i)
            last = i
    return [round(i * hop_seconds, 4) for i in hits]


def _bpm_from_onsets(onsets: list[float]) -> float | None:
    intervals = [b - a for a, b in zip(onsets, onsets[1:]) if 0.25 <= b - a <= 2.0]
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
    try:
        samples, rate = _read_wav_mono(path)
    except (wave.Error, ValueError, EOFError):
        samples, rate = _decode_for_beat_this(path)
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


def analyze_beat_this_onnx(path: Path, model_path: Path) -> dict[str, Any]:
    import onnxruntime as ort
    samples, rate = _decode_for_beat_this(path)
    if rate != BEAT_THIS_SAMPLE_RATE:
        raise RuntimeError("Beat This decode did not produce 22050 Hz audio")
    spect = beat_this_mel(samples)
    session = ort.InferenceSession(str(model_path), providers=["CPUExecutionProvider"])
    inputs = {x.name: x for x in session.get_inputs()}
    outputs = {x.name: x for x in session.get_outputs()}
    if "input_spectrogram" not in inputs or not {"beat", "downbeat"}.issubset(outputs):
        raise RuntimeError("Beat This ONNX signature mismatch")
    shape = inputs["input_spectrogram"].shape
    if len(shape) != 3 or (isinstance(shape[-1], int) and shape[-1] != BEAT_THIS_N_MELS):
        raise RuntimeError(f"Beat This ONNX input shape mismatch: {shape}")
    beat_logits, downbeat_logits = infer_beat_this_spectrogram(spect, session)
    beats, downbeats = postprocess_beat_this(beat_logits, downbeat_logits)
    bpm = _bpm_from_onsets(beats)
    return {
        "schema": "aivideoedit.music-analysis-evidence.v1",
        "engine": "beat_this_onnx",
        "model": str(model_path),
        "sample_rate": rate,
        "frames_per_second": BEAT_THIS_FPS,
        "bpm": bpm,
        "beat_positions_seconds": beats,
        "downbeat_positions_seconds": downbeats,
        "confidence": 0.9 if bpm is not None and len(beats) >= 4 else 0.55,
        "authority": "evidence_only",
    }


def analyze_repo_dsp(path: Path, source: str) -> dict[str, Any]:
    repo_root = inferred_repo_root()
    module_path = (repo_root / source).resolve()
    spec = importlib.util.spec_from_file_location("aivideoedit_audio_map", module_path)
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


def analyze_music(path: str | Path, registry: ModelRegistry | None = None) -> dict[str, Any]:
    path = Path(path)
    registry = registry or ModelRegistry.load_default()
    resolution = registry.resolve_capability("music_and_beat_analysis")
    if not resolution.available:
        raise RuntimeError(resolution.reason)
    runtime = resolution.record.get("runtime")
    if runtime == "onnxruntime":
        if not resolution.model_path:
            raise RuntimeError("resolved ONNX model has no verified path")
        evidence = analyze_beat_this_onnx(path, Path(resolution.model_path))
    elif runtime == "repo_python":
        evidence = analyze_repo_dsp(path, str(resolution.record["source"]))
    else:
        evidence = analyze_dsp(path)
    evidence["model_resolution"] = {
        "requested": resolution.requested,
        "resolved": resolution.resolved,
        "used_fallback": resolution.used_fallback,
        "reason": resolution.reason,
        "model_path": resolution.model_path,
    }
    return evidence
