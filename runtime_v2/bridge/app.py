"""FastAPI application for the Runtime V2 Remote Agent Bridge."""

from __future__ import annotations

import asyncio
import logging

from fastapi import FastAPI, HTTPException, Query, Request

from .capabilities import list_capabilities
from .config import BridgeSettings
from .middleware import BridgeMiddleware
from .schemas import (
    ArtifactDigest,
    CapabilitiesResponse,
    HealthResponse,
    ToolDescriptor,
    ToolRunRequest,
    ToolRunResponse,
    ToolsResponse,
    VersionResponse,
)
from runtime_v2.worker import ToolExecutor, build_default_registry
from runtime_v2.intelligence_api import router as intelligence_router
from runtime_v2.production_proxy import router as production_proxy_router
from runtime_v2.worker.registry import ToolRegistryError


def create_app(settings: BridgeSettings | None = None) -> FastAPI:
    resolved = settings or BridgeSettings.from_env()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    registry = build_default_registry()
    executor = ToolExecutor(
        registry=registry,
        workspace_root=resolved.workspace_root,
        default_timeout_seconds=resolved.execution_timeout_seconds,
        max_output_bytes=resolved.max_output_bytes,
        keep_workspaces=resolved.keep_workspaces,
    )

    app = FastAPI(
        title="AIVideoEdit Agent Bridge",
        version=resolved.service_version,
        docs_url="/docs",
        redoc_url=None,
        openapi_url="/openapi.json",
    )
    app.state.settings = resolved
    app.state.tool_registry = registry
    app.state.tool_executor = executor
    app.include_router(intelligence_router)
    app.include_router(production_proxy_router)
    app.add_middleware(BridgeMiddleware, settings=resolved)

    @app.get("/health", response_model=HealthResponse, tags=["bridge"])
    async def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            service=resolved.service_name,
            version=resolved.service_version,
        )

    @app.get("/version", response_model=VersionResponse, tags=["bridge"])
    async def version() -> VersionResponse:
        return VersionResponse(
            service=resolved.service_name,
            service_version=resolved.service_version,
            api_version=resolved.api_version,
        )

    @app.get("/capabilities", response_model=CapabilitiesResponse, tags=["bridge"])
    async def capabilities(
        include_planned: bool = Query(default=True),
    ) -> CapabilitiesResponse:
        return CapabilitiesResponse(
            service=resolved.service_name,
            api_version=resolved.api_version,
            capabilities=list_capabilities(include_planned=include_planned),
        )

    @app.get("/tools", response_model=ToolsResponse, tags=["tools"])
    async def tools(request: Request) -> ToolsResponse:
        registry = request.app.state.tool_registry
        return ToolsResponse(
            tools=[
                ToolDescriptor(
                    name=spec.name,
                    description=spec.description,
                    available=spec.available,
                    accepts_user_args=spec.accepts_user_args,
                )
                for spec in registry.all()
            ]
        )

    @app.post("/tools/run", response_model=ToolRunResponse, tags=["tools"])
    async def run_tool(payload: ToolRunRequest, request: Request) -> ToolRunResponse:
        executor = request.app.state.tool_executor
        try:
            result = await asyncio.to_thread(
                executor.run,
                tool=payload.tool,
                args=payload.args,
                timeout_seconds=payload.timeout_seconds,
            )
        except ToolRegistryError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

        return ToolRunResponse(
            job_id=result.job_id,
            tool=result.tool,
            exit_code=result.exit_code,
            timed_out=result.timed_out,
            duration_ms=result.duration_ms,
            stdout=result.stdout,
            stderr=result.stderr,
            output_truncated=result.output_truncated,
            artifacts=[
                ArtifactDigest(
                    path=item.path,
                    size_bytes=item.size_bytes,
                    sha256=item.sha256,
                )
                for item in result.artifacts
            ],
        )

    return app


app = create_app()
