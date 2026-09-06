#!/usr/bin/env python3
"""Fail-closed AIVideoEdit production-state validator."""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "general/reusable/PRODUCTION_CONTRACT.json"
MEDIA_PATH = ROOT / "general/reusable/MEDIA_CAPABILITY_MATRIX.json"

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"FAIL: missing {path.relative_to(ROOT)}")
    except Exception as e:
        raise SystemExit(f"FAIL: invalid JSON {path.relative_to(ROOT)}: {e}")

def truthy(v): return v is True

def fail(msg, errors): errors.append(msg)

def discover_project():
    env = os.environ.get("AIVIDEOEDIT_PROJECT_DIR")
    if env: return ROOT / env
    candidates = [p.parent for p in ROOT.glob("projects/*/PROJECT_STATE.json")]
    if len(candidates) == 1: return candidates[0]
    if not candidates: raise SystemExit("FAIL: no projects/*/PROJECT_STATE.json found")
    raise SystemExit("FAIL: multiple project states found; set AIVIDEOEDIT_PROJECT_DIR")

def validate(branch: str):
    contract = load_json(CONTRACT_PATH); media = load_json(MEDIA_PATH)
    errors=[]
    if branch == "main":
        for p in ["AGENTS.md","BIBLE.md","SYSTEM_INDEX.md","general/reusable/PRODUCTION_PIPELINE.md","general/reusable/STYLE_CONTRACT.md","general/reusable/fx_v2/registry.json"]:
            if not (ROOT/p).is_file(): fail(f"missing system file: {p}", errors)
        return errors
    if not branch.startswith("song/"): return [f"production work must use song/<slug>; got {branch}"]
    project=discover_project()
    for name in contract["required_project_files"]:
        if not (project/name).is_file(): fail(f"missing required project file: {project.relative_to(ROOT)}/{name}", errors)
    if errors: return errors
    state=load_json(project/"PROJECT_STATE.json")
    auth=load_json(project/"SOURCE_AUTHORITY.json")
    refs=load_json(project/"REFERENCE_MANIFEST.json")
    plan=load_json(project/"MEDIA_PLAN.json")
    states=contract["states"]
    stage=state.get("stage")
    if stage not in states: return [f"invalid production stage: {stage}"]
    expected_branch=state.get("branch")
    if expected_branch and expected_branch != branch: fail(f"PROJECT_STATE branch mismatch: {expected_branch} != {branch}", errors)
    for denied in contract["default_denied_sources"]:
        if auth.get("allow",{}).get(denied) is True and denied not in auth.get("explicit_user_authorizations",[]):
            fail(f"historical source enabled without explicit user authorization: {denied}", errors)
    idx=states.index(stage)
    def at(name): return idx >= states.index(name)
    if at("SOURCE_INGESTED") and not truthy(state.get("source_ingest_complete")): fail("SOURCE_INGESTED requires source_ingest_complete=true", errors)
    videos=refs.get("videos",[]); images=refs.get("images",[])
    if at("REFERENCES_ANALYZED"):
        if not truthy(state.get("reference_analysis_complete")): fail("reference analysis not complete", errors)
        for v in videos:
            dur=float(v.get("duration_seconds",0)); total=int(v.get("total_frames",0)); ext=int(v.get("extracted_frames",0)); policy=v.get("extraction_policy")
            short=(dur <= contract["reference_policy"]["short_video_max_seconds"] and total <= contract["reference_policy"]["short_video_max_frames"])
            if short and (policy != "all_frames" or ext != total): fail(f"short reference must extract all frames: {v.get('name','video')} {ext}/{total}", errors)
            if not short:
                if policy != "meaningful_sampling": fail(f"long reference requires meaningful_sampling: {v.get('name','video')}", errors)
                if ext <= 0 or not v.get("sampling_description") or not v.get("coverage"): fail(f"long reference sampling evidence incomplete: {v.get('name','video')}", errors)
            if not truthy(v.get("analysis_complete")): fail(f"reference video analysis incomplete: {v.get('name','video')}", errors)
        for im in images:
            if not truthy(im.get("analysis_complete")): fail(f"source image analysis incomplete: {im.get('name','image')}", errors)
    if at("APPROACH_ESTABLISHED"):
        selected=plan.get("selected_capabilities",[])
        valid={x["id"] for x in media["capabilities"]}
        unknown=[x for x in selected if x not in valid]
        if not selected: fail("MEDIA_PLAN selected_capabilities is empty", errors)
        if unknown: fail("unknown media capabilities: "+", ".join(unknown), errors)
        if not truthy(state.get("visual_approach_established")): fail("visual/media approach not established", errors)
        if not videos and not images and not truthy(plan.get("user_approach_established")): fail("no-reference production requires user_approach_established=true before generated media", errors)
    checks={
      "STORYBOARD_LOCKED":"storyboard_locked","SHOT_PACKAGES_BUILT":"shot_packages_built","SHOT_PROOFS_ACCEPTED":"shot_proofs_accepted",
      "FX_LOCKED":"fx_lock_verified","ASSEMBLED":"assembly_complete","FINAL_QC_PASSED":"final_qc_passed","ARCHIVED":"archive_complete"}
    for s,key in checks.items():
        if at(s) and not truthy(state.get(key)): fail(f"{s} requires {key}=true", errors)
    if at("FX_LOCKED") and not (project/"fx.lock.json").is_file(): fail("FX_LOCKED requires fx.lock.json", errors)
    if at("SHOT_PACKAGES_BUILT"):
        sp=project/"shot_packages"
        packages=[p for p in sp.iterdir() if p.is_dir()] if sp.is_dir() else []
        if not packages: fail("SHOT_PACKAGES_BUILT requires at least one shot package", errors)
    return errors

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--branch", default=os.environ.get("GITHUB_REF_NAME") or os.environ.get("AIVIDEOEDIT_BRANCH") or "")
    args=ap.parse_args()
    if not args.branch: raise SystemExit("FAIL: branch required (--branch or GITHUB_REF_NAME)")
    errors=validate(args.branch)
    if errors:
        print("AIVideoEdit production contract: FAIL", file=sys.stderr)
        for e in errors: print("- "+e, file=sys.stderr)
        raise SystemExit(1)
    print("AIVideoEdit production contract: PASS")
if __name__ == "__main__": main()
