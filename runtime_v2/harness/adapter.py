from __future__ import annotations

import shutil
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class HarnessStatus:
    enabled: bool
    launcher: str | None
    mcp_bridge: str
    production_authority: str = "aivideoedit"

    def as_dict(self) -> dict[str, Any]:
        return {
            "enabled": self.enabled,
            "launcher": self.launcher,
            "mcp_bridge": self.mcp_bridge,
            "production_authority": self.production_authority,
            "provider_neutral": True,
        }


def status(enabled: bool = False) -> HarnessStatus:
    launcher = shutil.which("dsh") or shutil.which("npx")
    return HarnessStatus(
        enabled=bool(enabled and launcher),
        launcher=launcher,
        mcp_bridge="prototype/backend_gui/aivideo_mcp.py",
    )


def specialist_request(
    *,
    task: str,
    context: dict[str, Any],
    provider: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    envelope = {
        "schema": "aivideoedit.specialist-request.v1",
        "task": task,
        "context": context,
        "authority": "advisory_only",
        "rules": [
            "AIVideoEdit remains production authority.",
            "Specialist output cannot bypass Runtime Gatekeeper.",
            "Provider/model identity is optional and interchangeable.",
        ],
    }
    if provider is None:
        return {
            "status": "ESCALATE",
            "request": envelope,
            "result": None,
        }
    result = provider(envelope)
    return {
        "status": "PASS",
        "request": envelope,
        "result": result,
    }
