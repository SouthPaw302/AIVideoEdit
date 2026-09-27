from __future__ import annotations

import asyncio
import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field

router = APIRouter(prefix="/production", tags=["production-proxy"])


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ProductionCall(StrictModel):
    name: str = Field(min_length=1, max_length=160)
    arguments: dict[str, Any] = Field(default_factory=dict)


def _base(request: Request) -> tuple[str, float]:
    settings = request.app.state.settings
    url = str(settings.studio_url or "").rstrip("/")
    if not url:
        raise HTTPException(
            status_code=503,
            detail="AIVIDEOEDIT_STUDIO_URL is not configured on this bridge",
        )
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise HTTPException(
            status_code=503,
            detail="configured Studio URL is invalid",
        )
    return url, float(settings.studio_timeout_seconds)


def _request_json(url: str, timeout: float, *, method: str = "GET", payload: dict | None = None) -> dict:
    body = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read(4 * 1024 * 1024 + 1)
            if len(raw) > 4 * 1024 * 1024:
                raise HTTPException(
                    status_code=502,
                    detail="Studio response exceeded bridge limit",
                )
            data = json.loads(raw.decode("utf-8"))
            if not isinstance(data, dict):
                raise HTTPException(
                    status_code=502,
                    detail="Studio returned non-object JSON",
                )
            return data
    except urllib.error.HTTPError as exc:
        raw = exc.read(64 * 1024)
        detail = raw.decode("utf-8", errors="replace") or str(exc)
        raise HTTPException(
            status_code=502,
            detail=f"Studio HTTP {exc.code}: {detail[:4000]}",
        ) from exc
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Studio unavailable or invalid response: {exc}",
        ) from exc


@router.get("/status")
async def production_status(request: Request):
    base, timeout = _base(request)
    return await asyncio.to_thread(
        _request_json,
        f"{base}/api/system",
        timeout,
    )


@router.get("/tools")
async def production_tools(request: Request):
    base, timeout = _base(request)
    return await asyncio.to_thread(
        _request_json,
        f"{base}/api/tools",
        timeout,
    )


@router.post("/call")
async def production_call(payload: ProductionCall, request: Request):
    base, timeout = _base(request)
    return await asyncio.to_thread(
        _request_json,
        f"{base}/api/tools/call",
        timeout,
        method="POST",
        payload={
            "name": payload.name,
            "arguments": payload.arguments,
        },
    )
