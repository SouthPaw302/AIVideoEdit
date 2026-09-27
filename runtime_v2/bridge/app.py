"""FastAPI application for the Runtime V2 Remote Agent Bridge."""

from __future__ import annotations

import logging

from fastapi import FastAPI, Query

from .capabilities import list_capabilities
from .config import BridgeSettings
from .middleware import BridgeMiddleware
from .schemas import CapabilitiesResponse, HealthResponse, VersionResponse


def create_app(settings: BridgeSettings | None = None) -> FastAPI:
    resolved = settings or BridgeSettings.from_env()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    app = FastAPI(
        title="AIVideoEdit Agent Bridge",
        version=resolved.service_version,
        docs_url="/docs",
        redoc_url=None,
        openapi_url="/openapi.json",
    )
    app.state.settings = resolved
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

    return app


app = create_app()
