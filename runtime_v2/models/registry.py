from __future__ import annotations

import hashlib
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
    model_path: str | None = None


def git_blob_sha1(path: Path) -> str:
    size = path.stat().st_size
    digest = hashlib.sha1()
    digest.update(f"blob {size}\\0".encode("utf-8"))
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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

    def model_path(self, record: dict[str, Any]) -> Path | None:
        env_name = record.get("path_env")
        if env_name:
            explicit = os.environ.get(str(env_name))
            if explicit:
                return Path(explicit).expanduser().resolve()
        cache_relpath = record.get("cache_relpath")
        repo_root = os.environ.get("AIVIDEOEDIT_REPO_ROOT")
        if cache_relpath and repo_root:
            return (Path(repo_root).expanduser().resolve() / str(cache_relpath)).resolve()
        return None

    def verify_model_file(self, record: dict[str, Any], path: Path) -> tuple[bool, str]:
        if not path.is_file():
            return False, "model file does not exist"
        expected_size = record.get("source_size_bytes")
        if expected_size is not None and path.stat().st_size != int(expected_size):
            return False, f"model size mismatch: expected {expected_size}, got {path.stat().st_size}"
        expected_blob = str(record.get("source_git_blob_sha1") or "")
        if expected_blob:
            actual_blob = git_blob_sha1(path)
            if actual_blob != expected_blob:
                return False, f"model Git blob mismatch: expected {expected_blob}, got {actual_blob}"
        return True, "model file matches pinned source identity"

    def available(self, record: dict[str, Any]) -> tuple[bool, str, Path | None]:
        runtime = record.get("runtime")
        if runtime == "builtin_python":
            return True, "builtin runtime available", None
        if runtime == "repo_python":
            repo_root = os.environ.get("AIVIDEOEDIT_REPO_ROOT")
            if not repo_root:
                return False, "AIVIDEOEDIT_REPO_ROOT is not configured", None
            source = Path(repo_root) / str(record.get("source") or "")
            if not source.is_file():
                return False, "repository analysis module is missing", None
            missing = [
                m
                for m in ("librosa", "numpy", "soundfile")
                if importlib.util.find_spec(m) is None
            ]
            if missing:
                return False, "repository DSP dependencies unavailable: " + ", ".join(missing), None
            if shutil.which("ffmpeg") is None:
                return False, "ffmpeg unavailable for repository DSP", None
            return True, "existing AIVideoEdit audio_map runtime available", None
        if runtime == "onnxruntime":
            if importlib.util.find_spec("onnxruntime") is None:
                return False, "onnxruntime package unavailable", None
            if importlib.util.find_spec("numpy") is None:
                return False, "numpy package unavailable", None
            model_path = self.model_path(record)
            if model_path is None:
                return False, "approved model is not provisioned and no model path is configured", None
            ok, reason = self.verify_model_file(record, model_path)
            return ok, reason, model_path
        return False, f"unsupported runtime: {runtime}", None

    def resolve(self, model_id: str) -> ModelResolution:
        self.require(model_id)
        current = model_id
        trail: list[str] = []
        for _ in range(8):
            record = self.require(current)
            ok, reason, model_path = self.available(record)
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
                    str(model_path) if model_path else None,
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
                    str(model_path) if model_path else None,
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
