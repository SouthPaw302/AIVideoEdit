"""Environment-backed configuration for the Runtime V2 bridge."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import tempfile


@dataclass(frozen=True)
class BridgeSettings:
    service_name: str = "aivideoedit-agent-bridge"
    service_version: str = "0.2.0"
    api_version: str = "v1"
    request_timeout_seconds: float = 30.0
    execution_timeout_seconds: float = 20.0
    max_output_bytes: int = 262_144
    bearer_token: str | None = None
    audit_log_path: str | None = None
    workspace_root: str = str(
        Path(tempfile.gettempdir()) / "aivideoedit-runtime-v2" / "jobs"
    )
    keep_workspaces: bool = False

    @classmethod
    def from_env(cls) -> "BridgeSettings":
        request_timeout = _positive_float(
            "BRIDGE_REQUEST_TIMEOUT_SECONDS",
            os.getenv("BRIDGE_REQUEST_TIMEOUT_SECONDS", "30"),
        )
        execution_timeout = _positive_float(
            "BRIDGE_EXECUTION_TIMEOUT_SECONDS",
            os.getenv("BRIDGE_EXECUTION_TIMEOUT_SECONDS", "20"),
        )
        max_output = _positive_int(
            "BRIDGE_MAX_OUTPUT_BYTES",
            os.getenv("BRIDGE_MAX_OUTPUT_BYTES", "262144"),
        )

        token = os.getenv("BRIDGE_TOKEN") or None
        audit_path = os.getenv("BRIDGE_AUDIT_LOG") or None
        workspace_root = os.getenv("BRIDGE_WORKSPACE_ROOT") or cls.workspace_root
        keep_workspaces = _truthy(os.getenv("BRIDGE_KEEP_WORKSPACES", "0"))

        return cls(
            request_timeout_seconds=request_timeout,
            execution_timeout_seconds=execution_timeout,
            max_output_bytes=max_output,
            bearer_token=token,
            audit_log_path=audit_path,
            workspace_root=workspace_root,
            keep_workspaces=keep_workspaces,
        )


def _positive_float(name: str, raw: str) -> float:
    try:
        value = float(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be numeric") from exc
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return value


def _positive_int(name: str, raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")
    return value


def _truthy(raw: str) -> bool:
    return raw.strip().lower() in {"1", "true", "yes", "on"}
