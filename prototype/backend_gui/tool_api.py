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
import production_storyboard
from core_adapter import CORE


TOOL_SCHEMAS = [
    {"name":"core.status","description":"Show canonical AIVideoEdit OS/bootstrap status.","input_schema":{"type":"object","properties":{}}},
    {"name":"core.bootstrap","description":"Install and attest an isolated exact current-main AIVideoEdit core.","input_schema":{"type":"object","properties":{"offline":{"type":"boolean"}}}},
    {"name":"capabilities.list","description":"List canonical media capabilities from the bootstrapped OS.","input_schema":{"type":"object","properties":{}}},
    {"name":"fx.list","description":"List reusable effects from the canonical FX registry.","input_schema":{"type":"object","properties":{}}},
    {"name":"project.list","description":"List local workstation projects.","input_schema":{"type":"object","properties":{}}},
    {"name":"project.create","description":"Create a local workstation project.","input_schema":{"type":"object","required":["name"],"properties":{"name":{"type":"string"}}}},
    {"name":"project.status","description":"Return project media and QC summary.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"project.prepare","description":"Queue all missing preview, review-frame and QC work for a project.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.initialize","description":"Create an isolated canonical song-branch production workspace.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.status","description":"Show canonical production branch, stage, next stage, manifest sync state and guard status.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.sync_assets","description":"Sync workstation media into canonical manifests without advancing stage or claiming analysis.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.analyze","description":"Queue evidence-producing reference extraction and music signal analysis.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.set_music_context","description":"Record explicit lyrics status/text and genre authority.","input_schema":{"type":"object","required":["project_id","lyrics_status","genre"],"properties":{"project_id":{"type":"string"},"lyrics_status":{"type":"string","enum":["present","absent"]},"genre":{"type":"string"},"lyrics_text":{"type":"string"},"directing_use":{"type":"string"}}}},
    {"name":"approach.status","description":"Show selected canonical capabilities and visual-direction gate state.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"approach.set_capabilities","description":"Record canonical media capabilities and an explicit production approach summary.","input_schema":{"type":"object","required":["project_id","capabilities","approach_summary"],"properties":{"project_id":{"type":"string"},"capabilities":{"type":"array","items":{"type":"string"}},"approach_summary":{"type":"string"}}}},
    {"name":"approach.set_routes","description":"Record at least three distinct numbered no-reference visual routes with mini-storyboards.","input_schema":{"type":"object","required":["project_id","routes"],"properties":{"project_id":{"type":"string"},"routes":{"type":"array","items":{"type":"object"}},"presentation_channel":{"type":"string","enum":["chat","studio"]}}}},
    {"name":"approach.select_route","description":"Lock the current user's selected visual route or hybrid.","input_schema":{"type":"object","required":["project_id","selected_option_numbers","recorded_user_instruction"],"properties":{"project_id":{"type":"string"},"selected_option_numbers":{"type":"array","items":{"type":"integer"}},"recorded_user_instruction":{"type":"string"},"status":{"type":"string","enum":["selected","hybrid"]}}}},
    {"name":"storyboard.status","description":"Show authored storyboard/script coverage and lock state.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"storyboard.set","description":"Author a full-frame production storyboard/script from explicit user or agent creative decisions.","input_schema":{"type":"object","required":["project_id","entries"],"properties":{"project_id":{"type":"string"},"entries":{"type":"array","items":{"type":"object"}},"target_fps":{"type":"number"},"summary":{"type":"string"},"authority":{"type":"string"}}}},
    {"name":"storyboard.lock","description":"Lock the authored storyboard and production script with a recorded instruction.","input_schema":{"type":"object","required":["project_id","recorded_instruction"],"properties":{"project_id":{"type":"string"},"recorded_instruction":{"type":"string"}}}},
    {"name":"storyboard.guard","description":"Run the bootstrapped canonical narrative guard against the current project.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.guard","description":"Re-run the bootstrapped current-main production guard for a project.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"production.advance","description":"Request exactly the next canonical production stage. Workstation evidence and canonical guards must pass.","input_schema":{"type":"object","required":["project_id","target_stage"],"properties":{"project_id":{"type":"string"},"target_stage":{"type":"string"}}}},
    {"name":"media.list","description":"List registered media assets for a project.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
    {"name":"media.prepare","description":"Queue one preparation operation for a registered asset.","input_schema":{"type":"object","required":["asset_id","operation"],"properties":{"asset_id":{"type":"string"},"operation":{"type":"string","enum":["make_proxy","extract_review_frames","qc_media"]}}}},
    {"name":"storage.status","description":"Show local/external storage configuration.","input_schema":{"type":"object","properties":{}}},
    {"name":"storage.sync","description":"Queue external backup for a project when storage is configured.","input_schema":{"type":"object","required":["project_id"],"properties":{"project_id":{"type":"string"}}}},
]


def schemas() -> list[dict]: return TOOL_SCHEMAS

def _project(project_id: str) -> dict:
    project=base.find_project(project_id)
    if not project: raise ValueError("project not found")
    return project

def _asset(asset_id: str) -> dict:
    asset=base.find_asset(asset_id)
    if not asset: raise ValueError("asset not found")
    return asset

def _create_project(name: str) -> dict:
    clean=(name or "").strip()
    if not clean: raise ValueError("project name is required")
    root_id=base.slugify(clean); project_id=root_id; suffix=2
    with base.LOCK:
        existing={p.get("id") for p in base.STATE["projects"]}
        while project_id in existing: project_id=f"{root_id}-{suffix}"; suffix+=1
        project={"id":project_id,"name":clean[:100],"created_at":base.now(),"updated_at":base.now()}
        base.STATE["projects"].append(project); base.PROJECT_ROOT.joinpath(project_id).mkdir(parents=True,exist_ok=True); base.save_state()
    return project

def _project_status(project_id: str) -> dict:
    project=_project(project_id)
    with base.LOCK:
        assets=[base.public_asset(a) for a in base.STATE["assets"] if a.get("project")==project_id]
        jobs=[dict(j) for j in base.STATE["jobs"] if j.get("project")==project_id]
    qc_pass=sum(1 for a in assets if (a.get("qc") or {}).get("status")=="pass")
    qc_fail=sum(1 for a in assets if (a.get("qc") or {}).get("status")=="fail")
    ready=sum(1 for a in assets if a.get("status")=="ready")
    return {"project":project,"assets":len(assets),"ready_assets":ready,"qc_pass":qc_pass,"qc_fail":qc_fail,"unchecked":max(0,len(assets)-qc_pass-qc_fail),"active_jobs":sum(1 for j in jobs if j.get("status") in {"queued","running"}),"canonical_core":CORE.status(),"production":production_project.status(project_id)}


def call_tool(name: str, arguments: dict | None, *, dispatch_job: Callable[[dict], None], prepare_project: Callable[[str], list[dict]]) -> dict:
    args=arguments or {}
    if name=="core.status": return CORE.status()
    if name=="core.bootstrap": return CORE.bootstrap(bool(args.get("offline",False)))
    if name=="capabilities.list":
        s=CORE.status(); return {"core":s,"capabilities":CORE.capabilities() if s.get("bootstrapped") else []}
    if name=="fx.list":
        s=CORE.status(); return {"core":s,"effects":CORE.effects() if s.get("bootstrapped") else []}
    if name=="project.list":
        with base.LOCK: return {"projects":[dict(p) for p in base.STATE["projects"]]}
    if name=="project.create": return {"project":_create_project(str(args.get("name") or ""))}
    if name=="project.status": return _project_status(str(args.get("project_id") or ""))
    if name=="project.prepare":
        pid=str(args.get("project_id") or ""); _project(pid); jobs=prepare_project(pid); return {"project_id":pid,"queued":len(jobs),"jobs":jobs}
    if name=="production.initialize":
        pid=str(args.get("project_id") or ""); _project(pid); return production_project.initialize(pid)
    if name=="production.status":
        pid=str(args.get("project_id") or ""); _project(pid); return production_project.status(pid)
    if name=="production.sync_assets":
        pid=str(args.get("project_id") or ""); _project(pid); return production_project.sync_assets(pid)
    if name=="production.analyze":
        pid=str(args.get("project_id") or ""); _project(pid); job=base.add_job("analyze_production",pid,None); dispatch_job(job); return {"job":job}
    if name=="production.set_music_context":
        pid=str(args.get("project_id") or ""); _project(pid); return production_analysis.set_music_context(pid,lyrics_status=str(args.get("lyrics_status") or ""),genre=str(args.get("genre") or ""),lyrics_text=str(args.get("lyrics_text") or ""),directing_use=str(args.get("directing_use") or "default"))
    if name=="approach.status":
        pid=str(args.get("project_id") or ""); _project(pid); return production_approach.status(pid)
    if name=="approach.set_capabilities":
        pid=str(args.get("project_id") or ""); _project(pid); caps=args.get("capabilities") if isinstance(args.get("capabilities"),list) else []; return production_approach.set_capabilities(pid,caps,str(args.get("approach_summary") or ""))
    if name=="approach.set_routes":
        pid=str(args.get("project_id") or ""); _project(pid); routes=args.get("routes") if isinstance(args.get("routes"),list) else []; return production_approach.set_routes(pid,routes,str(args.get("presentation_channel") or "studio"))
    if name=="approach.select_route":
        pid=str(args.get("project_id") or ""); _project(pid); nums=args.get("selected_option_numbers") if isinstance(args.get("selected_option_numbers"),list) else []; return production_approach.select_route(pid,nums,str(args.get("recorded_user_instruction") or ""),str(args.get("status") or "selected"))
    if name=="storyboard.status":
        pid=str(args.get("project_id") or ""); _project(pid); return production_storyboard.status(pid)
    if name=="storyboard.set":
        pid=str(args.get("project_id") or ""); _project(pid); entries=args.get("entries") if isinstance(args.get("entries"),list) else []; return production_storyboard.set_storyboard(pid,entries,target_fps=float(args.get("target_fps") or 30.0),summary=str(args.get("summary") or ""),authority=str(args.get("authority") or "current_user_or_agent"))
    if name=="storyboard.lock":
        pid=str(args.get("project_id") or ""); _project(pid); return production_storyboard.lock_storyboard(pid,str(args.get("recorded_instruction") or ""))
    if name=="storyboard.guard":
        pid=str(args.get("project_id") or ""); _project(pid); return production_storyboard.run_narrative_guard(pid)
    if name=="production.guard":
        pid=str(args.get("project_id") or ""); _project(pid); return production_project.run_guard(pid)
    if name=="production.advance":
        pid=str(args.get("project_id") or ""); target=str(args.get("target_stage") or ""); _project(pid); return production_stage.advance(pid,target)
    if name=="media.list":
        pid=str(args.get("project_id") or ""); _project(pid)
        with base.LOCK: assets=[base.public_asset(a) for a in base.STATE["assets"] if a.get("project")==pid]
        return {"assets":assets}
    if name=="media.prepare":
        aid=str(args.get("asset_id") or ""); op=str(args.get("operation") or ""); asset=_asset(aid)
        if op not in {"make_proxy","extract_review_frames","qc_media"}: raise ValueError("unsupported media preparation operation")
        job=base.add_job(op,asset.get("project") or "prototype",aid); dispatch_job(job); return {"job":job}
    if name=="storage.status": return storage.status()
    if name=="storage.sync":
        pid=str(args.get("project_id") or ""); _project(pid)
        if not storage.status().get("configured"): raise ValueError("external storage is not configured")
        job=base.add_job("sync_project",pid,None); dispatch_job(job); return {"job":job}
    raise ValueError(f"unknown tool: {name}")
