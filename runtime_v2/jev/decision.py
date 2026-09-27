from __future__ import annotations

from typing import Any

ALLOWED = {"PASS", "FAIL", "RETRY", "CONTINUE", "ESCALATE"}


def decide(evidence: dict[str, Any]) -> dict[str, Any]:
    gate = str(evidence.get("gate") or "").upper()
    if gate not in {"PASS", "DENY"}:
        return _result("ESCALATE", "missing or ambiguous gatekeeper evidence")
    if gate == "DENY":
        return _result("FAIL", "runtime gatekeeper denied the action")

    checks = (
        evidence.get("checks")
        if isinstance(evidence.get("checks"), dict)
        else {}
    )
    failed = sorted(k for k, v in checks.items() if v is False)
    unknown = sorted(k for k, v in checks.items() if v is None)
    if failed:
        return _result("FAIL", "required checks failed: " + ", ".join(failed))
    if evidence.get("retryable_error") is True:
        return _result("RETRY", "bounded retryable error reported")
    if evidence.get("ambiguous") is True or unknown:
        return _result(
            "ESCALATE",
            "ambiguous evidence requires authorized-agent review",
        )
    if evidence.get("next_action_permitted") is True:
        return _result(
            "CONTINUE",
            "all declared evidence passes and next action is permitted",
        )
    return _result("PASS", "all declared checks pass")


def _result(decision: str, reason: str) -> dict[str, Any]:
    if decision not in ALLOWED:
        raise ValueError("invalid Jev decision")
    return {
        "schema": "aivideoedit.jev-decision.v1",
        "decision": decision,
        "reason": reason,
    }
