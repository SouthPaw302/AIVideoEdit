"""Security, request identity, timeout, and audit middleware."""

from __future__ import annotations

import asyncio
import hmac
import logging
import re
import time
import uuid

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .audit import build_record, write_record
from .config import BridgeSettings


LOGGER = logging.getLogger("runtime_v2.bridge")
_REQUEST_ID_PATTERN = re.compile(r"^[A-Za-z0-9._:-]{1,128}$")


def _request_id(request: Request) -> str:
    candidate = request.headers.get("X-Request-ID", "")
    if candidate and _REQUEST_ID_PATTERN.fullmatch(candidate):
        return candidate
    return str(uuid.uuid4())


def _authorized(request: Request, token: str | None) -> bool:
    if token is None:
        return True

    authorization = request.headers.get("Authorization", "")
    prefix = "Bearer "
    if not authorization.startswith(prefix):
        return False

    supplied = authorization[len(prefix) :]
    return hmac.compare_digest(supplied, token)


class BridgeMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *, settings: BridgeSettings):
        super().__init__(app)
        self.settings = settings

    async def dispatch(self, request: Request, call_next):
        request_id = _request_id(request)
        request.state.request_id = request_id
        started = time.perf_counter()

        # Health remains available to infrastructure without credentials.
        if request.url.path != "/health" and not _authorized(
            request, self.settings.bearer_token
        ):
            response = JSONResponse(
                status_code=401,
                content={
                    "error": "unauthorized",
                    "detail": "A valid bearer token is required.",
                    "request_id": request_id,
                },
            )
        else:
            try:
                response = await asyncio.wait_for(
                    call_next(request),
                    timeout=self.settings.request_timeout_seconds,
                )
            except asyncio.TimeoutError:
                response = JSONResponse(
                    status_code=504,
                    content={
                        "error": "request_timeout",
                        "detail": "The bridge request exceeded its configured timeout.",
                        "request_id": request_id,
                    },
                )
            except Exception:
                LOGGER.exception("Unhandled bridge error request_id=%s", request_id)
                response = JSONResponse(
                    status_code=500,
                    content={
                        "error": "internal_error",
                        "detail": "The bridge encountered an internal error.",
                        "request_id": request_id,
                    },
                )

        response.headers["X-Request-ID"] = request_id
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        write_record(
            build_record(
                request_id=request_id,
                method=request.method,
                path=request.url.path,
                status_code=response.status_code,
                duration_ms=elapsed_ms,
            ),
            self.settings.audit_log_path,
        )
        return response
