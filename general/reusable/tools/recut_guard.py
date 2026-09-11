#!/usr/bin/env python3
"""Fail-closed validation for canonical-source recovery/recut workflows.

This guard supplements the existing production and narrative guards without changing
accepted-baseline semantics. It activates only for Director Brain projects using the
new source-library/recut fields or related artifacts.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
from pathlib import Path
from typing import Any

SCRIPT_ROOT = Path(__file__).resolve().parents[3]
if os.environ.get("AIVIDEOEDIT_REPO_ROOT"):
    ROOT = Path(os.environ["AIVIDEOEDIT_REPO_ROOT"]).resolve()
elif SCRIPT_ROOT.name == "os" and SCRIPT_ROOT.parent.name == ".aivideoedit":
    ROOT = SCRIPT_ROOT.parent.parent.resolve()
else:
    ROOT = SCRIPT_ROOT.resolve()
if os.environ.get("AIVIDEOEDIT_OS_ROOT"):
    OS_ROOT = Path(os.environ["AIVIDEOEDIT_OS_ROOT"]).resolve()
elif SCRIPT_ROOT.name == "os" and SCRIPT_ROOT.parent.name == ".aivideoedit":
    OS_ROOT = SCRIPT_ROOT.resolve()
else:
    OS_ROOT = ROOT

CONTRACT_PATH = OS_ROOT / "general/reusable/PRODUCTION_CONTRACT.json"
TOOLS = OS_ROOT / "general/reusable/tools"
FX = OS_ROOT / "general/reusable/fx_v2"
SOURCE_ROLES = {"hero_library", "shot_library", "visual_world", "reference_content"}
SOURCE_STATUSES = {"none", "accepted", "retired"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing {path}")
    except Exception as e:
        raise ValueError(f"invalid JSON {path}: {e}")


def nonempty(v: Any) -> bool:
    return isinstance(v, str) and bool(v.strip())


def valid_sha(v: Any) -> bool:
    return nonempty(v) and bool(re.fullmatch(r"[0-9a-fA-F]{64}", v.strip()))


def discover_project() -> Path | None:
    env = os.environ.get("AIVIDEOEDIT_PROJECT_DIR")
    if env:
        p = Path(env)
        return p.resolve() if p.is_absolute() else (ROOT / p).resolve()
    candidates = [p.parent for p in ROOT.glob("projects/*/PROJECT_STATE.json")]
    if len(candidates) == 1:
        return candidates[0]
    return None


def _import_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_source_library(order: dict, errors: list[str]) -> dict:
    source = order.get("accepted_source_library")
    if source is None:
        return {"status": "none"}
    if not isinstance(source, dict):
        errors.append("OPERATING_ORDER.accepted_source_library must be an object")
        return {"status": "none"}
    status = source.get("status")
    if status not in SOURCE_STATUSES:
        errors.append("accepted_source_library.status must be none, accepted, or retired")
        return source
    if status == "accepted":
        if source.get("role") not in SOURCE_ROLES:
            errors.append("accepted source library requires a supported role")
        if not nonempty(source.get("file_or_locator")):
            errors.append("accepted source library requires file_or_locator")
        if not valid_sha(source.get("sha256")):
            errors.append("accepted source library sha256 must contain 64 hexadecimal characters")
        if not nonempty(source.get("user_acceptance_statement")):
            errors.append("accepted source library requires user_acceptance_statement")
        if source.get("content_reuse_authorized") is not True:
            errors.append("accepted source library requires content_reuse_authorized=true")
        if source.get("timeline_locked") is not False:
            errors.append("accepted source library requires timeline_locked=false so the edit remains editable")
    return source


def validate_recut_scope(order: dict, source: dict, errors: list[str]) -> dict:
    scope = order.get("recut_scope")
    if scope is None:
        return {"active": False}
    if not isinstance(scope, dict):
        errors.append("OPERATING_ORDER.recut_scope must be an object")
        return {"active": False}
    active = scope.get("active")
    if not isinstance(active, bool):
        errors.append("recut_scope.active must be boolean")
        return scope
    if active:
        if source.get("status") != "accepted":
            errors.append("active recut_scope requires accepted_source_library.status=accepted")
        defects = scope.get("named_defects")
        if not isinstance(defects, list) or not defects or not all(nonempty(x) for x in defects):
            errors.append("active recut_scope requires non-empty named_defects")
        for key in ("allowed_changes", "forbidden_changes"):
            value = scope.get(key)
            if not isinstance(value, list) or not value or not all(nonempty(x) for x in value):
                errors.append(f"active recut_scope requires non-empty {key}")
        if scope.get("source_replacement_authorized") is not False:
            errors.append("recut_scope.source_replacement_authorized must be false unless user explicitly chooses a different workflow")
    return scope


def validate_render_recipe(project: Path, errors: list[str]) -> None:
    path = project / "RENDER_RECIPE.json"
    if not path.is_file():
        return
    try:
        recipe = load_json(path)
    except ValueError as e:
        errors.append(str(e)); return
    if recipe.get("schema") != "aivideoedit.render-recipe.v1":
        errors.append("RENDER_RECIPE.json has invalid schema")
    for key in ("recipe_identity", "proof_backend", "production_backend"):
        if not nonempty(recipe.get(key)):
            errors.append(f"RENDER_RECIPE.{key} is required")
    impl = recipe.get("render_implementation")
    if not isinstance(impl, dict) or not nonempty(impl.get("file_or_locator")) or not valid_sha(impl.get("sha256")):
        errors.append("RENDER_RECIPE.render_implementation requires locator and sha256")
    if recipe.get("proof_backend") != recipe.get("production_backend"):
        mapping = recipe.get("backend_mapping")
        if not isinstance(mapping, dict) or not mapping:
            errors.append("backend substitution requires non-empty backend_mapping")
        proof = recipe.get("equivalence_proof")
        if not isinstance(proof, dict):
            errors.append("backend substitution requires equivalence_proof")
        else:
            if proof.get("status") != "PASS": errors.append("backend substitution requires equivalence_proof.status=PASS")
            if proof.get("behavior_preserved") is not True: errors.append("equivalence proof requires behavior_preserved=true")
            if proof.get("effects_visible") is not True: errors.append("equivalence proof requires effects_visible=true")
            if proof.get("traceable") is not True: errors.append("equivalence proof requires traceable=true")
            media = proof.get("representative_proof")
            if not isinstance(media, dict) or not nonempty(media.get("file_or_locator")) or not valid_sha(media.get("sha256")):
                errors.append("equivalence proof requires representative proof locator and sha256")


def _asset_entries(project: Path) -> list[dict]:
    path = project / "ASSET_MANIFEST.json"
    if not path.is_file(): return []
    try: data = load_json(path)
    except ValueError: return []
    entries = data.get("assets") if isinstance(data.get("assets"), list) else data.get("entries")
    return [x for x in entries if isinstance(x, dict)] if isinstance(entries, list) else []


def validate_source_derived_provenance(project: Path, source: dict, scope: dict, errors: list[str]) -> None:
    accepted_sha = source.get("sha256") if source.get("status") == "accepted" else None
    for i, asset in enumerate(_asset_entries(project), 1):
        prov = asset.get("provenance") if isinstance(asset.get("provenance"), dict) else {}
        source_derived = asset.get("origin") == "source_derived" or prov.get("kind") == "source_derived"
        if not source_derived:
            continue
        if not valid_sha(prov.get("source_library_sha256")):
            errors.append(f"ASSET_MANIFEST source-derived entry {i} requires provenance.source_library_sha256")
        elif accepted_sha and prov.get("source_library_sha256").lower() != accepted_sha.lower():
            errors.append(f"ASSET_MANIFEST source-derived entry {i} does not derive from the accepted source library")
        if not nonempty(prov.get("derivation")):
            errors.append(f"ASSET_MANIFEST source-derived entry {i} requires provenance.derivation")
        has_time = isinstance(prov.get("source_time_seconds"), (int, float)) and not isinstance(prov.get("source_time_seconds"), bool)
        rng = prov.get("source_range_seconds")
        has_range = isinstance(rng, list) and len(rng) == 2 and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in rng)
        if not (has_time or has_range):
            errors.append(f"ASSET_MANIFEST source-derived entry {i} requires source time or range evidence")
        if scope.get("active") is True and scope.get("source_replacement_authorized") is False and asset.get("replaces_source_library") is True:
            errors.append(f"ASSET_MANIFEST source-derived entry {i} cannot silently replace locked source canon")


def validate_hero_library(project: Path, plan: dict, scope: dict, errors: list[str], warnings: list[str]) -> None:
    selected = plan.get("selected_capabilities", []) if isinstance(plan, dict) else []
    required = "canonical_hero_library" in selected or scope.get("active") is True
    path = project / "HERO_LIBRARY.json"
    if not required and not path.is_file(): return
    if required and not path.is_file():
        errors.append("canonical hero-library workflow requires HERO_LIBRARY.json"); return
    try:
        module = _import_module(TOOLS / "hero_library_extract.py", "hero_library_extract")
        manifest = load_json(path)
        errors.extend("HERO_LIBRARY: " + e for e in module.validate_library_manifest(manifest))
        warnings.extend("HERO_LIBRARY: " + w for w in module.library_warnings(manifest))
    except Exception as e:
        errors.append(f"cannot validate HERO_LIBRARY.json: {e}")


def validate_project_local_fx(project: Path, errors: list[str]) -> None:
    root = project / "project_fx"
    if not root.is_dir(): return
    try:
        gate = _import_module(FX / "project_local_fx_gate.py", "project_local_fx_gate")
    except Exception as e:
        errors.append(f"cannot load project-local FX gate: {e}"); return
    for manifest_path in sorted(root.glob("*.json")):
        if manifest_path.name.endswith(".lock.json"): continue
        try: manifest = load_json(manifest_path)
        except ValueError as e: errors.append(str(e)); continue
        errors.extend(f"{manifest_path.name}: {e}" for e in gate.validate_manifest(manifest, project))
        lock = manifest_path.with_suffix(".lock.json")
        errors.extend(f"{manifest_path.name}: {e}" for e in gate.validate_lock(manifest_path, lock, project))


def validate_refinement_qc(project: Path, source: dict, scope: dict, stage: str, states: list[str], errors: list[str]) -> None:
    if scope.get("active") is not True or source.get("status") != "accepted": return
    if stage not in states or states.index(stage) < states.index("FINAL_QC_PASSED"): return
    path = project / "REFINEMENT_QC.json"
    if not path.is_file():
        errors.append("recut FINAL_QC_PASSED requires REFINEMENT_QC.json with before/after evidence"); return
    try:
        tool = _import_module(TOOLS / "refinement_qc_compare.py", "refinement_qc_compare")
        data = load_json(path)
        errors.extend("REFINEMENT_QC: " + e for e in tool.validate_comparison(data, source.get("sha256")))
    except Exception as e:
        errors.append(f"cannot validate REFINEMENT_QC.json: {e}")


def validate(branch: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if branch == "main":
        for rel in (
            "general/reusable/RECUT_REFINEMENT.md",
            "general/reusable/tools/hero_library_extract.py",
            "general/reusable/tools/refinement_qc_compare.py",
            "general/reusable/tools/recut_guard.py",
            "general/reusable/fx_v2/project_local_fx_gate.py",
        ):
            if not (OS_ROOT / rel).is_file(): errors.append(f"missing recut system file: {rel}")
        return errors, warnings
    if not branch.startswith("song/"):
        return errors, warnings
    project = discover_project()
    if project is None:
        return errors, warnings
    try:
        state = load_json(project / "PROJECT_STATE.json")
        order = load_json(project / "OPERATING_ORDER.json") if (project / "OPERATING_ORDER.json").is_file() else {}
        plan = load_json(project / "MEDIA_PLAN.json") if (project / "MEDIA_PLAN.json").is_file() else {}
        contract = load_json(CONTRACT_PATH)
    except ValueError as e:
        return [str(e)], warnings
    try: version = int(state.get("director_brain_version", 0) or 0)
    except Exception: version = 0
    if version < 2 or not order:
        return errors, warnings
    source = validate_source_library(order, errors)
    scope = validate_recut_scope(order, source, errors)
    validate_render_recipe(project, errors)
    validate_source_derived_provenance(project, source, scope, errors)
    validate_hero_library(project, plan, scope, errors, warnings)
    validate_project_local_fx(project, errors)
    validate_refinement_qc(project, source, scope, state.get("stage", ""), contract.get("states", []), errors)
    return errors, warnings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", default=os.environ.get("GITHUB_REF_NAME") or os.environ.get("AIVIDEOEDIT_BRANCH") or "")
    args = ap.parse_args()
    if not args.branch:
        print("AIVideoEdit recut contract: FAIL\n- branch required"); return 1
    errors, warnings = validate(args.branch)
    for w in warnings: print("AIVideoEdit recut contract: WARN - " + w)
    if errors:
        print("AIVideoEdit recut contract: FAIL")
        for e in errors: print("- " + e)
        return 1
    print("AIVideoEdit recut contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
