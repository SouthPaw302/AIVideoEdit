#!/usr/bin/env python3
"""AIVideoEdit portable OS bootstrap.

Every new agent/session starts here.

The bootstrap materializes the *entire current main branch* into an ephemeral
`.aivideoedit/os/` sandbox-local runtime, runs that current-main production
guard against the active working branch, then writes:
  - `.aivideoedit/session.json`      immutable session attestation
  - `.aivideoedit/SECOND_BRAIN.md`   generated branch/session working context

No production authority is duplicated here. GitHub `main` remains the OS.
Stdlib only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import urllib.request
import uuid
from pathlib import Path

REPOSITORY = "SouthPaw302/AIVideoEdit"
DEFAULT_REF = "main"
API_MAIN = f"https://api.github.com/repos/{REPOSITORY}/commits/{DEFAULT_REF}"
SESSION_DIRNAME = ".aivideoedit"
SESSION_SCHEMA = "aivideoedit.session.v1"
MANIFEST_PATH = "general/reusable/AIVIDEOEDIT_OS_MANIFEST.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def http_bytes(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "AIVideoEdit-bootstrap/1",
            "Accept": "application/vnd.github+json, application/octet-stream;q=0.9, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def git(repo: Path, *args: str) -> str:
    try:
        p = subprocess.run(
            ["git", "-C", str(repo), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except FileNotFoundError:
        return ""
    return p.stdout.strip() if p.returncode == 0 else ""


def find_repo_root(start: Path | None = None) -> Path:
    env = os.environ.get("AIVIDEOEDIT_REPO_ROOT")
    if env:
        p = Path(env).expanduser().resolve()
        if p.is_dir():
            return p
    p = (start or Path.cwd()).expanduser().resolve()
    for cur in [p, *p.parents]:
        if (cur / "README.md").is_file() and (cur / "general/reusable").is_dir():
            return cur
    raise SystemExit("BOOTSTRAP FAIL: AIVideoEdit repository root not found. Use --repo-root.")


def detect_branch(repo: Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    for key in ("AIVIDEOEDIT_BRANCH", "GITHUB_HEAD_REF", "GITHUB_REF_NAME"):
        if os.environ.get(key):
            return os.environ[key]
    branch = git(repo, "branch", "--show-current")
    if branch:
        return branch
    raise SystemExit("BOOTSTRAP FAIL: branch cannot be determined. Use --branch.")


def detect_project_dir(repo: Path, branch: str, explicit: str | None) -> Path | None:
    if explicit:
        p = Path(explicit)
        return p.resolve() if p.is_absolute() else (repo / p).resolve()
    env = os.environ.get("AIVIDEOEDIT_PROJECT_DIR")
    if env:
        p = Path(env)
        return p.resolve() if p.is_absolute() else (repo / p).resolve()
    if branch.startswith("song/"):
        slug = branch.split("/", 1)[1]
        exact = repo / "projects" / slug
        if (exact / "PROJECT_STATE.json").is_file():
            return exact
    candidates = [p.parent for p in (repo / "projects").glob("*/PROJECT_STATE.json")]
    return candidates[0] if len(candidates) == 1 else None


def fetch_main_sha(offline: bool, repo: Path) -> tuple[str, str]:
    if not offline:
        try:
            data = json.loads(http_bytes(API_MAIN).decode("utf-8"))
            sha = str(data.get("sha") or "")
            if sha:
                return sha, "github-main"
        except Exception as e:
            print(f"BOOTSTRAP: GitHub main lookup unavailable ({e}); trying local origin/main.", file=sys.stderr)
    sha = git(repo, "rev-parse", "origin/main") or git(repo, "rev-parse", "main")
    if sha:
        return sha, "local-git-main"
    raise SystemExit("BOOTSTRAP FAIL: cannot establish authoritative main commit.")


def safe_extract_tar(tf: tarfile.TarFile, dest: Path, strip_first_component: bool) -> None:
    dest = dest.resolve()
    for member in tf.getmembers():
        parts = Path(member.name).parts
        if strip_first_component:
            if len(parts) <= 1:
                continue
            rel = Path(*parts[1:])
        else:
            rel = Path(*parts)
        if not rel.parts:
            continue
        target = (dest / rel).resolve()
        if target != dest and dest not in target.parents:
            raise SystemExit(f"BOOTSTRAP FAIL: unsafe archive member: {member.name}")
        if member.isdir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        if not member.isfile():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        src = tf.extractfile(member)
        if src is None:
            continue
        target.write_bytes(src.read())


def materialize_entire_main(repo: Path, os_root: Path, main_sha: str, offline: bool) -> str:
    """Materialize the entire exact main commit into the ephemeral OS root."""
    if offline:
        try:
            p = subprocess.run(
                ["git", "-C", str(repo), "archive", "--format=tar", main_sha],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
        except FileNotFoundError:
            raise SystemExit("BOOTSTRAP FAIL: --offline requires git.")
        if p.returncode != 0:
            raise SystemExit("BOOTSTRAP FAIL: git archive of authoritative main failed.")
        with tarfile.open(fileobj=io.BytesIO(p.stdout), mode="r:") as tf:
            safe_extract_tar(tf, os_root, strip_first_component=False)
        return "git-archive"

    url = f"https://codeload.github.com/{REPOSITORY}/tar.gz/{main_sha}"
    try:
        data = http_bytes(url, timeout=90)
    except Exception as e:
        raise SystemExit(
            f"BOOTSTRAP FAIL: exact current-main OS download failed: {e}. "
            "Use --offline only when local origin/main is trusted/current."
        )
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        safe_extract_tar(tf, os_root, strip_first_component=True)
    return "github-archive"


def load_os_manifest(os_root: Path) -> tuple[dict, bytes]:
    path = os_root / MANIFEST_PATH
    if not path.is_file():
        raise SystemExit(f"BOOTSTRAP FAIL: current main lacks {MANIFEST_PATH}")
    data = path.read_bytes()
    try:
        manifest = json.loads(data.decode("utf-8"))
    except Exception as e:
        raise SystemExit(f"BOOTSTRAP FAIL: invalid OS manifest: {e}")
    return manifest, data


def attest_manifest_files(os_root: Path, manifest: dict) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for rec in manifest.get("files", []):
        rel = rec["path"] if isinstance(rec, dict) else rec
        p = os_root / rel
        if not p.is_file():
            raise SystemExit(f"BOOTSTRAP FAIL: OS manifest file missing from main snapshot: {rel}")
        hashes[rel] = sha256_file(p)
    return hashes


def run_bootstrap_guard(repo: Path, os_root: Path, branch: str, project: Path | None) -> None:
    guard = os_root / "general/reusable/tools/production_guard.py"
    if not guard.is_file():
        raise SystemExit("BOOTSTRAP FAIL: canonical production_guard.py missing from current main.")
    env = os.environ.copy()
    env["AIVIDEOEDIT_REPO_ROOT"] = str(repo)
    env["AIVIDEOEDIT_OS_ROOT"] = str(os_root)
    env["AIVIDEOEDIT_BOOTSTRAP_PHASE"] = "1"
    if project:
        env["AIVIDEOEDIT_PROJECT_DIR"] = str(project.relative_to(repo))
    p = subprocess.run(
        [sys.executable, str(guard), "--branch", branch, "--bootstrap-phase"],
        env=env,
        text=True,
        check=False,
    )
    if p.returncode != 0:
        raise SystemExit("BOOTSTRAP FAIL: current-main production contract rejected this workspace.")


def read_json_if(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def next_stage(contract: dict, stage: str | None) -> str:
    states = contract.get("states", [])
    if stage in states:
        i = states.index(stage)
        return states[i + 1] if i + 1 < len(states) else "COMPLETE"
    return states[0] if states else "UNKNOWN"


def build_second_brain(repo: Path, os_root: Path, branch: str, project: Path | None, main_sha: str, session_id: str) -> str:
    contract = read_json_if(os_root / "general/reusable/PRODUCTION_CONTRACT.json")
    lines = [
        "# AIVideoEdit Session Second Brain",
        "",
        "> Generated by `bootstrap.py`. Ephemeral working context; never a separate authority.",
        "",
        f"- Session: `{session_id}`",
        f"- Current-main OS commit: `{main_sha}`",
        f"- Active branch: `{branch}`",
    ]
    if not project:
        lines += [
            "- Active production: none detected",
            "",
            "## Authority",
            "Current explicit user instruction -> current-main AIVideoEdit OS.",
            "Do not infer production identity, story, media, or continuity from history.",
        ]
        return "\n".join(lines) + "\n"

    state = read_json_if(project / "PROJECT_STATE.json")
    auth = read_json_if(project / "SOURCE_AUTHORITY.json")
    plan = read_json_if(project / "MEDIA_PLAN.json")
    refs = read_json_if(project / "REFERENCE_MANIFEST.json")
    stage = state.get("stage")
    allow = [k for k, v in auth.get("allow", {}).items() if v is True]
    deny = [k for k, v in auth.get("allow", {}).items() if v is False]
    lines += [
        f"- Project directory: `{project.relative_to(repo).as_posix()}`",
        f"- Production stage: `{stage or 'UNKNOWN'}`",
        f"- Next contract stage: `{next_stage(contract, stage)}`",
        "",
        "## Source authority snapshot",
        "Allowed: " + (", ".join(allow) if allow else "none recorded"),
        "",
        "Denied: " + (", ".join(deny) if deny else "none recorded"),
        "",
        "Explicit historical authorizations: " + (", ".join(auth.get("explicit_user_authorizations", [])) or "none"),
        "",
        "## Media plan",
        "Selected capabilities: " + (", ".join(plan.get("selected_capabilities", [])) or "not established"),
        "",
        "## Reference inventory",
        f"- Videos: {len(refs.get('videos', []))}",
        f"- Images: {len(refs.get('images', []))}",
        "",
        "## Session rule",
        "Do not advance stage, generate media, select FX, assemble, or claim QC from memory. Use active branch evidence and the current-main OS. Re-run the bootstrapped guard before stage-changing work.",
    ]
    return "\n".join(lines) + "\n"


def write_session(repo: Path, os_root: Path, branch: str, project: Path | None, main_sha: str, os_source: str, archive_source: str, manifest_hash: str, file_hashes: dict[str, str]) -> Path:
    session_dir = repo / SESSION_DIRNAME
    session_id = str(uuid.uuid4())
    rec = {
        "schema": SESSION_SCHEMA,
        "session_id": session_id,
        "started_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "repository": REPOSITORY,
        "branch": branch,
        "project_dir": project.relative_to(repo).as_posix() if project else None,
        "os_main_commit": main_sha,
        "os_source": os_source,
        "archive_source": archive_source,
        "os_root": str(os_root),
        "manifest_sha256": manifest_hash,
        "os_files": file_hashes,
        "guard_result": "PASS",
    }
    path = session_dir / "session.json"
    path.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (session_dir / "SECOND_BRAIN.md").write_text(build_second_brain(repo, os_root, branch, project, main_sha, session_id), encoding="utf-8")
    return path


def boot(args: argparse.Namespace) -> int:
    repo = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    branch = detect_branch(repo, args.branch)
    project = detect_project_dir(repo, branch, args.project_dir)
    session_dir = repo / SESSION_DIRNAME
    os_root = session_dir / "os"

    if session_dir.exists():
        shutil.rmtree(session_dir)
    os_root.mkdir(parents=True, exist_ok=True)

    main_sha, os_source = fetch_main_sha(args.offline, repo)
    archive_source = materialize_entire_main(repo, os_root, main_sha, args.offline)
    manifest, manifest_bytes = load_os_manifest(os_root)
    file_hashes = attest_manifest_files(os_root, manifest)
    run_bootstrap_guard(repo, os_root, branch, project)
    session_path = write_session(repo, os_root, branch, project, main_sha, os_source, archive_source, sha256_bytes(manifest_bytes), file_hashes)

    print("AIVideoEdit OS BOOTSTRAP: PASS")
    print(f"main={main_sha}")
    print(f"branch={branch}")
    print(f"os={os_root}")
    print(f"session={session_path}")
    print(f"second_brain={session_dir / 'SECOND_BRAIN.md'}")
    if project:
        print(f"project={project.relative_to(repo)}")
    return 0


def status(args: argparse.Namespace) -> int:
    repo = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    path = repo / SESSION_DIRNAME / "session.json"
    if not path.is_file():
        raise SystemExit("AIVideoEdit OS SESSION: MISSING — run `python bootstrap.py boot`.")
    print(path.read_text(encoding="utf-8"))
    return 0


def install(args: argparse.Namespace) -> int:
    """Install a clean main checkout in a sandbox that has no repository yet."""
    dst = Path(args.workspace).expanduser().resolve()
    if dst.exists() and any(dst.iterdir()):
        raise SystemExit(f"INSTALL FAIL: workspace is not empty: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)

    if shutil.which("git"):
        p = subprocess.run(["git", "clone", "--branch", DEFAULT_REF, "--single-branch", f"https://github.com/{REPOSITORY}.git", str(dst)], check=False)
        if p.returncode != 0:
            raise SystemExit("INSTALL FAIL: git clone failed.")
    else:
        data = http_bytes(f"https://codeload.github.com/{REPOSITORY}/tar.gz/refs/heads/{DEFAULT_REF}", timeout=90)
        dst.mkdir(parents=True, exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
            safe_extract_tar(tf, dst, strip_first_component=True)

    print(f"AIVideoEdit installed at {dst}")
    print(f"Next: {sys.executable} {dst/'bootstrap.py'} boot --repo-root {dst}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="AIVideoEdit portable OS bootstrap")
    sub = ap.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("boot", help="load exact current-main OS and attest this session")
    b.add_argument("--repo-root")
    b.add_argument("--branch")
    b.add_argument("--project-dir")
    b.add_argument("--offline", action="store_true", help="materialize exact local origin/main via git archive instead of GitHub")
    b.set_defaults(func=boot)

    s = sub.add_parser("status", help="show current session attestation")
    s.add_argument("--repo-root")
    s.set_defaults(func=status)

    i = sub.add_parser("install", help="install AIVideoEdit main into an empty sandbox")
    i.add_argument("--workspace", required=True)
    i.set_defaults(func=install)

    args = ap.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
