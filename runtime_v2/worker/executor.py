"""Safe process execution in a disposable job workspace."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import time
import uuid

from .registry import ToolRegistry


@dataclass(frozen=True)
class Artifact:
    path: str
    size_bytes: int
    sha256: str


@dataclass(frozen=True)
class ExecutionResult:
    job_id: str
    tool: str
    exit_code: int | None
    timed_out: bool
    duration_ms: float
    stdout: str
    stderr: str
    output_truncated: bool
    artifacts: tuple[Artifact, ...]


class ToolExecutor:
    def __init__(
        self,
        *,
        registry: ToolRegistry,
        workspace_root: str,
        default_timeout_seconds: float,
        max_output_bytes: int,
        keep_workspaces: bool = False,
    ):
        self.registry = registry
        self.workspace_root = Path(workspace_root).expanduser().resolve()
        self.default_timeout_seconds = default_timeout_seconds
        self.max_output_bytes = max_output_bytes
        self.keep_workspaces = keep_workspaces

    def run(
        self,
        *,
        tool: str,
        args: list[str] | None = None,
        timeout_seconds: float | None = None,
    ) -> ExecutionResult:
        user_args = list(args or [])
        command = self.registry.require_command(tool, user_args)
        timeout = min(
            timeout_seconds or self.default_timeout_seconds,
            self.default_timeout_seconds,
        )
        job_id = str(uuid.uuid4())
        workspace = self._create_workspace(job_id)
        started = time.perf_counter()

        exit_code: int | None = None
        timed_out = False
        stdout = b""
        stderr = b""

        try:
            process = subprocess.Popen(
                command,
                cwd=workspace,
                env=self._safe_environment(),
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False,
                close_fds=(os.name != "nt"),
            )
            try:
                stdout, stderr = process.communicate(timeout=timeout)
                exit_code = process.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
                process.kill()
                stdout, stderr = process.communicate()
                exit_code = process.returncode

            artifacts = tuple(self._artifacts(workspace))
            out_text, err_text, truncated = self._bounded_output(stdout, stderr)
            return ExecutionResult(
                job_id=job_id,
                tool=tool,
                exit_code=exit_code,
                timed_out=timed_out,
                duration_ms=round((time.perf_counter() - started) * 1000.0, 3),
                stdout=out_text,
                stderr=err_text,
                output_truncated=truncated,
                artifacts=artifacts,
            )
        finally:
            if not self.keep_workspaces:
                shutil.rmtree(workspace, ignore_errors=True)

    def _create_workspace(self, job_id: str) -> Path:
        self.workspace_root.mkdir(parents=True, exist_ok=True)
        workspace = (self.workspace_root / job_id).resolve()
        if self.workspace_root not in workspace.parents:
            raise RuntimeError("Resolved workspace escaped configured root.")
        workspace.mkdir(mode=0o700)
        return workspace

    def _safe_environment(self) -> dict[str, str]:
        allowed = {
            "PATH",
            "SystemRoot",
            "WINDIR",
            "COMSPEC",
            "PATHEXT",
            "TEMP",
            "TMP",
            "LANG",
            "LC_ALL",
        }
        env = {key: value for key, value in os.environ.items() if key in allowed}
        env["PYTHONNOUSERSITE"] = "1"
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["GIT_CONFIG_NOSYSTEM"] = "1"
        if os.name != "nt":
            env["GIT_CONFIG_GLOBAL"] = "/dev/null"
        return env

    def _bounded_output(self, stdout: bytes, stderr: bytes) -> tuple[str, str, bool]:
        remaining = self.max_output_bytes
        out_piece = stdout[:remaining]
        remaining -= len(out_piece)
        err_piece = stderr[:remaining]
        truncated = len(out_piece) < len(stdout) or len(err_piece) < len(stderr)
        return (
            out_piece.decode("utf-8", errors="replace"),
            err_piece.decode("utf-8", errors="replace"),
            truncated,
        )

    def _artifacts(self, workspace: Path) -> list[Artifact]:
        found: list[Artifact] = []
        for path in sorted(workspace.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(workspace).as_posix()
            found.append(
                Artifact(
                    path=relative,
                    size_bytes=path.stat().st_size,
                    sha256=_sha256(path),
                )
            )
        return found


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()
