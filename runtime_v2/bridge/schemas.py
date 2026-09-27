"""Strict API schemas."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class HealthResponse(StrictModel):
    status: Literal["ok"]
    service: str
    version: str


class VersionResponse(StrictModel):
    service: str
    service_version: str
    api_version: str
    runtime: Literal["runtime_v2"] = "runtime_v2"


class Capability(StrictModel):
    name: str = Field(min_length=1)
    status: Literal["ready", "planned"]
    description: str = Field(min_length=1)


class CapabilitiesResponse(StrictModel):
    service: str
    api_version: str
    capabilities: list[Capability]


class ToolDescriptor(StrictModel):
    name: str
    description: str
    available: bool
    accepts_user_args: bool = False


class ToolsResponse(StrictModel):
    tools: list[ToolDescriptor]


class ToolRunRequest(StrictModel):
    tool: str = Field(min_length=1, max_length=128)
    args: list[str] = Field(default_factory=list, max_length=32)
    timeout_seconds: float | None = Field(default=None, gt=0, le=120)


class ArtifactDigest(StrictModel):
    path: str
    size_bytes: int = Field(ge=0)
    sha256: str


class ToolRunResponse(StrictModel):
    job_id: str
    tool: str
    exit_code: int | None
    timed_out: bool
    duration_ms: float
    stdout: str
    stderr: str
    output_truncated: bool
    artifacts: list[ArtifactDigest]


class ErrorResponse(StrictModel):
    error: str
    detail: str
    request_id: str
