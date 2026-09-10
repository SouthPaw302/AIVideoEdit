#!/usr/bin/env python3
"""Provider-neutral Tool API for AIVideoEdit.

This is the stable seam shared by the browser GUI, external agents, future MCP
or ChatGPT integrations, and the hosted API. Tool names describe intent; the
implementation stays behind this module.
"""
from __future__ import annotations

from typing import Callable

import server as base
import storage
import production_project
import production_analysis
import production_stage
import production_approach
from core_adapter import CORE


TOOL_SCHEMAS = [
    {"name": "core.status", "description": "Show canonical AIVideoEdit OS/bootstrap status.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "core.bootstrap", "description": "Install and attest an isolated exact current-main AIVideoEdit core.", "input_schema": {"type": "object", "properties": {"offline": {"type": "boolean"}}}},
    {"name": "capabilities.list", "description": "List canonical media capabilities from the bootstrapped OS.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "fx.list", "description": "List reusable effects from the canonical FX registry.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "project.list", "description": "List local workstation projects.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "project.create", "description": "Create a local workstation project.", "input_schema": {"type": "object", "required": ["name"], "properties": {"name": {"type": "string"}}}},
    {"name": "project.status", "description": "Return project media and QC summary.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "project.prepare", "description": "Queue all missing preview, review-frame and QC work for a project.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "production.initialize", "description": "Create an isolated canonical song-branch production workspace for a browser project and validate INITIALIZED state with the current-main guard.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "production.status", "description": "Show canonical production branch, stage, next stage, manifest sync state and guard status for a project.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "production.sync_assets", "description": "Sync workstation media into canonical ASSET_MANIFEST.json and REFERENCE_MANIFEST.json without advancing production stage or claiming analysis.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "production.analyze", "description": "Queue evidence-producing reference extraction and music signal analysis for a SOURCE_INGESTED project.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "production.set_music_context", "description": "Record explicit lyrics status/text and genre authority. This does not infer or fabricate either value.", "input_schema": {"type": "object", "required": ["project_id", "lyrics_status", "genre"], "properties": {"project_id": {"type": "string"}, "lyrics_status": {"type": "string", "enum": ["present", "absent"]}, "genre": {"type": "string"}, "lyrics_text": {"type": "string"}, "directing_use": {"type": "string"}}}},
    {"name": "approach.status", "description": "Show selected canonical capabilities and visual-direction gate state.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "approach.set_capabilities", "description": "Record canonical media capabilities and an explicit production approach summary.", "input_schema": {"type": "object", "required": ["project_id", "capabilities", "approach_summary"], "properties": {"project_id": {"type": "string"}, "capabilities": {"type": "array", "items": {"type": "string"}}, "approach_summary": {"type": "string"}}}},
    {"name": "approach.set_routes", "description": "Record at least three distinct numbered visual-direction routes with mini-storyboards for a no-reference production, including the user-facing presentation channel.", "input_schema": {"type": "object", "required": ["project_id", "routes"], "properties": {"project_id": {"type": "string"}, "routes": {"type": "array", "items": {"type": "object"}}, "presentation_channel": {"type": "string", "enum": ["chat", "studio"]}}}},
    {"name": "approach.select_route", "description": "Lock the current user's selected visual route or hybrid and record the explicit instruction.", "input_schema": {"type": "object", "required": ["project_id", "selected_option_numbers", "recorded_user_instruction"], "properties": {"project_id": {"type": "string"}, "selected_option_numbers": {"type": "array", "items": {"type": "integer"}}, "recorded_user_instruction": {"type": "string"}, "status": {"type": "string", "enum": ["selected", "hybrid"]}}}},
    {"name": "production.guard", "description": "Re-run the bootstrapped current-main production guard for a project.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "production.advance", "description": "Request exactly the next canonical production stage. Workstation evidence preconditions and the current-main guard must both pass.", "input_schema": {"type": "object", "required": ["project_id", "target_stage"], "properties": {"project_id": {"type": "string"}, "target_stage": {"type": "string"}}}},
    {"name": "media.list", "description": "List registered media assets for a project.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
    {"name": "media.prepare", "description": "Queue one preparation operation for a registered asset.", "input_schema": {"type": "object", "required": ["asset_id", "operation"], "properties": {"asset_id": {"type": "string"}, "operation": {"type": "string", "enum": ["make_proxy", "extract_review_frames", "qc_media"]}}}},
    {"name": "storage.status", "description": "Show local/external storage configuration.", "input_schema": {"type": "object", "properties": {}}},
    {"name": "storage.sync", "description": "Queue external backup for a project when storage is configured.", "input_schema": {"type": "object", "required": ["project_id"], "properties": {"project_id": {"type": "string"}}}},
]


def schemas() -> list[dict]:
    return TOOL_SCHEMAS


def _project(project_id: str) -> dict:
    project = base.find_project(project_id)
    if not project:
        raise ValueError("project not found")
    return project


def _asset(asset_id: str) -> dict:
    asset = base.find_asset(asset_id)
    if not asset:
        raise ValueError("asset not found")
    return asset


def _create_project(name: str) -> dict:
    clean = (name or "").strip()
    if not clean:
        raise ValueError("project name is required")
    root_id = base.slugify(clean)
    project_id = root_id
    suffix = 2
    with base.LOCK:
        existing = {p.get("id") for p in base.STATE["projects"]}
        while project_id in existing:
            project_id = f"{root_id}-{suffix}"
            suffix += 1
        project = {"id": project_id, "name": clean[:100], "created_at": base.now(), "updated_at": base.now()}
        base.STATE["projects"].append(project)
        base.PROJECT_ROOT.joinpath(project_id).mkdir(parents=True, exist_ok=True)
        base.save_state()
    return project


def _project_status(project_id: str) -> dict:
    project = _project(project_id)
    with base.LOCK:
        assets = [base.public_asset(a) for a in base.STATE["assets"] if a.get("project") == project_id]
        jobs = [dict(j) for j in base.STATE["jobs"] if j.get("project") == project_id]
    qc_pass = sum(1 for a in assets if (a.get("qc") or {}).get("status") == "pass")
    qc_fail = sum(1 for a in assets if (a.get("qc") or {}).get("status") == "fail")
    ready = sum(1 for a in assets if a.get("status") == "ready")
    return {
        "project": project,
        "assets": len(assets),
        "ready_assets": ready,
        "qc_pass": qc_pass,
        "qc_fail": qc_fail,
        "unchecked": max(0, len(assets) - qc_pass - qc_fail),
        "active_jobs": sum(1 for j in jobs if j.get("status") in {"queued", "running"}),
        "canonical_core": CORE.status(),
        "production": production_project.status(project_id),
    }


def call_tool(name: str, arguments: dict | None, *, dispatch_job: Callable[[dict], None], prepare_project: Callable[[str], list[dict]]) -> dict:
    args = arguments or {}
    if name == "core.status": return CORE.status()
    if name == "core.bootstrap": return CORE.bootstrap(bool(args.get("offline", False)))
    if name == "capabilities.list":
        status = CORE.status(); return {"core": status, "capabilities": CORE.capabilities() if status.get("bootstrapped") else []}
    if name == "fx.list":
        status = CORE.status(); return {"core": status, "effects": CORE.effects() if status.get("bootstrapped") else []}
    if name == "project.list":
        with base.LOCK: return {"projects": [dict(p) for p in base.STATE["projects"]]}
    if name == "project.create": return {"project": _create_project(str(args.get("name") or ""))}
    if name == "project.status": return _project_status(str(args.get("project_id") or ""))
    if name == "project.prepare":
        project_id=str(args.get("project_id") or ""); _project(project_id); jobs=prepare_project(project_id); return {"project_id":project_id,"queued":len(jobs),"jobs":jobs}
    if name == "production.initialize":
        project_id=str(args.get("project_id") or ""); _project(project_id); return production_project.initialize(project_id)
    if name == "production.status":
        project_id=str(args.get("project_id") or ""); _project(project_id); return production_project.status(project_id)
    if name == "production.sync_assets":
        project_id=str(args.get("project_id") or ""); _project(project_id); return production_project.sync_assets(project_id)
    if name == "production.analyze":
        project_id=str(args.get("project_id") or ""); _project(project_id); job=base.add_job("analyze_production",project_id,None); dispatch_job(job); return {"job":job}
    if name == "production.set_music_context":
        project_id=str(args.get("project_id") or ""); _project(project_id); return production_analysis.set_music_context(project_id,lyrics_status=str(args.get("lyrics_status") or ""),genre=str(args.get("genre") or ""),lyrics_text=str(args.get("lyrics_text") or ""),directing_use=str(args.get("directing_use") or "default"))
    if name == "approach.status":
        project_id=str(args.get("project_id") or ""); _project(project_id); return production_approach.status(project_id)
    if name == "approach.set_capabilities":
        project_id=str(args.get("project_id") or ""); _project(project_id); capabilities=args.get("capabilities") if isinstance(args.get("capabilities"),list) else []; return production_approach.set_capabilities(project_id,capabilities,str(args.get("approach_summary") or ""))
    if name == "approach.set_routes":
        project_id=str(args.get("project_id") or ""); _project(project_id); routes=args.get("routes") if isinstance(args.get("routes"),list) else []; return production_approach.set_routes(project_id,routes,str(args.get("presentation_channel") or "studio"))
    if name == "approach.select_route":
        project_id=str(args.get("project_id") or ""); _project(project_id); numbers=args.get("selected_option_numbers") if isinstance(args.get("selected_option_numbers"),list) else []; return production_approach.select_route(project_id,numbers,str(args.get("recorded_user_instruction") or ""),str(args.get("status") or "selected"))
    if name == "production.guard":
        project_id=str(args.get("project_id") or ""); _project(project_id); return production_project.run_guard(project_id)
    if name == "production.advance":
        project_id=str(args.get("project_id") or ""); target_stage=str(args.get("target_stage") or ""); _project(project_id); return production_stage.advance(project_id,target_stage)
    if name == "media.list":
        project_id=str(args.get("project_id") or ""); _project(project_id)
        with base.LOCK: assets=[base.public_asset(a) for a in base.STATE["assets"] if a.get("project")==project_id]
        return {"assets":assets}
    if name == "media.prepare":
        asset_id=str(args.get("asset_id") or ""); operation=str(args.get("operation") or ""); asset=_asset(asset_id)
        if operation not in {"make_proxy","extract_review_frames","qc_media"}: raise ValueError("unsupported media preparation operation")
        job=base.add_job(operation,asset.get("project") or "prototype",asset_id); dispatch_job(job); return {"job":job}
    if name == "storage.status": return storage.status()
    if name == "storage.sync":
        project_id=str(args.get("project_id") or ""); _project(project_id)
        if not storage.status().get("configured"): raise ValueError("external storage is not configured")
        job=base.add_job("sync_project",project_id,None); dispatch_job(job); return {"job":job}
    raise ValueError(f"unknown tool: {name}")
