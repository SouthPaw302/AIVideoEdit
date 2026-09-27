"""Environment-backed configuration for the Runtime V2 bridge."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class BridgeSettings:
    service_name: str = "aivideoedit-agent-bridge"
    service_version: str = "0.1.0"
    api_version: str = "v1"
    request_timeout_seconds: float = 30.0
    bearer_token: str | None = None
    audit_log_path: str | None = None

    @classmethod
    def from_env(cls) -> "BridgeSettings":
        timeout_raw = os.getenv("BRIDGE_REQUEST_TIMEOUT_SECONDS", "30")
        try:
            timeout = float(timeout_raw)
        except ValueError as exc:
            raise ValueError("BRIDGE_REQUEST_TIMEOUT_SECONDS must be numeric") from exc

        if timeout <= 0:
            raise ValueError("BRIDGE_REQUEST_TIMEOUT_SECONDS must be greater than zero")

        token = os.getenv("BRIDGE_TOKEN") or None
        audit_path = os.getenv("BRIDGE_AUDIT_LOG") or None

        return cls(
            request_timeout_seconds=timeout,
            bearer_token=token,
            audit_log_path=audit_path,
        )
