#!/usr/bin/env python3
"""Canonical media-approach and visual-direction evidence for Studio projects."""
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


def _write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _project_dir(project_id: str) -> tuple[dict, Path, Path]:
    current = production_project.status(project_id)
    if not current.get("initialized"):
        raise RuntimeError("production workspace is not initialized")
    return current, Path(current["engine_root"]), Path(current["project_dir"])


def _visual_refs(refs: dict) -> bool:
    return bool(refs.get("videos") or refs.get("images"))


def available_capabilities() -> list[dict]:
    return CORE.capabilities()


def set_capabilities(project_id: str, capabilities: list[str], approach_summary: str) -> dict:
    current, engine, project_dir = _project_dir(project_id)
    if current.get("stage") not in {"REFERENCES_ANALYZED", "APPROACH_ESTABLISHED"}:
        raise RuntimeError("media approach requires REFERENCES_ANALYZED stage")
    valid = {str(x.get("id")) for x in CORE.capabilities() if isinstance(x, dict) and x.get("id")}
    selected = [str(x).strip() for x in capabilities if str(x).strip()]
    unknown = sorted(set(selected) - valid)
    if not selected:
        raise ValueError("select at least one canonical media capability")
    if unknown:
        raise ValueError("unknown media capabilities: " + ", ".join(unknown))
    summary = str(approach_summary or "").strip()
    if not summary:
        raise ValueError("approach_summary is required")

    plan_path = project_dir / "MEDIA_PLAN.json"
    plan = _read_json(plan_path, {})
    plan["schema"] = plan.get("schema") or "aivideoedit.media-plan.v1"
    plan["selected_capabilities"] = selected
    plan["approach_summary"] = summary
    plan["approach_authority"] = "explicit_current_user_or_agent_input"
    plan["capabilities_locked_at"] = production_project.base.now()
    _write_json(plan_path, plan)

    state_path = project_dir / "PROJECT_STATE.json"
    state = _read_json(state_path, {})
    state["media_plan_valid"] = True
    state["selected_capability_count"] = len(selected)
    # Visual approach is only established immediately when a visual reference exists.
    refs = _read_json(project_dir / "REFERENCE_MANIFEST.json", {"videos": [], "images": []})
    if _visual_refs(refs):
        state["visual_approach_established"] = True
        plan["user_approach_established"] = True
        _write_json(plan_path, plan)
    _write_json(state_path, state)

    commit = production_project._git_commit_paths(
        engine, [plan_path, state_path], "Record canonical media approach"
    )
    production_project._clear_guard_marker(engine)
    return {
        **production_project.status(project_id),
        "selected_capabilities": selected,
        "approach_summary": summary,
        "visual_reference_present": _visual_refs(refs),
        "route_gate_required": not _visual_refs(refs),
        "commit": commit,
    }


def set_routes(project_id: str, routes: list[dict]) -> dict:
    current, engine, project_dir = _project_dir(project_id)
    if current.get("stage") not in {"REFERENCES_ANALYZED", "APPROACH_ESTABLISHED"}:
        raise RuntimeError("visual direction routes require REFERENCES_ANALYZED stage")
    refs = _read_json(project_dir / "REFERENCE_MANIFEST.json", {"videos": [], "images": []})
    if _visual_refs(refs):
        raise RuntimeError("three-route gate is only required when there is no visual reference")

    contract = CORE.production_contract()
    minimum = int(contract.get("reference_policy", {}).get("no_visual_reference_min_options", 3))
    min_beats = int(contract.get("reference_policy", {}).get("no_visual_reference_min_storyboard_beats", 3))
    if len(routes) < minimum:
        raise ValueError(f"at least {minimum} visual-direction routes are required")

    normalized = []
    names, stories, renders = set(), set(), set()
    for index, route in enumerate(routes, start=1):
        if not isinstance(route, dict):
            raise ValueError(f"route {index} must be an object")
        number = int(route.get("number") or index)
        name = str(route.get("name") or "").strip()
        story = str(route.get("story_approach") or "").strip()
        rendering = str(route.get("rendering_route") or "").strip()
        beats = route.get("storyboard") or []
        if not name or not story or not rendering:
            raise ValueError(f"route {index} requires name, story_approach, and rendering_route")
        if len(beats) < min_beats:
            raise ValueError(f"route {index} requires at least {min_beats} storyboard beats")
        board = []
        for beat_index, beat in enumerate(beats, start=1):
            if not isinstance(beat, dict):
                raise ValueError(f"route {index} storyboard beat {beat_index} must be an object")
            description = str(beat.get("description") or "").strip()
            if not description:
                raise ValueError(f"route {index} storyboard beat {beat_index} requires description")
            board.append({"number": int(beat.get("number") or beat_index), "description": description})
        key_name, key_story, key_render = name.casefold(), story.casefold(), rendering.casefold()
        if key_name in names or key_story in stories or key_render in renders:
            raise ValueError("routes must be materially distinct in name, story approach, and rendering route")
        names.add(key_name); stories.add(key_story); renders.add(key_render)
        normalized.append({
            "number": number,
            "name": name,
            "story_approach": story,
            "rendering_route": rendering,
            "storyboard": board,
        })

    plan_path = project_dir / "MEDIA_PLAN.json"
    plan = _read_json(plan_path, {})
    plan["visual_direction_gate"] = {
        "required": True,
        "presented_in_chat": True,
        "locked": False,
        "options": normalized,
        "user_selection": None,
    }
    plan["user_approach_established"] = False
    _write_json(plan_path, plan)

    state_path = project_dir / "PROJECT_STATE.json"
    state = _read_json(state_path, {})
    state["visual_approach_established"] = False
    _write_json(state_path, state)
    commit = production_project._git_commit_paths(engine, [plan_path, state_path], "Record visual direction routes")
    production_project._clear_guard_marker(engine)
    return {**production_project.status(project_id), "routes": normalized, "route_gate_required": True, "commit": commit}


def select_route(project_id: str, selected_option_numbers: list[int], recorded_user_instruction: str, status: str = "selected") -> dict:
    current, engine, project_dir = _project_dir(project_id)
    plan_path = project_dir / "MEDIA_PLAN.json"
    plan = _read_json(plan_path, {})
    gate = plan.get("visual_direction_gate")
    if not isinstance(gate, dict) or not gate.get("required"):
        raise RuntimeError("visual direction route gate has not been created")
    selection_status = str(status or "selected").strip().lower()
    if selection_status not in {"selected", "hybrid"}:
        raise ValueError("status must be selected or hybrid")
    numbers = [int(x) for x in selected_option_numbers]
    valid = {int(x.get("number")) for x in gate.get("options", []) if isinstance(x, dict) and x.get("number") is not None}
    if not numbers or any(x not in valid for x in numbers):
        raise ValueError("selection references an unknown visual-direction option")
    if selection_status == "selected" and len(numbers) != 1:
        raise ValueError("selected status requires exactly one option")
    if selection_status == "hybrid" and len(numbers) < 2:
        raise ValueError("hybrid status requires at least two options")
    instruction = str(recorded_user_instruction or "").strip()
    if not instruction:
        raise ValueError("recorded_user_instruction is required")

    gate["user_selection"] = {
        "status": selection_status,
        "selected_option_numbers": numbers,
        "recorded_user_instruction": instruction,
    }
    gate["locked"] = True
    plan["visual_direction_gate"] = gate
    plan["user_approach_established"] = True
    _write_json(plan_path, plan)

    state_path = project_dir / "PROJECT_STATE.json"
    state = _read_json(state_path, {})
    state["visual_approach_established"] = True
    state["visual_direction_selection_locked"] = True
    _write_json(state_path, state)
    commit = production_project._git_commit_paths(engine, [plan_path, state_path], "Lock visual direction selection")
    production_project._clear_guard_marker(engine)
    return {
        **production_project.status(project_id),
        "selection": gate["user_selection"],
        "selected_capabilities": plan.get("selected_capabilities", []),
        "commit": commit,
    }


def status(project_id: str) -> dict:
    current, _engine, project_dir = _project_dir(project_id)
    plan = _read_json(project_dir / "MEDIA_PLAN.json", {})
    refs = _read_json(project_dir / "REFERENCE_MANIFEST.json", {"videos": [], "images": []})
    gate = plan.get("visual_direction_gate") if isinstance(plan.get("visual_direction_gate"), dict) else None
    return {
        **current,
        "selected_capabilities": plan.get("selected_capabilities", []),
        "approach_summary": plan.get("approach_summary"),
        "visual_reference_present": _visual_refs(refs),
        "route_gate_required": not _visual_refs(refs),
        "route_options": gate.get("options", []) if gate else [],
        "route_locked": bool(gate and gate.get("locked")),
        "route_selection": gate.get("user_selection") if gate else None,
        "user_approach_established": bool(plan.get("user_approach_established")),
    }
