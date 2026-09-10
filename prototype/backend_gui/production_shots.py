#!/usr/bin/env python3
"""Build canonical shot packages from a locked script and real media evidence."""
from __future__ import annotations
import json, shutil
from pathlib import Path
import server as base
import production_project
import production_storyboard

def _read_json(path,default):
    try:return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:return default

def _write_json(path,payload):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")

def _project(project_id):
    current=production_project.status(project_id)
    if not current.get("initialized"):raise RuntimeError("production workspace is not initialized")
    return current,Path(current["engine_root"]),Path(current["project_dir"])

def _assets(project_id):
    with base.LOCK:return {str(a.get("id")):dict(a) for a in base.STATE["assets"] if a.get("project")==project_id}

def template(project_id):
    current,_engine,project_dir=_project(project_id)
    script=_read_json(project_dir/"SCRIPT.json",{})
    entries=script.get("entries") if isinstance(script.get("entries"),list) else []
    assets=[]
    for a in _assets(project_id).values():
        if a.get("status")=="ready" and a.get("sha256"):
            assets.append({"id":a.get("id"),"filename":a.get("filename"),"content_type":a.get("content_type"),"sha256":a.get("sha256"),"thumbnail_url":a.get("thumbnail_url"),"proxy_url":a.get("proxy_url"),"source_url":a.get("source_url")})
    shots=[{"shot_id":e.get("shot_id"),"start_frame":e.get("start_frame"),"end_frame":e.get("end_frame"),"story_action":e.get("story_action"),"visual_media":e.get("visual_media")} for e in entries if isinstance(e,dict)]
    return {**current,"shots":shots,"assets":assets}

def build_packages(project_id,assignments):
    current,engine,project_dir=_project(project_id)
    if current.get("stage")!="STORYBOARD_LOCKED":raise RuntimeError("shot packages require STORYBOARD_LOCKED stage")
    script=_read_json(project_dir/"SCRIPT.json",{})
    if not script.get("locked") or not isinstance(script.get("entries"),list) or not script.get("entries"):raise RuntimeError("locked SCRIPT.json is required")
    by_shot={str(x.get("shot_id")):x for x in assignments if isinstance(x,dict) and x.get("shot_id")};asset_map=_assets(project_id)
    package_root=project_dir/"shot_packages"
    if package_root.exists():shutil.rmtree(package_root)
    package_root.mkdir(parents=True,exist_ok=True);package_paths=[];used_assets=set()
    for entry in script["entries"]:
        shot_id=str(entry.get("shot_id") or "").strip()
        if not shot_id:raise RuntimeError("script contains an entry without shot_id")
        assignment=by_shot.get(shot_id,{});asset_ids=assignment.get("asset_ids") if isinstance(assignment.get("asset_ids"),list) else []
        if not asset_ids:raise ValueError(f"{shot_id} requires at least one real media asset")
        evidence=[]
        for asset_id in asset_ids:
            asset=asset_map.get(str(asset_id))
            if not asset:raise ValueError(f"{shot_id} references unknown project asset {asset_id}")
            if asset.get("status")!="ready" or not str(asset.get("sha256") or "").strip():raise RuntimeError(f"{shot_id} asset {asset.get('filename') or asset_id} is not ready/hashed")
            used_assets.add(str(asset_id));evidence.append({"asset_id":str(asset_id),"uri":f"aive://asset/{asset_id}","name":asset.get("filename"),"sha256":asset.get("sha256"),"status":str(assignment.get("status") or "ingested"),"role":str(assignment.get("role") or "scripted_visual_media"),"content_type":asset.get("content_type")})
        pkg=package_root/shot_id;pkg.mkdir(parents=True,exist_ok=True)
        _write_json(pkg/"package.json",{"schema":"aivideoedit.shot-package.v1","shot_id":shot_id,"script_entry":entry,"media_evidence":evidence,"build_notes":str(assignment.get("notes") or "").strip(),"built_at":base.now()});package_paths.append(pkg/"package.json")
    state_path=project_dir/"PROJECT_STATE.json";state=_read_json(state_path,{})
    state["shot_package_count"]=len(package_paths);state["shot_packages_built"]=True;state["media_evidence_verified"]=True;state["shot_package_asset_count"]=len(used_assets);_write_json(state_path,state)
    commit=production_project._git_commit_paths(engine,package_paths+[state_path],"Build real-media shot packages");production_project._clear_guard_marker(engine)
    narrative=production_storyboard.run_narrative_guard(project_id)
    if not narrative.get("ok"):
        state["shot_packages_built"]=False;state["media_evidence_verified"]=False;_write_json(state_path,state);production_project._git_commit_paths(engine,[state_path],"Reject invalid shot package evidence")
        raise RuntimeError("canonical narrative guard rejected shot packages: "+str(narrative.get("stdout") or narrative.get("stderr") or "unknown error")[-1800:])
    return {**status(project_id),"commit":commit,"narrative_guard":"PASS"}

def status(project_id):
    current,_engine,project_dir=_project(project_id);root=project_dir/"shot_packages";packages=[]
    if root.is_dir():
        for pkg in sorted(root.iterdir()):
            if not pkg.is_dir():continue
            data=_read_json(pkg/"package.json",{});packages.append({"shot_id":data.get("shot_id") or pkg.name,"media_evidence_count":len(data.get("media_evidence",[])) if isinstance(data.get("media_evidence"),list) else 0})
    state=_read_json(project_dir/"PROJECT_STATE.json",{})
    return {**current,"package_count":len(packages),"packages":packages,"shot_packages_built":bool(state.get("shot_packages_built")),"media_evidence_verified":bool(state.get("media_evidence_verified"))}
