#!/usr/bin/env python3
"""Provider-neutral generated-media requests and canonical asset registration.

A generation request is intent, not evidence. Only an existing ready + hashed
workstation asset can be registered as generated production media.
"""
from __future__ import annotations

import json
import uuid
from pathlib import Path

import server as base
import production_project


def _read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _project(project_id: str) -> tuple[dict, Path, Path]:
    current = production_project.status(project_id)
    if not current.get("initialized"):
        raise RuntimeError("production workspace is not initialized")
    return current, Path(current["engine_root"]), Path(current["project_dir"])


def _requests_path(project_id: str) -> Path:
    return base.PROJECT_ROOT / project_id / "generation_requests.json"


def request_generation(project_id: str, *, shot_id: str, capability: str, prompt: str,
                       provider_hint: str = "", notes: str = "") -> dict:
    current, _engine, project_dir = _project(project_id)
    if current.get("stage") not in {"STORYBOARD_LOCKED", "SHOT_PACKAGES_BUILT"}:
        raise RuntimeError("generated media requests require STORYBOARD_LOCKED or SHOT_PACKAGES_BUILT stage")
    shot_id = str(shot_id or "").strip()
    prompt = str(prompt or "").strip()
    capability = str(capability or "").strip()
    if not shot_id or not prompt or not capability:
        raise ValueError("shot_id, capability, and prompt are required")

    script = _read_json(project_dir / "SCRIPT.json", {})
    valid_shots = {str(x.get("shot_id")) for x in script.get("entries", []) if isinstance(x, dict)}
    if shot_id not in valid_shots:
        raise ValueError(f"unknown script shot: {shot_id}")

    plan = _read_json(project_dir / "MEDIA_PLAN.json", {})
    selected = set(plan.get("selected_capabilities", [])) if isinstance(plan.get("selected_capabilities"), list) else set()
    if capability not in selected:
        raise ValueError(f"capability is not selected in MEDIA_PLAN: {capability}")

    path = _requests_path(project_id)
    data = _read_json(path, {"schema": "aivideoedit.generation-requests.v1", "requests": []})
    rec = {
        "id": uuid.uuid4().hex[:12],
        "project_id": project_id,
        "shot_id": shot_id,
        "capability": capability,
        "prompt": prompt,
        "provider_hint": str(provider_hint or "").strip() or None,
        "notes": str(notes or "").strip() or None,
        "status": "requested",
        "created_at": base.now(),
        "asset_id": None,
    }
    data.setdefault("requests", []).append(rec)
    _write_json(path, data)
    return {"ok": True, "request": rec}


def register_generated(project_id: str, *, asset_id: str, shot_id: str, capability: str,
                       request_id: str = "", provider: str = "", model: str = "",
                       prompt: str = "", role: str = "generated_visual") -> dict:
    current, engine, project_dir = _project(project_id)
    if current.get("stage") not in {"STORYBOARD_LOCKED", "SHOT_PACKAGES_BUILT"}:
        raise RuntimeError("generated media registration requires STORYBOARD_LOCKED or SHOT_PACKAGES_BUILT stage")
    with base.LOCK:
        asset = base.find_asset(str(asset_id))
        if not asset or asset.get("project") != project_id:
            raise ValueError("generated asset is not part of this project")
        if asset.get("status") != "ready" or not str(asset.get("sha256") or "").strip():
            raise RuntimeError("generated asset must exist, be ready, and have SHA-256 evidence")
        asset["origin"] = "generated"
        asset["kind"] = str(capability or "generated_media")
        asset["role"] = str(role or "generated_visual")
        asset["generation"] = {
            "request_id": str(request_id or "").strip() or None,
            "shot_id": str(shot_id or "").strip(),
            "capability": str(capability or "").strip(),
            "provider": str(provider or "").strip() or None,
            "model": str(model or "").strip() or None,
            "prompt": str(prompt or "").strip() or None,
            "registered_at": base.now(),
        }
        asset["updated_at"] = base.now()
        base.save_state()
        asset_copy = dict(asset)

    if not asset_copy["generation"]["shot_id"] or not asset_copy["generation"]["capability"]:
        raise ValueError("shot_id and capability are required")

    plan = _read_json(project_dir / "MEDIA_PLAN.json", {})
    selected = set(plan.get("selected_capabilities", [])) if isinstance(plan.get("selected_capabilities"), list) else set()
    if capability not in selected:
        raise ValueError(f"capability is not selected in MEDIA_PLAN: {capability}")

    manifest_path = project_dir / "ASSET_MANIFEST.json"
    manifest = _read_json(manifest_path, {"schema": "aivideoedit.asset-manifest.v1", "assets": []})
    assets = manifest.get("assets", []) if isinstance(manifest.get("assets"), list) else []
    record = {
        "id": asset_copy.get("id"),
        "name": asset_copy.get("filename"),
        "uri": f"aive://asset/{asset_copy.get('id')}",
        "sha256": asset_copy.get("sha256"),
        "content_type": asset_copy.get("content_type"),
        "size_bytes": asset_copy.get("size_bytes"),
        "status": "ready",
        "origin": "generated",
        "kind": str(capability),
        "role": str(role or "generated_visual"),
        "authority": "current_project_generated",
        "generation": asset_copy.get("generation"),
        "metadata": asset_copy.get("metadata") or {},
        "qc": asset_copy.get("qc") or {"status": "unchecked"},
    }
    replaced = False
    for i, old in enumerate(assets):
        if isinstance(old, dict) and str(old.get("id")) == str(asset_id):
            assets[i] = record
            replaced = True
            break
    if not replaced:
        assets.append(record)
    manifest["assets"] = assets
    manifest["generated_media_updated_at"] = base.now()
    _write_json(manifest_path, manifest)

    req_path = _requests_path(project_id)
    reqs = _read_json(req_path, {"schema": "aivideoedit.generation-requests.v1", "requests": []})
    if request_id:
        for req in reqs.get("requests", []):
            if isinstance(req, dict) and req.get("id") == request_id:
                req["status"] = "fulfilled"
                req["asset_id"] = asset_id
                req["fulfilled_at"] = base.now()
        _write_json(req_path, reqs)

    commit = production_project._git_commit_paths(engine, [manifest_path], "Register generated production media evidence")
    production_project._clear_guard_marker(engine)
    return {"ok": True, "asset": base.public_asset(asset_copy), "manifest_record": record, "commit": commit}


def reject_generated(project_id: str, *, asset_id: str, reason: str) -> dict:
    current, engine, project_dir = _project(project_id)
    reason = str(reason or "").strip()
    if not reason:
        raise ValueError("rejection reason is required")
    with base.LOCK:
        asset = base.find_asset(str(asset_id))
        if not asset or asset.get("project") != project_id:
            raise ValueError("asset not found in project")
        asset["creative_status"] = "rejected"
        asset["rejection_reason"] = reason
        asset["updated_at"] = base.now()
        base.save_state()
    manifest_path = project_dir / "ASSET_MANIFEST.json"
    manifest = _read_json(manifest_path, {})
    for rec in manifest.get("assets", []) if isinstance(manifest.get("assets"), list) else []:
        if isinstance(rec, dict) and str(rec.get("id")) == str(asset_id):
            rec["creative_status"] = "rejected"
            rec["rejection_reason"] = reason
    _write_json(manifest_path, manifest)
    state_path = project_dir / "PROJECT_STATE.json"
    state = _read_json(state_path, {})
    state["shot_proofs_accepted"] = False
    state["final_qc_passed"] = False
    _write_json(state_path, state)
    commit = production_project._git_commit_paths(engine, [manifest_path, state_path], "Record generated media rejection")
    production_project._clear_guard_marker(engine)
    return {"ok": True, "asset_id": asset_id, "creative_status": "rejected", "commit": commit}


def status(project_id: str) -> dict:
    current, _engine, project_dir = _project(project_id)
    reqs = _read_json(_requests_path(project_id), {"requests": []})
    manifest = _read_json(project_dir / "ASSET_MANIFEST.json", {"assets": []})
    generated = [x for x in manifest.get("assets", []) if isinstance(x, dict) and x.get("origin") == "generated"]
    return {
        **current,
        "requests": reqs.get("requests", []),
        "generated_assets": generated,
        "requested_count": sum(1 for x in reqs.get("requests", []) if isinstance(x, dict) and x.get("status") == "requested"),
        "generated_count": len(generated),
    }
