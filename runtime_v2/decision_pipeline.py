from __future__ import annotations

from pathlib import Path
from typing import Any

from runtime_v2.gatekeeper import evaluate_action
from runtime_v2.harness.adapter import specialist_request
from runtime_v2.jev.decision import decide as jev_decide


def decide_action(
    *,
    repo: Path,
    action: str,
    mutation: bool,
    checks: dict[str, bool | None] | None = None,
    observations: dict[str, Any] | None = None,
    requested_changes: list[str] | None = None,
    expected_stage: str | None = None,
    target_branch: str | None = None,
    protected_canon_replacement: bool = False,
    next_action_permitted: bool = False,
) -> dict[str, Any]:
    gate = evaluate_action(
        repo=repo,
        action=action,
        mutation=mutation,
        requested_changes=requested_changes or [],
        expected_stage=expected_stage,
        target_branch=target_branch,
        protected_canon_replacement=protected_canon_replacement,
    )
    evidence = {
        "gate": gate.decision,
        "checks": checks or {},
        "observations": observations or {},
        "next_action_permitted": bool(next_action_permitted),
        "ambiguous": any(value is None for value in (checks or {}).values()),
    }
    jev = jev_decide(evidence)
    result: dict[str, Any] = {
        "schema": "aivideoedit.bounded-decision.v1",
        "action": action,
        "gatekeeper": gate.as_dict(),
        "evidence": evidence,
        "jev": jev,
        "specialist": None,
    }
    if jev["decision"] == "ESCALATE":
        result["specialist"] = specialist_request(
            task=f"Resolve ambiguous bounded decision for AIVideoEdit action: {action}",
            context={
                "gatekeeper": gate.as_dict(),
                "checks": checks or {},
                "observations": observations or {},
            },
            workspace=repo,
        )
    return result
