#!/usr/bin/env python3
"""Regression tests for canonical source-library recovery/recut support."""
from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


hero = load("hero", HERE / "hero_library_extract.py")
qc = load("qc", HERE / "refinement_qc_compare.py")
recut = load("recut", HERE / "recut_guard.py")
fx = load("fx", HERE.parent / "fx_v2" / "project_local_fx_gate.py") if (HERE.parent / "fx_v2" / "project_local_fx_gate.py").is_file() else None


def assert_true(v, msg):
    if not v:
        raise AssertionError(msg)


def source_library(**overrides):
    d = {
        "status": "accepted",
        "role": "hero_library",
        "file_or_locator": "source.mp4",
        "sha256": "a" * 64,
        "user_acceptance_statement": "Use these approved pixels as canon.",
        "content_reuse_authorized": True,
        "timeline_locked": False,
    }
    d.update(overrides)
    return d


def test_accepted_source_library_valid_and_timeline_editable():
    errors = []
    src = recut.validate_source_library({"accepted_source_library": source_library()}, errors)
    assert_true(src["status"] == "accepted" and not errors, str(errors))
    errors = []
    recut.validate_source_library({"accepted_source_library": source_library(timeline_locked=True)}, errors)
    assert_true(any("timeline_locked=false" in e for e in errors), str(errors))


def test_source_library_hash_and_reuse_authorization_required():
    errors = []
    recut.validate_source_library({"accepted_source_library": source_library(sha256="bad", content_reuse_authorized=False)}, errors)
    assert_true(any("64 hexadecimal" in e for e in errors), str(errors))
    assert_true(any("content_reuse_authorized=true" in e for e in errors), str(errors))


def test_baseline_semantics_are_separate():
    order = {"accepted_baseline": {"status": "accepted"}, "accepted_source_library": source_library()}
    errors = []
    recut.validate_source_library(order, errors)
    assert_true(not errors and order["accepted_baseline"]["status"] == "accepted", str(errors))


def test_recut_scope_blocks_source_replacement():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "ASSET_MANIFEST.json").write_text(json.dumps({"assets": [{
            "origin": "source_derived",
            "replaces_source_library": True,
            "provenance": {"kind": "source_derived", "source_library_sha256": "a" * 64, "derivation": "crop/reframe", "source_time_seconds": 1.2}
        }]}))
        errors = []
        scope = {"active": True, "source_replacement_authorized": False}
        recut.validate_source_derived_provenance(root, source_library(), scope, errors)
        assert_true(any("cannot silently replace" in e for e in errors), str(errors))


def test_source_derived_provenance_matches_canon():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "ASSET_MANIFEST.json").write_text(json.dumps({"assets": [{
            "origin": "source_derived",
            "provenance": {"kind": "source_derived", "source_library_sha256": "b" * 64, "derivation": "detail extraction", "source_range_seconds": [1.0, 1.5]}
        }]}))
        errors = []
        recut.validate_source_derived_provenance(root, source_library(), {"active": False}, errors)
        assert_true(any("does not derive" in e for e in errors), str(errors))


def test_backend_substitution_requires_equivalence():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "RENDER_RECIPE.json").write_text(json.dumps({
            "schema": "aivideoedit.render-recipe.v1",
            "recipe_identity": "r1",
            "proof_backend": "python_opencv",
            "production_backend": "ffmpeg",
            "render_implementation": {"file_or_locator": "render.py", "sha256": "c" * 64}
        }))
        errors = []
        recut.validate_render_recipe(root, errors)
        assert_true(any("equivalence_proof" in e for e in errors), str(errors))


def test_backend_substitution_with_equivalence_passes():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "RENDER_RECIPE.json").write_text(json.dumps({
            "schema": "aivideoedit.render-recipe.v1",
            "recipe_identity": "r1",
            "proof_backend": "python_opencv",
            "production_backend": "ffmpeg",
            "backend_mapping": {"zoom": "scale expression"},
            "render_implementation": {"file_or_locator": "render.py", "sha256": "c" * 64},
            "equivalence_proof": {
                "status": "PASS",
                "behavior_preserved": True,
                "effects_visible": True,
                "traceable": True,
                "representative_proof": {"file_or_locator": "proof.mp4", "sha256": "d" * 64}
            }
        }))
        errors = []
        recut.validate_render_recipe(root, errors)
        assert_true(not errors, str(errors))


def test_hero_manifest_valid_and_nonempty():
    manifest = {
        "schema": hero.SCHEMA,
        "source": {"identity": "source.mp4", "sha256": "a" * 64},
        "selection": {"candidate_count": 8, "near_duplicate_rejections": 1},
        "entries": [{
            "frame_index": 10,
            "time_seconds": .4,
            "frame_sha256": "b" * 64,
            "lifecycle_status": "candidate",
            "source_range_seconds": [.2, .6],
            "visual_signature": {"vector": [.1, .2]},
            "diversity_evidence": {"min_distance_to_selected": .2},
        }],
    }
    assert_true(not hero.validate_library_manifest(manifest), str(hero.validate_library_manifest(manifest)))


def test_empty_hero_library_fails():
    m = {"schema": hero.SCHEMA, "source": {"identity": "x", "sha256": "a" * 64}, "entries": []}
    assert_true(any("at least one" in e for e in hero.validate_library_manifest(m)), str(hero.validate_library_manifest(m)))


def test_duplicate_heavy_library_warns():
    m = {"entries": [{}, {}, {}], "selection": {"candidate_count": 10, "near_duplicate_rejections": 7}}
    assert_true(any("duplicate-heavy" in w for w in hero.library_warnings(m)), str(hero.library_warnings(m)))


def snapshot(result="PASS", runs=0, source_sha="a" * 64):
    return {
        "schema": qc.SNAPSHOT_SCHEMA,
        "runtime_seconds": 120.0,
        "export_variety": {"result": result, "similar_runs_count": runs, "metrics": {"mean_adjacent_similarity": .8}},
        "black_freeze": {"result": "PASS"},
        "framing_aspect": {"result": "PASS"},
        "audio_sync": {"result": "PASS"},
        "continuity_warnings": [],
        "mode_aware_qc": {"result": "PASS"},
        "source_canon_integrity": {"result": "PASS", "source_library_sha256": source_sha},
    }


def test_before_after_qc_evidence():
    data = qc.compare_snapshots(snapshot("REVIEW", 3), snapshot("PASS", 0))
    assert_true(data["comparison"]["similar_runs_delta"] == -3, str(data))
    assert_true(not qc.validate_comparison(data, "a" * 64), str(qc.validate_comparison(data, "a" * 64)))


def test_canon_integrity_hash_required():
    data = qc.compare_snapshots(snapshot("REVIEW", 1), snapshot("PASS", 0, "b" * 64))
    errs = qc.validate_comparison(data, "a" * 64)
    assert_true(any("hash does not match" in e for e in errs), str(errs))


def test_project_local_fx_requires_proof_and_lock():
    if fx is None:
        return
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        impl = root / "impl.py"; impl.write_text("print('fx')\n")
        inp = root / "in.dat"; inp.write_text("input")
        proof = root / "proof.dat"; proof.write_text("changed pixels")
        manifest = {
            "schema": fx.SCHEMA,
            "scope": "project_local",
            "effect_id": "local_fx",
            "technology_label": "project-local image transform",
            "truthful_naming": True,
            "placeholder": False,
            "promoted_to_canonical": False,
            "implementation": {"path": "impl.py", "sha256": fx.sha256_file(impl)},
            "render_inputs": [{"path": "in.dat", "sha256": fx.sha256_file(inp)}],
            "deterministic_applicable": True,
            "parameters": {"amount": .2},
            "deterministic_parameters": True,
            "proof": {"path": "proof.dat", "sha256": fx.sha256_file(proof), "visible_pixel_change": True},
            "qc": {"status": "PASS", "reviewer": "agent:test"},
        }
        p = root / "local.json"; p.write_text(json.dumps(manifest))
        assert_true(not fx.validate_manifest(manifest, root), str(fx.validate_manifest(manifest, root)))
        lock = fx.make_lock(p, root); lp = root / "local.lock.json"; lp.write_text(json.dumps(lock))
        assert_true(not fx.validate_lock(p, lp, root), str(fx.validate_lock(p, lp, root)))
        manifest["proof"]["visible_pixel_change"] = False
        assert_true(any("visible_pixel_change" in e for e in fx.validate_manifest(manifest, root)), "missing proof failure")


def main():
    tests = [
        test_accepted_source_library_valid_and_timeline_editable,
        test_source_library_hash_and_reuse_authorization_required,
        test_baseline_semantics_are_separate,
        test_recut_scope_blocks_source_replacement,
        test_source_derived_provenance_matches_canon,
        test_backend_substitution_requires_equivalence,
        test_backend_substitution_with_equivalence_passes,
        test_hero_manifest_valid_and_nonempty,
        test_empty_hero_library_fails,
        test_duplicate_heavy_library_warns,
        test_before_after_qc_evidence,
        test_canon_integrity_hash_required,
        test_project_local_fx_requires_proof_and_lock,
    ]
    for t in tests:
        t()
        print("PASS", t.__name__)
    print(f"Recut system regression tests: PASS ({len(tests)} tests)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
