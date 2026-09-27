from __future__ import annotations

import hashlib
import json
import os
import re
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


_TAG_ALIASES: dict[str, tuple[str, ...]] = {
    "source_media": ("source media", "source", "asset", "assets", "media ingest"),
    "asset_manifest": ("asset manifest", "assets"),
    "reference_manifest": ("reference manifest", "references"),
    "analysis": ("analysis", "evidence"),
    "music": ("music", "audio", "beat", "tempo"),
    "references": ("reference", "references"),
    "lyrics": ("lyrics",),
    "genre": ("genre",),
    "visual_approach": ("visual approach", "direction", "route", "routes"),
    "storyboard": ("storyboard",),
    "script": ("script",),
    "shots": ("shot", "shots", "shot package", "shot packages"),
    "generated_media": ("generated media", "generated visual", "stills", "images"),
    "accepted_media": ("accepted media", "acceptance", "canon media"),
    "proofs": ("proof", "proofs"),
    "fx": ("fx", "effect", "effects"),
    "transitions": ("transition", "transitions"),
    "assembly": ("assembly", "assemble"),
    "final_qc": ("final qc", "qc"),
    "archive": ("archive",),
    "stage": ("stage", "advance"),
    "canon": ("canon", "picture language", "visual canon"),
    "accepted_baseline": ("accepted baseline", "baseline"),
}


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _git(repo: Path, *args: str) -> str:
    try:
        p = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        return ""
    return p.stdout.strip() if p.returncode == 0 else ""


def _branch(repo: Path) -> str:
    return _git(repo, "branch", "--show-current")


def _sha256(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _truthy_env(name: str) -> bool:
    return os.environ.get(name, "0").strip().lower() in {"1", "true", "yes", "on"}


def _normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", str(value or "").lower()))


def _tag_matches(tag: str, declared: str) -> bool:
    requested = _normalize(tag.replace("_", " "))
    candidate = _normalize(declared)
    if not requested or not candidate:
        return False
    aliases = tuple(
        _normalize(x)
        for x in _TAG_ALIASES.get(tag, (tag.replace("_", " "),))
    )
    return any(
        alias == candidate or alias in candidate or candidate in alias
        for alias in aliases
        if alias
    )


def _runtime_state_reasons(repo: Path, capsule: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    active = capsule.get("active") if isinstance(capsule.get("active"), dict) else {}

    expected_head = str(active.get("branch_commit") or "")
    current_head = _git(repo, "rev-parse", "HEAD")
    if expected_head and current_head and expected_head != current_head:
        reasons.append(f"stale session: boot HEAD={expected_head} current HEAD={current_head}")

    dirty = _git(repo, "status", "--porcelain", "--untracked-files=no")
    if dirty:
        reasons.append("tracked workspace has uncommitted changes since attestation")

    project_rel = str(active.get("project_dir") or "").strip()
    if not project_rel:
        return reasons

    project = (repo / project_rel).resolve()
    repo = repo.resolve()
    if project != repo and repo not in project.parents:
        reasons.append("attested project path escapes repository root")
        return reasons
    if not project.is_dir():
        reasons.append("attested project directory is missing")
        return reasons

    state_path = project / "PROJECT_STATE.json"
    expected_state_hash = str(active.get("project_state_sha256") or "")
    if expected_state_hash and _sha256(state_path) != expected_state_hash:
        reasons.append("PROJECT_STATE.json changed since attestation")
    state = _read_json(state_path)
    expected_stage = str(active.get("stage") or "")
    current_stage = str(state.get("stage") or "")
    if expected_stage and current_stage != expected_stage:
        reasons.append(
            f"stale stage: boot={expected_stage} current={current_stage or 'UNKNOWN'}"
        )

    expected_next = str(active.get("exact_next_action") or "").strip()
    state_next = str(state.get("exact_next_action") or "").strip()
    order_path = project / "OPERATING_ORDER.json"
    order = _read_json(order_path)
    order_next = str(order.get("exact_next_action") or "").strip()
    current_next = order_next or state_next
    if expected_next and current_next and expected_next != current_next:
        reasons.append("exact_next_action changed since attestation")

    operating = capsule.get("operating_order") if isinstance(capsule.get("operating_order"), dict) else {}
    expected_order_hash = str(operating.get("sha256") or "")
    if expected_order_hash and _sha256(order_path) != expected_order_hash:
        reasons.append("OPERATING_ORDER.json changed since attestation")

    media = capsule.get("media") if isinstance(capsule.get("media"), dict) else {}
    for filename, key in (
        ("REFERENCE_MANIFEST.json", "reference_manifest_sha256"),
        ("ASSET_MANIFEST.json", "asset_manifest_sha256"),
    ):
        expected = str(media.get(key) or "")
        if expected and _sha256(project / filename) != expected:
            reasons.append(f"{filename} changed since attestation")
    return reasons


def evaluate_action(
    *,
    repo: Path,
    action: str,
    mutation: bool,
    requested_changes: list[str] | None = None,
    expected_stage: str | None = None,
    target_branch: str | None = None,
    protected_canon_replacement: bool = False,
    canon_sensitive: bool = False,
    current_branch: str | None = None,
) -> GateDecision:
    repo = repo.resolve()
    session_dir = repo / ".aivideoedit"
    capsule = _read_json(session_dir / "boot_capsule.json")
    attestation = _read_json(session_dir / "session_attestation.json")
    if not capsule or not attestation:
        return GateDecision("DENY", ("missing boot capsule or session attestation",))

    attestation_key = os.environ.get("AIVIDEOEDIT_ATTESTATION_KEY")
    if _truthy_env("AIVIDEOEDIT_REQUIRE_SIGNED_ATTESTATION"):
        if not attestation_key:
            return GateDecision(
                "DENY",
                ("signed attestation is required but no attestation key is configured",),
            )
        if attestation.get("scheme") != "hmac-sha256":
            return GateDecision("DENY", ("signed HMAC session attestation is required",))

    ok, detail = verify_capsule(capsule, attestation, key=attestation_key)
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

    reasons.extend(_runtime_state_reasons(repo, capsule))

    stage = str(active.get("stage") or "")
    if expected_stage and stage != expected_stage:
        reasons.append(f"stage mismatch: boot={stage or 'UNKNOWN'} expected={expected_stage}")

    exact_next_tool = str(active.get("exact_next_tool") or "").strip()
    if mutation and exact_next_tool and action != exact_next_tool:
        reasons.append(f"exact-next-tool mismatch: boot={exact_next_tool} requested={action}")

    canon = capsule.get("canon") if isinstance(capsule.get("canon"), dict) else {}
    refine = canon.get("refinement") if isinstance(canon.get("refinement"), dict) else {}
    recut = canon.get("recut") if isinstance(canon.get("recut"), dict) else {}
    active_scope = refine.get("active") is True or recut.get("active") is True

    if mutation and canon_sensitive and canon.get("locked") is True and not active_scope:
        reasons.append(
            "canon-sensitive mutation denied while canon is locked without an active refinement/recut scope"
        )

    replacement_authorized = (
        refine.get("restart_authorized") is True
        or recut.get("source_replacement_authorized") is True
    )
    if (
        mutation
        and protected_canon_replacement
        and canon.get("locked") is True
        and not replacement_authorized
    ):
        reasons.append("protected canon replacement denied while canon is locked")

    changes = [str(x) for x in (requested_changes or []) if str(x).strip()]
    for scope_name, scope in (("refinement", refine), ("recut", recut)):
        if scope.get("active") is not True:
            continue
        allowed = [str(x) for x in scope.get("allowed_changes", []) if x is not None]
        forbidden = [str(x) for x in scope.get("forbidden_changes", []) if x is not None]
        for change in changes:
            if any(_tag_matches(change, item) for item in forbidden):
                reasons.append(f"{scope_name} forbidden change requested: {change}")
        if changes and not allowed:
            reasons.append(f"{scope_name} scope is active but declares no allowed_changes")
        else:
            outside = [
                change
                for change in changes
                if not any(_tag_matches(change, item) for item in allowed)
            ]
            if outside:
                reasons.append(
                    f"{scope_name} changes outside allowed scope: {', '.join(sorted(outside))}"
                )

    if mutation and not action.strip():
        reasons.append("mutation action name is required")

    if reasons:
        return GateDecision("DENY", tuple(dict.fromkeys(reasons)))
    return GateDecision(
        "PASS",
        ("attestation, runtime freshness, branch, stage, canon and scope checks passed",),
        refresh_required=mutation,
    )
