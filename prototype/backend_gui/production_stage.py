#!/usr/bin/env python3
"""Workstation preconditions layered in front of canonical stage advancement."""
from __future__ import annotations

import json
from pathlib import Path

import production_project
from core_adapter import CORE


def _read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _reference_policy_ok(refs: dict, contract: dict) -> tuple[bool, list[str]]:
    problems: list[str] = []
    policy = contract.get("reference_policy", {})
    max_seconds = float(policy.get("short_video_max_seconds", 30.0))
    max_frames = int(policy.get("short_video_max_frames", 1800))
    for ref in refs.get("videos", []):
        name = str(ref.get("name") or "video")
        duration = float(ref.get("duration_seconds") or 0)
        total = int(ref.get("total_frames") or 0)
        extracted = int(ref.get("extracted_frames") or 0)
        short = duration <= max_seconds and total <= max_frames
        if not ref.get("analysis_complete"):
            problems.append(f"{name}: reference analysis incomplete")
        if short:
            if ref.get("extraction_policy") != "all_frames" or extracted != total or total <= 0:
                problems.append(f"{name}: short reference requires all-frame evidence")
        else:
            if ref.get("extraction_policy") != "meaningful_sampling":
                problems.append(f"{name}: long reference requires meaningful sampling")
            if extracted <= 0 or not ref.get("sampling_description") or not ref.get("coverage"):
                problems.append(f"{name}: long-reference sampling evidence incomplete")
    for ref in refs.get("images", []):
        if not ref.get("analysis_complete"):
            problems.append(f"{ref.get('name') or 'image'}: image inspection incomplete")
    return not problems, problems


def advance(project_id: str, target_stage: str) -> dict:
    current = production_project.status(project_id)
    if not current.get("initialized"):
        raise RuntimeError("production workspace is not initialized")
    target_stage = str(target_stage or "").strip()

    if target_stage == "REFERENCES_ANALYZED":
        project_dir = Path(current["project_dir"])
        state = _read_json(project_dir / "PROJECT_STATE.json", {})
        refs = _read_json(project_dir / "REFERENCE_MANIFEST.json", {"videos": [], "images": []})
        music = _read_json(project_dir / "MUSIC_ANALYSIS.json", {})
        policy_ok, problems = _reference_policy_ok(refs, CORE.production_contract())
        required = {
            "reference_analysis_complete": bool(state.get("reference_analysis_complete")),
            "music_analysis_complete": bool(state.get("music_analysis_complete")) and bool(music.get("analysis_complete")),
            "lyrics_status_resolved": bool(state.get("lyrics_status_resolved")),
            "genre_authority_resolved": bool(state.get("genre_authority_resolved")),
            "reference_policy_satisfied": policy_ok,
        }
        missing = [key for key, ok in required.items() if not ok]
        if missing:
            detail = problems[:6]
            if not state.get("lyrics_status_resolved"):
                detail.append("lyrics status requires explicit authority")
            if not state.get("genre_authority_resolved"):
                detail.append("genre requires explicit authority")
            if not state.get("music_analysis_complete"):
                detail.append("music signal analysis is incomplete")
            raise RuntimeError(
                "REFERENCES_ANALYZED gate is not satisfied: " + ", ".join(missing)
                + (" · " + "; ".join(detail) if detail else "")
            )
        # Record the computed policy evidence immediately before guarded advance.
        state["reference_policy_satisfied"] = True
        state["reference_analysis_complete"] = True
        state["music_analysis_complete"] = True
        state_path = project_dir / "PROJECT_STATE.json"
        state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        engine = Path(current["engine_root"])
        production_project._git_commit_paths(engine, [state_path], "Record reference-analysis gate evidence")
        production_project._clear_guard_marker(engine)

    return production_project.advance(project_id, target_stage)
