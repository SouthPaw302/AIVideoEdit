"""Capability registry.

Only capabilities actually implemented in Runtime V2 should be marked ready.
"""

from __future__ import annotations

from .schemas import Capability


READY_CAPABILITIES: tuple[Capability, ...] = (
    Capability(
        name="bridge.health",
        status="ready",
        description="Liveness and service identity check.",
    ),
    Capability(
        name="bridge.version",
        status="ready",
        description="Runtime and API version discovery.",
    ),
    Capability(
        name="bridge.capabilities",
        status="ready",
        description="Machine-readable capability discovery.",
    ),
)

PLANNED_CAPABILITIES: tuple[Capability, ...] = (
    Capability(
        name="repo.read",
        status="planned",
        description="Read-only repository inspection through an allowlisted adapter.",
    ),
    Capability(
        name="cli.run",
        status="planned",
        description="Allowlisted command execution in isolated workspaces.",
    ),
    Capability(
        name="jev.evaluate",
        status="planned",
        description="Deterministic workflow and policy evaluation.",
    ),
    Capability(
        name="model.run",
        status="planned",
        description="Specialist ONNX/model execution through registered capabilities.",
    ),
)


def list_capabilities(*, include_planned: bool = True) -> list[Capability]:
    capabilities = list(READY_CAPABILITIES)
    if include_planned:
        capabilities.extend(PLANNED_CAPABILITIES)
    return capabilities
