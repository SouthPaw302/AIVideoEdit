from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from runtime_v2.boot.capsule import verify_capsule


@dataclass(frozen=True)
class GateDecision:
    decision: str
    reasons: tuple[str, ...]
    refresh_required: bool = False

    def as_dict(self) -> dict[str, Any]:
        return {
            "decision": self.decision,
            "reasons": list(self.reasons),
            "refresh_required": self.refresh_required,
        }


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _branch(repo: Path) -> str:
    try:
        p = subprocess.run(
            ["git", "-C", str(repo), "branch", "--show-current"],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        return ""
    return p.stdout.strip() if p.returncode == 0 else ""


def evaluate_action(
    *,
    repo: Path,
    action: str,
    mutation: bool,
    requested_changes: list[str] | None = None,
    expected_stage: str | None = None,
    target_branch: str | None = None,
    protected_canon_replacement: bool = False,
    current_branch: str | None = None,
) -> GateDecision:
    session_dir = repo / ".aivideoedit"
    capsule = _read_json(session_dir / "boot_capsule.json")
    attestation = _read_json(session_dir / "session_attestation.json")
    if not capsule or not attestation:
        return GateDecision("DENY", ("missing boot capsule or session attestation",))
    ok, detail = verify_capsule(
        capsule,
        attestation,
        key=os.environ.get("AIVIDEOEDIT_ATTESTATION_KEY"),
    )
    if not ok:
        return GateDecision("DENY", (detail,))

    active = capsule.get("active") if isinstance(capsule.get("active"), dict) else {}
    canonical_branch = str(active.get("branch") or "")
    observed_branch = current_branch if current_branch is not None else _branch(repo)
    reasons: list[str] = []

    if observed_branch and canonical_branch and observed_branch != canonical_branch:
        reasons.append(f"branch mismatch: boot={canonical_branch} current={observed_branch}")
    if target_branch and target_branch != canonical_branch:
        reasons.append(f"target branch mismatch: boot={canonical_branch} target={target_branch}")

    stage = str(active.get("stage") or "")
    if expected_stage and stage != expected_stage:
        reasons.append(f"stage mismatch: boot={stage or 'UNKNOWN'} expected={expected_stage}")

    canon = capsule.get("canon") if isinstance(capsule.get("canon"), dict) else {}
    if mutation and protected_canon_replacement and canon.get("locked") is True:
        reasons.append("protected canon replacement denied while canon is locked")

    changes = set(requested_changes or [])
    for scope_name in ("refinement", "recut"):
        scope = canon.get(scope_name) if isinstance(canon.get(scope_name), dict) else {}
        if scope.get("active") is not True:
            continue
        allowed = set(str(x) for x in scope.get("allowed_changes", []) if x is not None)
        forbidden = set(str(x) for x in scope.get("forbidden_changes", []) if x is not None)
        bad = sorted(changes & forbidden)
        if bad:
            reasons.append(f"{scope_name} forbidden changes requested: {', '.join(bad)}")
        outside = sorted(changes - allowed) if allowed else []
        if outside:
            reasons.append(f"{scope_name} changes outside allowed scope: {', '.join(outside)}")

    if mutation and not action.strip():
        reasons.append("mutation action name is required")

    if reasons:
        return GateDecision("DENY", tuple(reasons))
    return GateDecision(
        "PASS",
        ("attestation, branch, stage, canon and scope checks passed",),
        refresh_required=mutation,
    )
