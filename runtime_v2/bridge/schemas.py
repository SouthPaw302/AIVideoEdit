"""Strict API response schemas."""

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


class ErrorResponse(StrictModel):
    error: str
    detail: str
    request_id: str
