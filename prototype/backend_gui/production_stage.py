#!/usr/bin/env python3
"""Workstation preconditions layered in front of canonical stage advancement."""
from __future__ import annotations

import json
from pathlib import Path

import server as base
import production_project
import production_storyboard
from core_adapter import CORE


def _read_json(path: Path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return default


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _reference_policy_ok(refs: dict, contract: dict) -> tuple[bool, list[str]]:
    problems=[]; policy=contract.get("reference_policy", {})
    max_seconds=float(policy.get("short_video_max_seconds",30.0)); max_frames=int(policy.get("short_video_max_frames",1800))
    for ref in refs.get("videos",[]):
        name=str(ref.get("name") or "video"); duration=float(ref.get("duration_seconds") or 0); total=int(ref.get("total_frames") or 0); extracted=int(ref.get("extracted_frames") or 0)
        short=duration<=max_seconds and total<=max_frames
        if not ref.get("analysis_complete"): problems.append(f"{name}: reference analysis incomplete")
        if short:
            if ref.get("extraction_policy")!="all_frames" or extracted!=total or total<=0: problems.append(f"{name}: short reference requires all-frame evidence")
        else:
            if ref.get("extraction_policy")!="meaningful_sampling": problems.append(f"{name}: long reference requires meaningful sampling")
            if extracted<=0 or not ref.get("sampling_description") or not ref.get("coverage"): problems.append(f"{name}: long-reference sampling evidence incomplete")
    for ref in refs.get("images",[]):
        if not ref.get("analysis_complete"): problems.append(f"{ref.get('name') or 'image'}: image inspection incomplete")
    return not problems, problems


def _validate_next_stage(current: dict, target_stage: str) -> None:
    states=CORE.production_contract().get("states",[]); current_stage=current.get("stage")
    if current_stage not in states: raise RuntimeError(f"current production stage is invalid: {current_stage}")
    if target_stage not in states: raise ValueError(f"unknown production stage: {target_stage}")
    i=states.index(current_stage); expected=states[i+1] if i+1<len(states) else None
    if target_stage!=expected: raise ValueError(f"only the next stage may be requested; expected {expected or 'none'}")


def _generic_guarded_advance(project_id: str, target_stage: str, *, narrative: bool=False) -> dict:
    current=production_project.status(project_id); _validate_next_stage(current,target_stage)
    engine=Path(current["engine_root"]); project_dir=Path(current["project_dir"]); state_path=project_dir/"PROJECT_STATE.json"; status_path=project_dir/"STATUS.md"
    old_state=state_path.read_text(encoding="utf-8"); old_status=status_path.read_text(encoding="utf-8") if status_path.is_file() else ""
    state=_read_json(state_path,{}); state["stage"]=target_stage; state["stage_requested_by"]="aivideoedit-workstation"; state["stage_requested_at"]=base.now(); _write_json(state_path,state)
    status_path.write_text(f"# Status\n\nStage: {target_stage}\n\nPending canonical guard verification.\n",encoding="utf-8"); production_project._clear_guard_marker(engine)
    guard=production_project.run_guard(project_id)
    narrative_guard={"ok":True,"stdout":"","stderr":""}
    if guard.get("guard_pass") and narrative:
        narrative_guard=production_storyboard.run_narrative_guard(project_id)
    if not guard.get("guard_pass") or not narrative_guard.get("ok"):
        state_path.write_text(old_state,encoding="utf-8"); status_path.write_text(old_status,encoding="utf-8"); production_project._clear_guard_marker(engine)
        return {**production_project.status(project_id),"ok":False,"advanced":False,"requested_stage":target_stage,"guard_stdout":guard.get("stdout",""),"guard_stderr":guard.get("stderr",""),"narrative_stdout":narrative_guard.get("stdout",""),"narrative_stderr":narrative_guard.get("stderr",""),"error":"canonical guard rejected the requested stage"}
    status_path.write_text(f"# Status\n\nStage: {target_stage}\n\nCanonical production guard: PASS.\nCanonical narrative guard: {'PASS' if narrative else 'not required'}.\n",encoding="utf-8")
    commit=production_project._git_commit_paths(engine,[state_path,status_path],f"Advance production to {target_stage}"); production_project._write_guard_marker(project_id)
    return {**production_project.status(project_id),"ok":True,"advanced":True,"requested_stage":target_stage,"commit":commit,"guard_stdout":guard.get("stdout",""),"narrative_stdout":narrative_guard.get("stdout","")}


def _validate_approach(project_dir: Path) -> tuple[dict,dict,list[str]]:
    state=_read_json(project_dir/"PROJECT_STATE.json",{}); plan=_read_json(project_dir/"MEDIA_PLAN.json",{}); refs=_read_json(project_dir/"REFERENCE_MANIFEST.json",{"videos":[],"images":[]}); problems=[]
    valid={str(x.get("id")) for x in CORE.capabilities() if isinstance(x,dict) and x.get("id")}; selected=plan.get("selected_capabilities") if isinstance(plan.get("selected_capabilities"),list) else []
    if not selected: problems.append("select at least one canonical media capability")
    unknown=[str(x) for x in selected if str(x) not in valid]
    if unknown: problems.append("unknown media capabilities: "+", ".join(unknown))
    if not str(plan.get("approach_summary") or "").strip(): problems.append("explicit approach summary is missing")
    if not state.get("media_plan_valid"): problems.append("media plan has not been validated")
    if not state.get("visual_approach_established"): problems.append("visual/media approach is not established")
    if not bool(refs.get("videos") or refs.get("images")):
        gate=plan.get("visual_direction_gate")
        if not isinstance(gate,dict): problems.append("no-reference production requires three visual-direction routes")
        else:
            options=gate.get("options") if isinstance(gate.get("options"),list) else []; min_options=int(CORE.production_contract().get("reference_policy",{}).get("no_visual_reference_min_options",3))
            if len(options)<min_options: problems.append(f"no-reference production requires at least {min_options} routes")
            if not gate.get("presented_in_chat"): problems.append("visual-direction routes have not been presented to the user")
            if not gate.get("locked"): problems.append("visual-direction selection is not locked")
            selection=gate.get("user_selection")
            if not isinstance(selection,dict) or not selection.get("selected_option_numbers"): problems.append("explicit user route selection is missing")
            if not str((selection or {}).get("recorded_user_instruction") or "").strip(): problems.append("current user selection instruction is not recorded")
            if not plan.get("user_approach_established"): problems.append("user approach selection is not established")
    return state,plan,problems


def advance(project_id: str, target_stage: str) -> dict:
    current=production_project.status(project_id)
    if not current.get("initialized"): raise RuntimeError("production workspace is not initialized")
    target_stage=str(target_stage or "").strip(); _validate_next_stage(current,target_stage)
    if target_stage=="SOURCE_INGESTED": return production_project.advance(project_id,target_stage)
    project_dir=Path(current["project_dir"]); engine=Path(current["engine_root"])
    if target_stage=="REFERENCES_ANALYZED":
        state=_read_json(project_dir/"PROJECT_STATE.json",{}); refs=_read_json(project_dir/"REFERENCE_MANIFEST.json",{"videos":[],"images":[]}); music=_read_json(project_dir/"MUSIC_ANALYSIS.json",{}); policy_ok,problems=_reference_policy_ok(refs,CORE.production_contract())
        required={"reference_analysis_complete":bool(state.get("reference_analysis_complete")),"music_analysis_complete":bool(state.get("music_analysis_complete")) and bool(music.get("analysis_complete")),"lyrics_status_resolved":bool(state.get("lyrics_status_resolved")),"genre_authority_resolved":bool(state.get("genre_authority_resolved")),"reference_policy_satisfied":policy_ok}
        missing=[k for k,v in required.items() if not v]
        if missing: raise RuntimeError("REFERENCES_ANALYZED gate is not satisfied: "+", ".join(missing)+(": "+"; ".join(problems[:6]) if problems else ""))
        state["reference_policy_satisfied"]=True; _write_json(project_dir/"PROJECT_STATE.json",state); production_project._git_commit_paths(engine,[project_dir/"PROJECT_STATE.json"],"Record reference-analysis gate evidence"); production_project._clear_guard_marker(engine)
    if target_stage=="APPROACH_ESTABLISHED":
        state,_plan,problems=_validate_approach(project_dir)
        if problems: raise RuntimeError("APPROACH_ESTABLISHED gate is not satisfied: "+"; ".join(problems))
        state["visual_approach_established"]=True; state["media_plan_valid"]=True; _write_json(project_dir/"PROJECT_STATE.json",state); production_project._git_commit_paths(engine,[project_dir/"PROJECT_STATE.json"],"Record approach gate evidence"); production_project._clear_guard_marker(engine)
    if target_stage=="STORYBOARD_LOCKED":
        board=production_storyboard.status(project_id)
        missing=[]
        if not board.get("storyboard_exists"): missing.append("storyboard is not authored")
        if not board.get("storyboard_locked"): missing.append("storyboard is not locked")
        if not board.get("script_locked"): missing.append("production script is not locked")
        if not board.get("entry_count"): missing.append("script has no entries")
        if missing: raise RuntimeError("STORYBOARD_LOCKED gate is not satisfied: "+"; ".join(missing))
        return _generic_guarded_advance(project_id,target_stage,narrative=True)
    return _generic_guarded_advance(project_id,target_stage)
