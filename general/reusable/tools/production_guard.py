#!/usr/bin/env python3
"""Fail-closed AIVideoEdit production-state validator.

Normal mode requires a valid bootstrap session attestation. The portable
bootstrap invokes `--bootstrap-phase` once to validate the active branch using
the freshly materialized current-main OS; only then is a session attestation
written.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

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
MEDIA_PATH = OS_ROOT / "general/reusable/MEDIA_CAPABILITY_MATRIX.json"
SESSION_PATH = ROOT / ".aivideoedit/session.json"


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        try:
            display = path.relative_to(ROOT)
        except ValueError:
            display = path
        raise SystemExit(f"FAIL: missing {display}")
    except Exception as e:
        try:
            display = path.relative_to(ROOT)
        except ValueError:
            display = path
        raise SystemExit(f"FAIL: invalid JSON {display}: {e}")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def truthy(v):
    return v is True


def fail(msg, errors):
    errors.append(msg)


def discover_project():
    env = os.environ.get("AIVIDEOEDIT_PROJECT_DIR")
    if env:
        p = Path(env)
        return p if p.is_absolute() else ROOT / p
    candidates = [p.parent for p in ROOT.glob("projects/*/PROJECT_STATE.json")]
    if len(candidates) == 1:
        return candidates[0]
    if not candidates:
        raise SystemExit("FAIL: no projects/*/PROJECT_STATE.json found")
    raise SystemExit("FAIL: multiple project states found; set AIVIDEOEDIT_PROJECT_DIR")


def verify_bootstrap_session(branch: str):
    if not SESSION_PATH.is_file():
        return [
            "bootstrap session missing; run `python bootstrap.py boot --repo-root <repo>` before production work"
        ]
    session = load_json(SESSION_PATH)
    errors = []
    if session.get("schema") != "aivideoedit.session.v1":
        fail("invalid bootstrap session schema", errors)
    if session.get("guard_result") != "PASS":
        fail("bootstrap session does not contain guard_result=PASS", errors)
    if session.get("branch") != branch:
        fail(f"bootstrap branch mismatch: {session.get('branch')} != {branch}", errors)

    os_root = Path(session.get("os_root") or "")
    if not os_root.is_absolute():
        os_root = (ROOT / os_root).resolve()
    if not os_root.is_dir():
        fail(f"bootstrapped OS root missing: {os_root}", errors)
        return errors

    recorded = session.get("os_files", {})
    critical = [
        "AGENTS.md",
        "SOUL.md",
        "general/reusable/PRODUCTION_CONTRACT.json",
        "general/reusable/MEDIA_CAPABILITY_MATRIX.json",
        "general/reusable/tools/production_guard.py",
        "general/reusable/fx_v2/registry.json",
    ]
    for rel in critical:
        p = os_root / rel
        expected = recorded.get(rel)
        if not p.is_file():
            fail(f"bootstrapped OS file missing: {rel}", errors)
        elif not expected:
            fail(f"bootstrap attestation missing hash for: {rel}", errors)
        elif sha256_file(p) != expected:
            fail(f"bootstrapped OS file changed after attestation: {rel}", errors)

    os_guard = os_root / "general/reusable/tools/production_guard.py"
    if os_guard.is_file():
        this_hash = sha256_file(Path(__file__).resolve())
        os_hash = sha256_file(os_guard)
        if this_hash != os_hash and Path(__file__).resolve() != os_guard.resolve():
            fail(
                "stale branch production_guard.py invoked; run the guard from "
                ".aivideoedit/os/general/reusable/tools/production_guard.py",
                errors,
            )
    return errors


def validate(branch: str):
    contract = load_json(CONTRACT_PATH)
    media = load_json(MEDIA_PATH)
    errors = []

    if branch == "main":
        for p in [
            "AGENTS.md",
            "SOUL.md",
            "BIBLE.md",
            "SYSTEM_INDEX.md",
            "general/reusable/AIVIDEOEDIT_OS_MANIFEST.json",
            "general/reusable/PRODUCTION_PIPELINE.md",
            "general/reusable/STYLE_CONTRACT.md",
            "general/reusable/fx_v2/registry.json",
        ]:
            if not (OS_ROOT / p).is_file():
                fail(f"missing system file: {p}", errors)
        return errors

    if not branch.startswith("song/"):
        return [f"production work must use song/<slug>; got {branch}"]

    project = discover_project()
    for name in contract["required_project_files"]:
        if not (project / name).is_file():
            fail(f"missing required project file: {project.relative_to(ROOT)}/{name}", errors)
    if errors:
        return errors

    state = load_json(project / "PROJECT_STATE.json")
    auth = load_json(project / "SOURCE_AUTHORITY.json")
    refs = load_json(project / "REFERENCE_MANIFEST.json")
    plan = load_json(project / "MEDIA_PLAN.json")
    states = contract["states"]
    stage = state.get("stage")
    if stage not in states:
        return [f"invalid production stage: {stage}"]

    expected_branch = state.get("branch")
    if expected_branch and expected_branch != branch:
        fail(f"PROJECT_STATE branch mismatch: {expected_branch} != {branch}", errors)

    for denied in contract["default_denied_sources"]:
        if (
            auth.get("allow", {}).get(denied) is True
            and denied not in auth.get("explicit_user_authorizations", [])
        ):
            fail(f"historical source enabled without explicit user authorization: {denied}", errors)

    idx = states.index(stage)

    def at(name):
        return idx >= states.index(name)

    if at("SOURCE_INGESTED") and not truthy(state.get("source_ingest_complete")):
        fail("SOURCE_INGESTED requires source_ingest_complete=true", errors)

    videos = refs.get("videos", [])
    images = refs.get("images", [])

    if at("REFERENCES_ANALYZED"):
        if not truthy(state.get("reference_analysis_complete")):
            fail("reference analysis not complete", errors)
        for v in videos:
            dur = float(v.get("duration_seconds", 0))
            total = int(v.get("total_frames", 0))
            ext = int(v.get("extracted_frames", 0))
            policy = v.get("extraction_policy")
            short = (
                dur <= contract["reference_policy"]["short_video_max_seconds"]
                and total <= contract["reference_policy"]["short_video_max_frames"]
            )
            if short and (policy != "all_frames" or ext != total):
                fail(
                    f"short reference must extract all frames: "
                    f"{v.get('name', 'video')} {ext}/{total}",
                    errors,
                )
            if not short:
                if policy != "meaningful_sampling":
                    fail(
                        f"long reference requires meaningful_sampling: {v.get('name', 'video')}",
                        errors,
                    )
                if ext <= 0 or not v.get("sampling_description") or not v.get("coverage"):
                    fail(
                        f"long reference sampling evidence incomplete: {v.get('name', 'video')}",
                        errors,
                    )
            if not truthy(v.get("analysis_complete")):
                fail(f"reference video analysis incomplete: {v.get('name', 'video')}", errors)
        for im in images:
            if not truthy(im.get("analysis_complete")):
                fail(f"source image analysis incomplete: {im.get('name', 'image')}", errors)

    if at("APPROACH_ESTABLISHED"):
        selected = plan.get("selected_capabilities", [])
        valid = {x["id"] for x in media["capabilities"]}
        unknown = [x for x in selected if x not in valid]
        if not selected:
            fail("MEDIA_PLAN selected_capabilities is empty", errors)
        if unknown:
            fail("unknown media capabilities: " + ", ".join(unknown), errors)
        if not truthy(state.get("visual_approach_established")):
            fail("visual/media approach not established", errors)
        if not videos and not images and not truthy(plan.get("user_approach_established")):
            fail(
                "no-reference production requires user_approach_established=true "
                "before generated media",
                errors,
            )

    checks = {
        "STORYBOARD_LOCKED": "storyboard_locked",
        "SHOT_PACKAGES_BUILT": "shot_packages_built",
        "SHOT_PROOFS_ACCEPTED": "shot_proofs_accepted",
        "FX_LOCKED": "fx_lock_verified",
        "ASSEMBLED": "assembly_complete",
        "FINAL_QC_PASSED": "final_qc_passed",
        "ARCHIVED": "archive_complete",
    }
    for s, key in checks.items():
        if at(s) and not truthy(state.get(key)):
            fail(f"{s} requires {key}=true", errors)

    if at("FX_LOCKED") and not (project / "fx.lock.json").is_file():
        fail("FX_LOCKED requires fx.lock.json", errors)

    if at("SHOT_PACKAGES_BUILT"):
        sp = project / "shot_packages"
        packages = [p for p in sp.iterdir() if p.is_dir()] if sp.is_dir() else []
        if not packages:
            fail("SHOT_PACKAGES_BUILT requires at least one shot package", errors)

    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--branch",
        default=os.environ.get("GITHUB_REF_NAME")
        or os.environ.get("AIVIDEOEDIT_BRANCH")
        or "",
    )
    ap.add_argument(
        "--bootstrap-phase",
        action="store_true",
        help="validate state before the bootstrap session attestation exists",
    )
    args = ap.parse_args()

    if not args.branch:
        raise SystemExit("FAIL: branch required (--branch or GITHUB_REF_NAME)")

    errors = []
    if not args.bootstrap_phase and os.environ.get("AIVIDEOEDIT_BOOTSTRAP_PHASE") != "1":
        errors.extend(verify_bootstrap_session(args.branch))
        if errors:
            print("AIVideoEdit production contract: FAIL", file=sys.stderr)
            for e in errors:
                print("- " + e, file=sys.stderr)
            raise SystemExit(1)

        session = load_json(SESSION_PATH)
        os_root = Path(session.get("os_root") or "")
        if not os_root.is_absolute():
            os_root = (ROOT / os_root).resolve()
        os.environ["AIVIDEOEDIT_OS_ROOT"] = str(os_root)

    errors.extend(validate(args.branch))
    if errors:
        print("AIVideoEdit production contract: FAIL", file=sys.stderr)
        for e in errors:
            print("- " + e, file=sys.stderr)
        raise SystemExit(1)

    print("AIVideoEdit production contract: PASS")


if __name__ == "__main__":
    main()
