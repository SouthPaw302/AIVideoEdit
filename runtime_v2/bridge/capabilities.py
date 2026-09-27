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
    Capability(
        name="cli.run",
        status="ready",
        description="Execute registered, allowlisted tools in isolated job workspaces.",
    ),
    Capability(name="boot.capsule", status="ready", description="Portable deterministic production-state capsule and session attestation."),
    Capability(name="gate.evaluate", status="ready", description="Fail-closed branch, stage, canon, scope and attestation gate."),
    Capability(name="model.registry", status="ready", description="Provider-neutral intelligence registry with deterministic fallback."),
    Capability(name="model.music_beat", status="ready", description="CPU music/beat evidence worker with optional ONNX and existing-DSP fallback."),
    Capability(name="jev.decide", status="ready", description="Bounded deterministic PASS/FAIL/RETRY/CONTINUE/ESCALATE decision hook."),
    Capability(name="harness.optional", status="ready", description="Optional provider-neutral specialist-agent request seam."),
)

PLANNED_CAPABILITIES: tuple[Capability, ...] = (
    Capability(
        name="repo.read",
        status="planned",
        description="Read-only repository inspection through an allowlisted adapter.",
    ),
)


def list_capabilities(*, include_planned: bool = True) -> list[Capability]:
    capabilities = list(READY_CAPABILITIES)
    if include_planned:
        capabilities.extend(PLANNED_CAPABILITIES)
    return capabilities
