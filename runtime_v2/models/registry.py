from __future__ import annotations

import importlib.util
import json
import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ModelResolution:
    requested: str
    resolved: str
    available: bool
    used_fallback: bool
    reason: str
    record: dict[str, Any]


class ModelRegistry:
    def __init__(self, data: dict[str, Any]):
        self.data = data
        self.models = {
            str(x.get("id")): x
            for x in data.get("models", [])
            if isinstance(x, dict) and x.get("id")
        }

    @classmethod
    def load_default(cls) -> "ModelRegistry":
        path = Path(__file__).with_name("registry.json")
        return cls(json.loads(path.read_text(encoding="utf-8")))

    def require(self, model_id: str) -> dict[str, Any]:
        if model_id not in self.models:
            raise KeyError(f"unknown or unapproved model identifier: {model_id}")
        return self.models[model_id]

    def available(self, record: dict[str, Any]) -> tuple[bool, str]:
        runtime = record.get("runtime")
        if runtime == "builtin_python":
            return True, "builtin runtime available"
        if runtime == "repo_python":
            repo_root = os.environ.get("AIVIDEOEDIT_REPO_ROOT")
            if not repo_root:
                return False, "AIVIDEOEDIT_REPO_ROOT is not configured"
            source = Path(repo_root) / str(record.get("source") or "")
            if not source.is_file():
                return False, "repository analysis module is missing"
            missing = [
                m
                for m in ("librosa", "numpy", "soundfile")
                if importlib.util.find_spec(m) is None
            ]
            if missing:
                return False, "repository DSP dependencies unavailable: " + ", ".join(missing)
            if shutil.which("ffmpeg") is None:
                return False, "ffmpeg unavailable for repository DSP"
            return True, "existing AIVideoEdit audio_map runtime available"
        if runtime == "onnxruntime":
            if importlib.util.find_spec("onnxruntime") is None:
                return False, "onnxruntime package unavailable"
            env_name = record.get("path_env")
            model_path = os.environ.get(str(env_name or "")) if env_name else None
            if not model_path:
                return False, f"{env_name} is not configured"
            if not Path(model_path).expanduser().is_file():
                return False, "configured ONNX model file does not exist"
            return True, "onnxruntime and model file available"
        return False, f"unsupported runtime: {runtime}"

    def resolve(self, model_id: str) -> ModelResolution:
        self.require(model_id)
        current = model_id
        trail: list[str] = []
        for _ in range(8):
            record = self.require(current)
            ok, reason = self.available(record)
            if ok:
                prefix = "; ".join(trail)
                final_reason = (prefix + "; " if prefix else "") + reason
                return ModelResolution(
                    model_id,
                    current,
                    True,
                    current != model_id,
                    final_reason,
                    record,
                )
            trail.append(f"{current} unavailable ({reason})")
            fallback = record.get("fallback")
            if not fallback:
                return ModelResolution(
                    model_id,
                    current,
                    False,
                    current != model_id,
                    "; ".join(trail),
                    record,
                )
            current = str(fallback)
        raise RuntimeError("model fallback chain exceeded safety limit")

    def resolve_capability(self, capability: str) -> ModelResolution:
        candidates = [
            r
            for r in self.models.values()
            if r.get("capability") == capability
        ]
        if not candidates:
            raise KeyError(f"no approved model for capability: {capability}")
        onnx = next(
            (r for r in candidates if r.get("runtime") == "onnxruntime"),
            candidates[0],
        )
        return self.resolve(str(onnx["id"]))
