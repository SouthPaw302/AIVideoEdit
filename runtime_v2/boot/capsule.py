from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

CAPSULE_SCHEMA = "aivideoedit.boot-capsule.v1"
ATTESTATION_SCHEMA = "aivideoedit.session-attestation.v1"
GUARD_PATHS = (
    "general/reusable/tools/production_guard.py",
    "general/reusable/tools/recut_guard.py",
    "general/reusable/tools/workflow_guard.py",
    "general/reusable/tools/branch_policy.py",
)
REGISTRY_PATHS = (
    "general/reusable/PRODUCTION_CONTRACT.json",
    "general/reusable/STANDARD_WORKFLOW_REGISTRY.json",
    "general/reusable/CANONICAL_EFFECT_REGISTRY.json",
    "general/reusable/fx_v2/registry.json",
    "general/reusable/fx_v2/recipes.json",
)


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _sha256(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _git(repo: Path, *args: str) -> str:
    try:
        p = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except FileNotFoundError:
        return ""
    return p.stdout.strip() if p.returncode == 0 else ""


def _canonical_bytes(data: dict[str, Any]) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _model_snapshot(os_root: Path, repo: Path) -> dict[str, Any]:
    original = os.environ.get("AIVIDEOEDIT_REPO_ROOT")
    os.environ["AIVIDEOEDIT_REPO_ROOT"] = str(repo)
    sys.path.insert(0, str(os_root))
    try:
        from runtime_v2.models.registry import ModelRegistry
        registry = ModelRegistry.load_default()
        resolution = registry.resolve_capability("music_and_beat_analysis")
        return {
            "music_and_beat_analysis": {
                "requested": resolution.requested,
                "resolved": resolution.resolved,
                "available": resolution.available,
                "used_fallback": resolution.used_fallback,
                "reason": resolution.reason,
                "authority": resolution.record.get("authority"),
                "model_path": resolution.model_path,
            }
        }
    except Exception as exc:
        return {"music_and_beat_analysis": {"available": False, "error": str(exc)}}
    finally:
        try:
            sys.path.remove(str(os_root))
        except ValueError:
            pass
        if original is None:
            os.environ.pop("AIVIDEOEDIT_REPO_ROOT", None)
        else:
            os.environ["AIVIDEOEDIT_REPO_ROOT"] = original


def _media_locators(project: Path | None) -> dict[str, Any]:
    if project is None:
        return {}
    refs = _read_json(project / "REFERENCE_MANIFEST.json")
    assets = _read_json(project / "ASSET_MANIFEST.json")
    order = _read_json(project / "OPERATING_ORDER.json")
    baseline = order.get("accepted_baseline") if isinstance(order.get("accepted_baseline"), dict) else {}
    source = order.get("accepted_source_library") if isinstance(order.get("accepted_source_library"), dict) else {}
    return {
        "reference_manifest_sha256": _sha256(project / "REFERENCE_MANIFEST.json"),
        "asset_manifest_sha256": _sha256(project / "ASSET_MANIFEST.json"),
        "reference_counts": {
            "videos": len(refs.get("videos", [])) if isinstance(refs.get("videos"), list) else 0,
            "images": len(refs.get("images", [])) if isinstance(refs.get("images"), list) else 0,
        },
        "accepted_baseline": {
            "status": baseline.get("status"),
            "file_or_locator": baseline.get("file_or_locator"),
            "sha256": baseline.get("sha256"),
        },
        "accepted_source_library": {
            "status": source.get("status"),
            "role": source.get("role"),
            "file_or_locator": source.get("file_or_locator"),
            "sha256": source.get("sha256"),
        },
        "asset_count": len(assets.get("assets", [])) if isinstance(assets.get("assets"), list) else None,
    }


def validate_project_consistency(
    state: dict[str, Any],
    order: dict[str, Any],
    branch: str | None = None,
) -> list[str]:
    errors: list[str] = []
    state_next = str(state.get("exact_next_action") or "").strip()
    order_next = str(order.get("exact_next_action") or "").strip()
    if state_next and order_next and state_next != order_next:
        errors.append("exact_next_action mismatch between PROJECT_STATE.json and OPERATING_ORDER.json")
    state_tool = str(state.get("exact_next_tool") or "").strip()
    order_tool = str(order.get("exact_next_tool") or "").strip()
    if state_tool and order_tool and state_tool != order_tool:
        errors.append("exact_next_tool mismatch between PROJECT_STATE.json and OPERATING_ORDER.json")
    state_branch = str(state.get("branch") or "").strip()
    if branch and state_branch and state_branch != branch:
        errors.append(f"project branch mismatch: PROJECT_STATE={state_branch} active={branch}")
    return errors


def _next_stage(contract: dict[str, Any], stage: str | None) -> str:
    states = contract.get("states", [])
    if isinstance(states, list) and stage in states:
        i = states.index(stage)
        return str(states[i + 1]) if i + 1 < len(states) else "COMPLETE"
    return str(states[0]) if isinstance(states, list) and states else "UNKNOWN"


def build_capsule(
    *,
    repo: Path,
    os_root: Path,
    branch: str,
    project: Path | None,
    authority_ref: str,
    authority_commit: str,
    session_id: str,
) -> dict[str, Any]:
    repo = repo.resolve()
    os_root = os_root.resolve()
    state = _read_json(project / "PROJECT_STATE.json") if project else {}
    order = _read_json(project / "OPERATING_ORDER.json") if project else {}
    contract = _read_json(os_root / "general/reusable/PRODUCTION_CONTRACT.json")
    canon = order.get("canon_lock") if isinstance(order.get("canon_lock"), dict) else {}
    refine = order.get("refinement_scope") if isinstance(order.get("refinement_scope"), dict) else {}
    recut = order.get("recut_scope") if isinstance(order.get("recut_scope"), dict) else {}
    stage = state.get("stage")
    consistency_errors = validate_project_consistency(state, order, branch)
    if consistency_errors:
        raise ValueError("; ".join(consistency_errors))
    order_next = str(order.get("exact_next_action") or "").strip()
    state_next = str(state.get("exact_next_action") or "").strip()
    exact_next_action = order_next or state_next or None
    order_tool = str(order.get("exact_next_tool") or "").strip()
    state_tool = str(state.get("exact_next_tool") or "").strip()
    exact_next_tool = order_tool or state_tool or None
    return {
        "schema": CAPSULE_SCHEMA,
        "session_id": session_id,
        "repository": "SouthPaw302/AIVideoEdit",
        "authority": {"ref": authority_ref, "commit": authority_commit},
        "active": {
            "branch": branch,
            "branch_commit": _git(repo, "rev-parse", "HEAD") or None,
            "project_dir": project.resolve().relative_to(repo).as_posix() if project else None,
            "stage": stage,
            "project_state_sha256": _sha256(project / "PROJECT_STATE.json") if project else None,
            "next_contract_stage": _next_stage(contract, stage),
            "exact_next_action": exact_next_action,
            "exact_next_tool": exact_next_tool,
            "exact_next_action_source": "OPERATING_ORDER.json" if order_next else ("PROJECT_STATE.json" if state_next else None),
        },
        "operating_order": {
            "sha256": _sha256(project / "OPERATING_ORDER.json") if project else None,
            "direction_authority": order.get("direction_authority"),
            "production_mode": order.get("production_mode"),
            "current_user_direction": order.get("current_user_direction"),
        },
        "canon": {
            "locked": canon.get("locked"),
            "items": canon.get("items") if isinstance(canon.get("items"), list) else [],
            "refinement": {
                "active": refine.get("active"),
                "allowed_changes": refine.get("allowed_changes") if isinstance(refine.get("allowed_changes"), list) else [],
                "forbidden_changes": refine.get("forbidden_changes") if isinstance(refine.get("forbidden_changes"), list) else [],
                "restart_authorized": refine.get("restart_authorized"),
            },
            "recut": {
                "active": recut.get("active"),
                "allowed_changes": recut.get("allowed_changes") if isinstance(recut.get("allowed_changes"), list) else [],
                "forbidden_changes": recut.get("forbidden_changes") if isinstance(recut.get("forbidden_changes"), list) else [],
                "source_replacement_authorized": recut.get("source_replacement_authorized"),
            },
        },
        "guards": {path: _sha256(os_root / path) for path in GUARD_PATHS},
        "registries": {path: _sha256(os_root / path) for path in REGISTRY_PATHS},
        "media": _media_locators(project),
        "models": _model_snapshot(os_root, repo),
    }


def sign_capsule(capsule: dict[str, Any], *, key: str | None = None) -> dict[str, Any]:
    raw = _canonical_bytes(capsule)
    digest = hashlib.sha256(raw).hexdigest()
    if key:
        signature = hmac.new(key.encode("utf-8"), raw, hashlib.sha256).hexdigest()
        scheme = "hmac-sha256"
    else:
        signature = digest
        scheme = "sha256"
    return {
        "schema": ATTESTATION_SCHEMA,
        "session_id": capsule.get("session_id"),
        "capsule_sha256": digest,
        "scheme": scheme,
        "signature": signature,
    }


def verify_capsule(
    capsule: dict[str, Any],
    attestation: dict[str, Any],
    *,
    key: str | None = None,
) -> tuple[bool, str]:
    if capsule.get("schema") != CAPSULE_SCHEMA:
        return False, "unsupported capsule schema"
    if attestation.get("schema") != ATTESTATION_SCHEMA:
        return False, "unsupported attestation schema"
    if capsule.get("session_id") != attestation.get("session_id"):
        return False, "session mismatch"
    expected = sign_capsule(capsule, key=key)
    for field in ("capsule_sha256", "scheme", "signature"):
        if not hmac.compare_digest(str(expected.get(field)), str(attestation.get(field))):
            return False, f"attestation {field} mismatch"
    return True, "PASS"


def write_capsule(
    *,
    repo: Path,
    os_root: Path,
    branch: str,
    project: Path | None,
    authority_ref: str,
    authority_commit: str,
    session_id: str,
    cache: bool = True,
) -> tuple[Path, Path]:
    session_dir = repo / ".aivideoedit"
    session_dir.mkdir(parents=True, exist_ok=True)
    capsule = build_capsule(
        repo=repo,
        os_root=os_root,
        branch=branch,
        project=project,
        authority_ref=authority_ref,
        authority_commit=authority_commit,
        session_id=session_id,
    )
    attestation = sign_capsule(capsule, key=os.environ.get("AIVIDEOEDIT_ATTESTATION_KEY"))
    capsule_path = session_dir / "boot_capsule.json"
    attestation_path = session_dir / "session_attestation.json"
    capsule_path.write_text(json.dumps(capsule, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    attestation_path.write_text(json.dumps(attestation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if cache:
        cache_dir = session_dir / "cache"
        cache_dir.mkdir(parents=True, exist_ok=True)
        safe_branch = branch.replace("/", "__")
        (cache_dir / f"boot_capsule.{safe_branch}.json").write_text(
            json.dumps(capsule, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        (cache_dir / f"session_attestation.{safe_branch}.json").write_text(
            json.dumps(attestation, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return capsule_path, attestation_path


def refresh_from_session(repo: Path) -> tuple[Path, Path]:
    repo = repo.resolve()
    session = _read_json(repo / ".aivideoedit" / "session.json")
    if not session:
        raise RuntimeError("cannot refresh capsule without bootstrap session")
    os_root_text = str(session.get("os_root") or "")
    authority_ref = str(session.get("os_authority_ref") or "main")
    authority_commit = str(session.get("os_authority_commit") or session.get("os_main_commit") or "")
    branch = str(session.get("branch") or "")
    session_id = str(session.get("session_id") or "")
    project_text = session.get("project_dir")
    if not os_root_text or not authority_commit or not branch or not session_id:
        raise RuntimeError("bootstrap session is missing capsule refresh fields")
    project = (repo / str(project_text)).resolve() if project_text else None
    return write_capsule(
        repo=repo,
        os_root=Path(os_root_text),
        branch=branch,
        project=project,
        authority_ref=authority_ref,
        authority_commit=authority_commit,
        session_id=session_id,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--os-root", required=True)
    ap.add_argument("--branch", required=True)
    ap.add_argument("--project-dir")
    ap.add_argument("--authority-ref", required=True)
    ap.add_argument("--authority-commit", required=True)
    ap.add_argument("--session-id", required=True)
    args = ap.parse_args()
    repo = Path(args.repo_root).resolve()
    project = None
    if args.project_dir:
        p = Path(args.project_dir)
        project = p.resolve() if p.is_absolute() else (repo / p).resolve()
    capsule_path, attestation_path = write_capsule(
        repo=repo,
        os_root=Path(args.os_root),
        branch=args.branch,
        project=project,
        authority_ref=args.authority_ref,
        authority_commit=args.authority_commit,
        session_id=args.session_id,
    )
    print(json.dumps({"capsule": str(capsule_path), "attestation": str(attestation_path)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
