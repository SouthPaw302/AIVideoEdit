"""Static registry for commands the remote worker is allowed to execute."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import sys
from typing import Callable, Sequence


ArgValidator = Callable[[Sequence[str]], tuple[bool, str | None]]


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    executable: str | None
    fixed_args: tuple[str, ...] = ()
    accepts_user_args: bool = False
    validate_args: ArgValidator | None = None

    @property
    def available(self) -> bool:
        return bool(self.executable)


class ToolRegistry:
    def __init__(self, specs: Sequence[ToolSpec]):
        self._specs = {spec.name: spec for spec in specs}

    def get(self, name: str) -> ToolSpec | None:
        return self._specs.get(name)

    def all(self) -> list[ToolSpec]:
        return [self._specs[name] for name in sorted(self._specs)]

    def require_command(self, name: str, user_args: Sequence[str]) -> list[str]:
        spec = self.get(name)
        if spec is None:
            raise UnknownToolError(f"Tool is not registered: {name}")
        if not spec.available:
            raise ToolUnavailableError(f"Tool is not installed on this worker: {name}")
        if user_args and not spec.accepts_user_args:
            raise UnsafeArgumentsError(f"Tool does not accept user arguments: {name}")
        if spec.validate_args is not None:
            ok, detail = spec.validate_args(user_args)
            if not ok:
                raise UnsafeArgumentsError(detail or "Arguments were rejected.")
        return [spec.executable, *spec.fixed_args, *user_args]


class ToolRegistryError(ValueError):
    pass


class UnknownToolError(ToolRegistryError):
    pass


class ToolUnavailableError(ToolRegistryError):
    pass


class UnsafeArgumentsError(ToolRegistryError):
    pass


def _which(command: str) -> str | None:
    return shutil.which(command)


def build_default_registry() -> ToolRegistry:
    probe = str(Path(__file__).with_name("probe.py").resolve())
    return ToolRegistry(
        [
            ToolSpec(
                name="runtime.python.version",
                description="Report the worker Python interpreter version.",
                executable=sys.executable,
                fixed_args=("--version",),
            ),
            ToolSpec(
                name="runtime.python.probe",
                description="Run the built-in isolated workspace diagnostic.",
                executable=sys.executable,
                fixed_args=(probe,),
            ),
            ToolSpec(
                name="system.git.version",
                description="Report the installed Git version.",
                executable=_which("git"),
                fixed_args=("--version",),
            ),
            ToolSpec(
                name="system.ffmpeg.version",
                description="Report the installed FFmpeg version.",
                executable=_which("ffmpeg"),
                fixed_args=("-version",),
            ),
            ToolSpec(
                name="system.ffprobe.version",
                description="Report the installed FFprobe version.",
                executable=_which("ffprobe"),
                fixed_args=("-version",),
            ),
        ]
    )
