from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable


@dataclass(frozen=True)
class HarnessStatus:
    enabled: bool
    launcher: str | None
    mcp_bridge: str
    production_authority: str = "aivideoedit"
    profile: str = "headless"
    allow_npx: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "enabled": self.enabled,
            "launcher": self.launcher,
            "mcp_bridge": self.mcp_bridge,
            "production_authority": self.production_authority,
            "provider_neutral": True,
            "profile": self.profile,
            "allow_npx": self.allow_npx,
        }


def _truthy(name: str, default: str = "0") -> bool:
    return os.environ.get(name, default).strip().lower() in {"1", "true", "yes", "on"}


def status(enabled: bool | None = None) -> HarnessStatus:
    if enabled is None:
        enabled = _truthy("AIVIDEOEDIT_HARNESS_ENABLED")
    dsh = shutil.which("dsh")
    npx = shutil.which("npx")
    allow_npx = _truthy("AIVIDEOEDIT_HARNESS_ALLOW_NPX")
    launcher = dsh or (npx if allow_npx else None)
    profile = os.environ.get("AIVIDEOEDIT_HARNESS_PROFILE", "headless").strip() or "headless"
    return HarnessStatus(
        enabled=bool(enabled and launcher),
        launcher=launcher,
        mcp_bridge="prototype/backend_gui/aivideo_mcp.py",
        profile=profile,
        allow_npx=allow_npx,
    )


def _command(current: HarnessStatus, prompt: str) -> list[str]:
    if not current.launcher:
        raise RuntimeError("DeepSeek Harness launcher is unavailable")
    if Path(current.launcher).name.lower().startswith("npx"):
        return [
            current.launcher,
            "-y",
            "@deepseek-ai/dsh",
            "--profile",
            current.profile,
            prompt,
        ]
    return [
        current.launcher,
        "--profile",
        current.profile,
        prompt,
    ]


def launch_specialist(
    *,
    task: str,
    context: dict[str, Any],
    workspace: Path | None = None,
    timeout_seconds: int = 180,
) -> dict[str, Any]:
    current = status()
    if not current.enabled:
        return {
            "status": "ESCALATE",
            "reason": "Harness is disabled or no approved launcher is available.",
            "harness": current.as_dict(),
            "result": None,
        }
    envelope = {
        "schema": "aivideoedit.specialist-request.v1",
        "task": task,
        "context": context,
        "authority": "advisory_only",
        "rules": [
            "AIVideoEdit remains production authority.",
            "Use the configured AIVideoEdit MCP tools for project facts.",
            "Do not bypass Runtime Gatekeeper.",
            "Return bounded evidence/recommendation to the authorized primary agent.",
        ],
    }
    prompt = (
        "You are an AIVideoEdit specialist sub-agent. Analyze the following request. "
        "Do not claim production authority. Return a concise structured result.\n"
        + json.dumps(envelope, sort_keys=True)
    )
    try:
        proc = subprocess.run(
            _command(current, prompt),
            cwd=str((workspace or Path.cwd()).resolve()),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=max(10, min(int(timeout_seconds), 900)),
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "status": "RETRY",
            "reason": "Harness specialist timed out.",
            "harness": current.as_dict(),
            "stdout": (exc.stdout or "")[-4000:] if isinstance(exc.stdout, str) else "",
            "stderr": (exc.stderr or "")[-4000:] if isinstance(exc.stderr, str) else "",
            "result": None,
        }
    return {
        "status": "PASS" if proc.returncode == 0 else "RETRY",
        "reason": "Harness specialist completed." if proc.returncode == 0 else "Harness specialist exited nonzero.",
        "harness": current.as_dict(),
        "returncode": proc.returncode,
        "stdout": (proc.stdout or "")[-12000:],
        "stderr": (proc.stderr or "")[-4000:],
        "result": (proc.stdout or "").strip() or None,
    }


def specialist_request(
    *,
    task: str,
    context: dict[str, Any],
    provider: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    workspace: Path | None = None,
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
    if provider is not None:
        result = provider(envelope)
        return {"status": "PASS", "request": envelope, "result": result}
    launched = launch_specialist(
        task=task,
        context=context,
        workspace=workspace,
    )
    launched["request"] = envelope
    return launched
