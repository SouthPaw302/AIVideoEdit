from __future__ import annotations

import math
import wave
from array import array
from pathlib import Path

import numpy as np

from runtime_v2.models.music_beat import (
    BEAT_THIS_N_MELS,
    BEAT_THIS_SAMPLE_RATE,
    beat_this_mel,
    infer_beat_this_spectrogram,
    postprocess_beat_this,
)
from runtime_v2.models.registry import git_blob_sha1


def _click_samples(seconds: float = 3.0, bpm: float = 120.0):
    total = int(seconds * BEAT_THIS_SAMPLE_RATE)
    data = [0.0] * total
    period = int(BEAT_THIS_SAMPLE_RATE * 60.0 / bpm)
    width = int(0.02 * BEAT_THIS_SAMPLE_RATE)
    for start in range(0, total, period):
        for i in range(start, min(total, start + width)):
            t = (i - start) / BEAT_THIS_SAMPLE_RATE
            data[i] = math.sin(2 * math.pi * 1000 * t) * (1 - t / 0.02)
    return data


class FakeBeatThisSession:
    def run(self, outputs, feeds):
        assert outputs == ["beat", "downbeat"]
        x = feeds["input_spectrogram"]
        assert x.ndim == 3 and x.shape[0] == 1 and x.shape[2] == BEAT_THIS_N_MELS
        frames = x.shape[1]
        beat = np.full((1, frames), -1.0, dtype=np.float32)
        down = np.full((1, frames), -1.0, dtype=np.float32)
        for i in range(25, frames, 25):
            beat[0, i] = 2.0
        for i in range(100, frames, 100):
            down[0, i] = 3.0
        return [beat, down]


def test_beat_this_preprocess_and_named_io():
    spect = beat_this_mel(_click_samples())
    assert spect.ndim == 2
    assert spect.shape[1] == 128
    beat_logits, downbeat_logits = infer_beat_this_spectrogram(spect, FakeBeatThisSession())
    beats, downbeats = postprocess_beat_this(beat_logits, downbeat_logits)
    assert len(beats) >= 4
    assert set(downbeats).issubset(set(beats))


def test_git_blob_identity(tmp_path: Path):
    path = tmp_path / "x.bin"
    path.write_bytes(b"abc")
    assert git_blob_sha1(path) == "f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f"
