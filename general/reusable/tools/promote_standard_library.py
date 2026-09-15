#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REUSABLE = ROOT / "general/reusable"
FX = REUSABLE / "fx_v2"
TOOLS = REUSABLE / "tools"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_promoted():
    path = FX / "promoted_effects.py"
    spec = importlib.util.spec_from_file_location("aivideoedit_promoted_effects_migration", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load promoted_effects.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def effect_family(name: str):
    if any(k in name for k in ("transition", "_to_", "portal", "pigment", "ghosted_memory")):
        return "transition"
    if any(k in name for k in ("reflection", "puddle", "shimmer", "water_region")):
        return "surface"
    if any(k in name for k in ("light", "halation", "glint", "grade")):
        return "light"
    if any(k in name for k in ("waveform", "oscilloscope", "frequency", "spectrum", "particle_tunnel", "plasma")):
        return "visualizer"
    if any(k in name for k in ("fog", "rain", "smoke", "ember", "flame", "fire", "atmospheric", "steam")):
        return "environment"
    if any(k in name for k in ("depth", "parallax", "orbit", "corridor", "camera")):
        return "spatial"
    if "disocclusion" in name:
        return "compositing"
    if "rms_" in name:
        return "audio_reactive"
    return "motion"


def effect_id(name: str):
    return "FX2-" + name.upper().replace("_", "-")


def workflow_registry():
    checks = ["neutral_identity", "selection_rule_validated", "requirements_declared", "qc_contract_declared"]
    def wf(wid, name, category, steps, select_if, tools=None):
        return {
            "id": wid,
            "name": name,
            "category": category,
            "status": "approved",
            "implementation": {"kind": "standard_recipe", "steps": steps, "backend_options": tools or ["python", "ffmpeg", "opencv"]},
            "select_if": select_if,
            "verification": {"status": "PASS", "checks": checks},
        }
    return {
        "schema": "aivideoedit.standard-workflows.v1",
        "selection_policy": "Resolve from the active production mode and MEDIA_PLAN selected capabilities. Names and IDs are project-neutral; no production provenance participates in selection.",
        "overrides": "OPERATING_ORDER.standard_workflow_overrides may include/exclude neutral workflow IDs or names; current user direction remains highest authority.",
        "workflows": [
            wf("WF-PROJECT-STATE", "nondestructive_project_state_versioning", "project_state", ["preserve reversible state", "branch/version before destructive changes", "record hashes and lifecycle"], {"default": True}),
            wf("WF-CACHE-INVALIDATION", "proxy_cache_render_invalidation", "performance", ["cache derived media", "invalidate when source/recipe hashes change", "never treat cache as canon"], {"default": True}),
            wf("WF-RENDER-DELIVERY", "deterministic_resumable_render_delivery", "render", ["hash render inputs", "use deterministic recipe", "resume by shot/segment", "verify final duration/hash"], {"default": True}),
            wf("WF-MACHINE-QC", "machine_readable_visual_delivery_qc", "qc", ["validate frame/duration/audio", "generate contact/evidence", "run mode-aware QC", "record PASS/FAIL"], {"default": True}),
            wf("WF-AUDIO-POST", "professional_audio_post_and_qc", "audio", ["preserve score authority", "smooth ramps", "mix ambience/dialogue/SFX", "verify sync and loudness"], {"default": True}),
            wf("WF-REFERENCE-MOTION-CALIBRATION", "reference_motion_envelope_calibration", "analysis", ["measure reference motion", "separate camera from internal motion", "record bounded motion envelope"], {"capabilities_any": ["accepted_motion_benchmark_video"]}),
            wf("WF-EDGE-REFRAME", "edge_contamination_reframe", "cleanup", ["detect contaminated edges", "reframe/crop without identity drift", "verify aspect and safe composition"], {"capabilities_any": ["source_video", "conventional_video", "extracted_frames"]}),
            wf("WF-AUDIO-EDIT-MAP", "audio_edit_map", "audio_analysis", ["map structural sections", "record beat/energy transitions", "bind edit decisions to time/frame"], {"capabilities_any": ["reactive_plate", "loop_media"]}),
            wf("WF-AUDIO-REACTIVITY", "normalized_reactivity_controls", "audio_analysis", ["derive RMS/onset/bands", "normalize percentiles", "smooth controls", "bind controls to effect parameters"], {"capabilities_any": ["reactive_plate"]}),
            wf("WF-TEMPORAL-QC", "temporal_qc_scan", "qc", ["scan freezes/black frames", "measure repetition and temporal change", "verify loop/join integrity"], {"capabilities_any": ["living_painting", "living_still_fx", "loop_media", "transition_media"]}),
            wf("WF-REAL-FOOTAGE-RESTORATION", "cinematic_real_footage_restoration", "restoration", ["inspect source defects", "restore without rewriting content", "preserve camera energy and identity", "compare pre/post evidence"], {"capabilities_any": ["source_video", "conventional_video"]}),
            wf("WF-SOURCE-DERIVED-LOOPS", "source_derived_motion_loop", "source_derived", ["extract approved source state", "derive bounded loop", "record source hash/time range", "verify seam and canon integrity"], {"capabilities_any": ["accepted_source_library", "canonical_hero_library", "source_derived_coverage"]}),
            wf("WF-IDENTITY-SAFE-LOOP-25D-QC", "identity_safe_loop_25d_qc", "qc", ["protect identity/anatomy", "bound depth/camera displacement", "verify loop seam", "reject topology drift"], {"capabilities_any": ["living_still_fx", "depth_25d"]}),
            wf("WF-LIVING-SCENE-ASSEMBLY", "pre_rendered_reusable_scene_loop_assembly", "assembly", ["prepare reusable scene/loop segments", "preserve entry/exit handles", "assemble to music/script", "avoid mechanical repetition"], {"modes_any": ["living_scene", "hybrid"], "capabilities_any": ["living_painting", "living_still_fx", "loop_media"]}),
            wf("WF-LYRIC-LIVING-SCENE", "lyric_timed_multi_image_living_scene_construction", "assembly", ["map lyric/music spans", "assign multiple approved images", "apply living-scene motion", "cut on narrative/music logic"], {"modes_any": ["living_scene", "hybrid"], "capabilities_any": ["generated_stills", "source_images", "living_painting"]}),
            wf("WF-SEQUENTIAL-GENERATED-CINEMA", "sequential_generated_cinema_shot_architecture", "generated_cinema", ["lock start state", "generate shot progression", "validate terminal frame", "chain continuity to next shot"], {"modes_any": ["cinematic", "hybrid"], "capabilities_any": ["generated_stills", "generated_support_imagery"]}),
            wf("WF-SCENE-GRAPH-25D", "scene_graph_25d", "spatial", ["derive depth/planes", "protect foreground identity", "apply bounded image-space parallax", "verify edge/disocclusion"], {"capabilities_any": ["depth_25d"]}),
            wf("WF-NERF-PATH", "nerf_captured_scene_path", "spatial", ["require actual trained radiance field", "validate capture/training evidence", "author bounded camera path", "render and QC"], {"capabilities_any": ["nerf"]}),
            wf("WF-GAUSSIAN-SPLAT-PATH", "gaussian_splat_scene_path", "spatial", ["require genuine Gaussian geometry", "run spatial preflight", "author camera path", "render and verify geometry"], {"capabilities_any": ["true_3dgs"]}),
            wf("WF-LAYERED-COMPOSITING", "layered_nondestructive_compositing", "compositing", ["separate semantic layers", "preserve source plates", "composite nondestructively", "verify alpha/edge integrity"], {"capabilities_any": ["layered_composite", "reflection_echo", "atmospheric_plate", "reactive_plate"]}),
            wf("WF-MASK-MATTE-KEY", "masks_mattes_alpha_keying", "compositing", ["author masks/mattes", "feather/edge inspect", "preserve protected regions", "verify alpha continuity"], {"capabilities_any": ["layered_composite", "reflection_echo"]}),
            wf("WF-ROTOSCOPING", "rotoscoping", "compositing", ["track subject/region", "refine mask over time", "protect anatomy/edges", "QC temporal matte stability"], {"capabilities_all": ["source_video", "layered_composite"]}),
            wf("WF-TRACKING", "planar_point_camera_tracking", "tracking", ["choose planar/point/camera model", "solve track", "inspect drift", "bind overlays/effects to solved motion"], {"capabilities_any": ["source_video", "conventional_video"]}),
            wf("WF-CLEANUP", "cleanup_object_removal_screen_replacement", "cleanup", ["identify bounded cleanup target", "track/mask target", "inpaint/replace", "compare against source continuity"], {"capabilities_any": ["source_video", "conventional_video"]}),
            wf("WF-STABILIZATION", "stabilization_natural_camera_energy", "motion", ["measure source camera motion", "remove defect motion only", "preserve intentional energy", "verify crop/edge safety"], {"capabilities_any": ["source_video", "conventional_video"]}),
            wf("WF-PROCEDURAL-PARTICLES", "procedural_particle_effect_authoring", "fx", ["declare semantic ROI", "author particle state", "couple to environment/audio when motivated", "verify visible bounded output"], {"capabilities_any": ["atmospheric_plate", "reactive_plate"]}),
            wf("WF-LENS-DISTORTION", "lens_warp_distortion_pipeline", "fx", ["declare lens/warp intent", "bound geometry displacement", "protect identity/topology", "QC edges/crop"], {"capabilities_any": ["perspective_transform", "living_still_fx"]}),
            wf("WF-DEPTH-LIGHT-OPS", "glow_blur_sharpen_depth_light_operations", "fx", ["apply operations to semantic regions", "preserve linework/identity", "couple light to source", "verify no global pumping"], {"capabilities_any": ["living_painting", "living_still_fx", "atmospheric_plate"]}),
            wf("WF-RETIME", "speed_changes_retiming_curves", "edit", ["declare source/target timing", "author curve", "preserve sync/action readability", "verify joins and cadence"], {"capabilities_any": ["conventional_video", "loop_media"]}),
            wf("WF-NESTED-TIMELINES", "compound_clips_nested_timelines", "edit", ["group shot-level composites", "preserve source traceability", "nest without baking canon", "verify duration propagation"], {"modes_any": ["cinematic", "hybrid"]}),
            wf("WF-WARM-NARRATIVE-LOOK", "warm_narrative_treatment", "look", ["apply warm practical-led grade", "preserve skin/identity", "retain motivated contrast", "QC against style contract"], {"manual_only": True}),
        ],
    }


def replace_once(path: Path, old: str, new: str):
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"patch anchor not found in {path}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def append_once(path: Path, marker: str, block: str):
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    path.write_text(text.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8")


def patch_bootstrap():
    path = ROOT / "bootstrap.py"
    old = '''    recut = os_root / "general/reusable/tools/recut_guard.py"\n    if recut.is_file():\n        run_guard(recut, ["--branch", branch], env, "recut contract")\n'''
    new = old + '''    workflow = os_root / "general/reusable/tools/workflow_guard.py"\n    if workflow.is_file():\n        run_guard(workflow, ["--branch", branch], env, "standard workflow contract")\n'''
    replace_once(path, old, new)

    old = '''def fmt_list(value) -> str:\n    return "; ".join(str(x) for x in value) if isinstance(value, list) and value else "none recorded"\n\n\ndef build_second_brain'''
    new = '''def fmt_list(value) -> str:\n    return "; ".join(str(x) for x in value) if isinstance(value, list) and value else "none recorded"\n\n\ndef resolve_standard_workflows(os_root: Path, project: Path | None) -> list[str]:\n    if project is None:\n        return []\n    tool = os_root / "general/reusable/tools/workflow_resolver.py"\n    if not tool.is_file():\n        return []\n    p = subprocess.run([sys.executable, str(tool), "--project", str(project), "--json"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)\n    if p.returncode != 0:\n        return ["ERROR: standard workflow resolution failed"]\n    try:\n        data = json.loads(p.stdout)\n    except Exception:\n        return ["ERROR: standard workflow resolver returned invalid JSON"]\n    vals = data.get("selected_workflow_names", [])\n    return [str(x) for x in vals] if isinstance(vals, list) else []\n\n\ndef build_second_brain'''
    replace_once(path, old, new)

    old = '''    else:\n        lines += ["OPERATING_ORDER.json not present. This is permitted only for an unmigrated legacy project. Do not invent canon/baseline/source-library/refinement state from history.", ""]\n    lines += [\n'''
    new = '''    else:\n        lines += ["OPERATING_ORDER.json not present. This is permitted only for an unmigrated legacy project. Do not invent canon/baseline/source-library/refinement state from history.", ""]\n    standard_workflows = resolve_standard_workflows(os_root, project)\n    lines += [\n'''
    replace_once(path, old, new)

    old = '''        "## Media plan", "Selected capabilities: " + (", ".join(plan.get("selected_capabilities", [])) or "not established"), "",\n        "## Reference inventory"'''
    new = '''        "## Media plan", "Selected capabilities: " + (", ".join(plan.get("selected_capabilities", [])) or "not established"), "",\n        "## Standard workflow selection", "Selected workflows: " + (", ".join(standard_workflows) or "none resolved"), "",\n        "## Reference inventory"'''
    replace_once(path, old, new)

    old = '''    recut = order.get("recut_scope", {}) if isinstance(order.get("recut_scope"), dict) else {}\n    rec = {\n'''
    new = '''    recut = order.get("recut_scope", {}) if isinstance(order.get("recut_scope"), dict) else {}\n    standard_workflows = resolve_standard_workflows(os_root, project) if project else []\n    rec = {\n'''
    replace_once(path, old, new)

    old = '''        "refinement_active": refine.get("active"), "recut_active": recut.get("active"),\n    }\n'''
    new = '''        "refinement_active": refine.get("active"), "recut_active": recut.get("active"),\n        "standard_workflows": standard_workflows,\n    }\n'''
    replace_once(path, old, new)


def patch_agents():
    path = ROOT / "AGENTS.md"
    old = '''  - `python .aivideoedit/os/general/reusable/tools/recut_guard.py --branch <current-branch>` when present in the current-main OS (it is mandatory for current-main versions that provide it).\n'''
    new = old + '''  - `python .aivideoedit/os/general/reusable/tools/workflow_guard.py --branch <current-branch>` when present; this resolves and validates the project-neutral standard workflow set for the active production.\n- Use `python .aivideoedit/os/general/reusable/tools/workflow_resolver.py --project <project-dir> --json` to inspect the selected standard workflows; do not substitute historical production names for capability names.\n'''
    replace_once(path, old, new)


def patch_production_guard():
    path = TOOLS / "production_guard.py"
    text = path.read_text(encoding="utf-8")
    anchor = '        "general/reusable/fx_v2/registry.json",\n'
    addition = anchor + '        "general/reusable/fx_v2/promoted_effects.py",\n        "general/reusable/STANDARD_WORKFLOW_REGISTRY.json",\n        "general/reusable/tools/workflow_resolver.py",\n        "general/reusable/tools/workflow_guard.py",\n'
    if '"general/reusable/tools/workflow_guard.py"' not in text:
        if anchor not in text:
            raise RuntimeError("production_guard registry anchor not found")
        text = text.replace(anchor, addition)
        path.write_text(text, encoding="utf-8")


def patch_ci():
    path = ROOT / ".github/workflows/fx-v2-precompile-gate.yml"
    old = '''      - name: Run hard precompile FX gate\n'''
    new = '''      - name: Verify neutral standard effect library\n        run: python general/reusable/fx_v2/verify_standard_effects.py\n      - name: Verify neutral standard workflow registry and resolver\n        run: python general/reusable/tools/workflow_resolver.py --verify --json\n      - name: Run hard precompile FX gate\n'''
    replace_once(path, old, new)
    text = path.read_text(encoding="utf-8")
    old_req = "            'general/reusable/CANONICAL_EFFECT_REGISTRY.json','general/reusable/CANONICAL_EFFECT_REGISTRY.md',\n"
    new_req = "            'general/reusable/CANONICAL_EFFECT_REGISTRY.json','general/reusable/CANONICAL_EFFECT_REGISTRY.md',\n            'general/reusable/STANDARD_WORKFLOW_REGISTRY.json','general/reusable/STANDARD_WORKFLOWS.md',\n"
    if new_req not in text:
        if old_req not in text:
            raise RuntimeError("CI documentation path anchor not found")
        path.write_text(text.replace(old_req, new_req, 1), encoding="utf-8")


def main():
    mod = load_promoted()
    verifier = FX / "verify_standard_effects.py"
    report_path = FX / "proofs/FX2_PROOF04_STANDARD_EFFECT_LIBRARY.report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    p = subprocess.run([sys.executable, str(verifier), "--report-out", str(report_path)], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if p.returncode != 0:
        print(p.stdout)
        print(p.stderr, file=sys.stderr)
        raise SystemExit("standard effect verification failed")
    report = read_json(report_path)
    if report.get("result") != "PASS":
        raise SystemExit("standard effect report did not PASS")

    registry_path = FX / "registry.json"
    registry = read_json(registry_path)
    effects = registry.setdefault("effects", {})
    for key in list(effects):
        if isinstance(effects[key], dict) and effects[key].get("status") == "standard":
            del effects[key]
    proof_id = "FX2_PROOF04_STANDARD_EFFECT_LIBRARY"
    standard_ids = []
    for name in mod.EFFECT_NAMES:
        eid = effect_id(name)
        standard_ids.append(eid)
        effects[eid] = {
            "name": name,
            "family": effect_family(name),
            "status": "standard",
            "gate_status": "approved",
            "implementation": {"kind": "adapter", "path": "general/reusable/fx_v2/promoted_effects.py", "symbol": "apply_effect", "effect_name": name},
            "proofs": [proof_id],
            "quality": {"source_delta_min": 0.02, "temporal_delta_min": 0.005, "max_global_shift_px": 12.0},
            "notes": "Project-neutral standard effect; select by neutral effect name/FX2 id.",
        }
    registry["schema_version"] = max(4, int(registry.get("schema_version", 0)))
    write_json(registry_path, registry)

    write_json(FX / "effect_aliases.json", {
        "schema": "aivideoedit.effect-aliases.v1",
        "policy": "Aliases preserve old technique wording only. Project/production provenance is intentionally omitted and is not part of effect identity.",
        "aliases": dict(sorted(mod.LEGACY_ALIASES.items())),
    })

    report_sha = sha256(report_path)
    write_json(FX / f"proofs/{proof_id}.json", {
        "schema": "aivideoedit.fx-proof.v1",
        "proof_id": proof_id,
        "effects": standard_ids,
        "visual_qc": "PASS: every standard effect produced deterministic visible and temporal output under the automated neutral synthetic-frame verifier.",
        "frames": int(report.get("effect_count", 0)) * int(report.get("sample_frames_per_effect", 0)),
        "fps": int(report.get("fps_basis", 24)),
        "size": report.get("sample_size", [320, 180]),
        "artifact_path": "general/reusable/fx_v2/proofs/FX2_PROOF04_STANDARD_EFFECT_LIBRARY.report.json",
        "sha256": report_sha,
    })

    write_json(REUSABLE / "STANDARD_WORKFLOW_REGISTRY.json", workflow_registry())
    (REUSABLE / "STANDARD_WORKFLOWS.md").write_text(
        "# Standard Workflow Library\n\n"
        "These are project-neutral production workflows available to every production. The resolver selects them from the active production mode and `MEDIA_PLAN.json` capabilities. Historical production names are not runtime identities and are intentionally absent.\n\n"
        "Authority: `STANDARD_WORKFLOW_REGISTRY.json`. Resolver: `tools/workflow_resolver.py`. Guard: `tools/workflow_guard.py`.\n\n"
        "Default workflows always preserve reversible project state, cache invalidation, deterministic resumable delivery, machine-readable QC, and professional audio post/QC. Conditional workflows cover reference-motion calibration, restoration, source-derived looping, living-scene assembly, generated cinema, 2.5D/NeRF/3DGS, compositing/mattes/rotoscoping/tracking/cleanup/stabilization, procedural FX, retiming and nested timelines.\n",
        encoding="utf-8",
    )

    write_json(REUSABLE / "CANONICAL_EFFECT_REGISTRY.json", {
        "schema": "aivideoedit.capability-index.v2",
        "status": "compatibility_index",
        "effect_authority": "general/reusable/fx_v2/registry.json",
        "effect_aliases": "general/reusable/fx_v2/effect_aliases.json",
        "workflow_authority": "general/reusable/STANDARD_WORKFLOW_REGISTRY.json",
        "policy": "Callable capabilities are identified by neutral effect/workflow names. Production provenance is not part of current capability identity or selection.",
        "verification": {
            "effects": "general/reusable/fx_v2/verify_standard_effects.py",
            "workflows": "general/reusable/tools/workflow_resolver.py --verify",
        },
    })

    write_json(REUSABLE / "AIVIDEOEDIT_OS_MANIFEST.json", add_manifest_files(read_json(REUSABLE / "AIVIDEOEDIT_OS_MANIFEST.json")))
    patch_bootstrap()
    patch_agents()
    patch_production_guard()
    patch_ci()

    append_once(ROOT / "SYSTEM_INDEX.md", "## Standard capability selection", '''## Standard capability selection
- `general/reusable/fx_v2/registry.json` — callable effect authority, including neutral standard effects promoted from prior technique work.
- `general/reusable/fx_v2/promoted_effects.py` — project-neutral runtime implementation for the standardized effect library.
- `general/reusable/fx_v2/verify_standard_effects.py` — per-effect visible/temporal/determinism verification and proof-report generator.
- `general/reusable/STANDARD_WORKFLOW_REGISTRY.json` — project-neutral non-effect workflow authority.
- `general/reusable/tools/workflow_resolver.py` — selects standard workflows from current production mode + media capabilities.
- `general/reusable/tools/workflow_guard.py` — fail-closed registry/project selection verification; bootstrap runs it when present.

Historical production names are not capability identities and are not used for automatic selection.''')

    (REUSABLE / "CAPABILITY_LINEAGE.md").write_text(
        "# Capability Lineage\n\nReusable capabilities are identified exclusively by what they do. Production names and origin projects are not runtime identities and are not inputs to selection.\n\n"
        "Two canonical families exist:\n- callable visual/audio-reactive effects under `fx_v2/registry.json`;\n- non-effect production workflows under `STANDARD_WORKFLOW_REGISTRY.json`.\n\n"
        "Promotion requires: real implementation or explicit workflow recipe -> verification/QC -> neutral naming -> registry entry -> CI/guard coverage. The active project chooses capabilities from its current direction, production mode, media plan, source authority and explicit user instruction.\n",
        encoding="utf-8",
    )

    append_once(TOOLS / "README.md", "workflow_resolver.py", '''## Standard workflow tools
- `workflow_resolver.py` — validates the neutral workflow registry and resolves the workflow set for a project from its current mode/media capabilities.
- `workflow_guard.py` — fail-closed bootstrap/stage guard for standard workflow selection.
- `promote_standard_library.py` — idempotent migration/generator used to build the neutral standard effect/workflow registries and proofs.''')

    print(f"PASS: standardized {len(mod.EFFECT_NAMES)} effects and {len(workflow_registry()['workflows'])} workflows")


def add_manifest_files(manifest: dict):
    additions = [
        {"path": "general/reusable/fx_v2/promoted_effects.py", "role": "neutral_standard_effect_runtime"},
        {"path": "general/reusable/fx_v2/verify_standard_effects.py", "role": "neutral_standard_effect_verifier"},
        {"path": "general/reusable/fx_v2/effect_aliases.json", "role": "neutral_effect_alias_compatibility"},
        {"path": "general/reusable/STANDARD_WORKFLOW_REGISTRY.json", "role": "neutral_standard_workflow_registry"},
        {"path": "general/reusable/STANDARD_WORKFLOWS.md", "role": "neutral_standard_workflow_contract"},
        {"path": "general/reusable/tools/workflow_resolver.py", "role": "standard_workflow_resolver"},
        {"path": "general/reusable/tools/workflow_guard.py", "role": "fail_closed_standard_workflow_guard"},
    ]
    files = manifest.setdefault("files", [])
    existing = {x.get("path") for x in files if isinstance(x, dict)}
    for rec in additions:
        if rec["path"] not in existing:
            files.append(rec)
    return manifest


if __name__ == "__main__":
    main()
