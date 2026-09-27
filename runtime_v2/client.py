from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


class BridgeClient:
    def __init__(self, base_url: str, token: str | None = None, timeout: float = 120.0):
        self.base_url = base_url.rstrip("/")
        parsed = urllib.parse.urlparse(self.base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("bridge URL must be absolute http(s)")
        self.token = token
        self.timeout = timeout

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict:
        if not path.startswith("/"):
            raise ValueError("bridge path must start with /")
        body = None
        headers = {"Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if payload is not None:
            body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(
            self.base_url + path,
            data=body,
            headers=headers,
            method=method.upper(),
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
                if not isinstance(data, dict):
                    raise RuntimeError("bridge returned non-object JSON")
                return data
        except urllib.error.HTTPError as exc:
            raw = exc.read(256 * 1024)
            detail = raw.decode("utf-8", errors="replace")
            raise RuntimeError(f"bridge HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"bridge connection failed: {exc}") from exc


def _json_arg(value: str) -> dict:
    if value.startswith("@"):
        data = json.loads(Path(value[1:]).read_text(encoding="utf-8"))
    else:
        data = json.loads(value)
    if not isinstance(data, dict):
        raise ValueError("arguments must decode to a JSON object")
    return data


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Thin SandAgent client for AIVideoEdit Runtime V2")
    ap.add_argument(
        "--url",
        default=os.environ.get("AIVIDEOEDIT_BRIDGE_URL", ""),
        help="Runtime V2 bridge base URL or AIVIDEOEDIT_BRIDGE_URL",
    )
    ap.add_argument(
        "--token",
        default=os.environ.get("AIVIDEOEDIT_BRIDGE_TOKEN"),
        help="Bearer token or AIVIDEOEDIT_BRIDGE_TOKEN",
    )
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("health")
    sub.add_parser("capabilities")
    sub.add_parser("status")
    sub.add_parser("tools")
    call = sub.add_parser("call")
    call.add_argument("tool")
    call.add_argument("--args", default="{}", help="JSON object or @file.json")
    decide = sub.add_parser("decide")
    decide.add_argument("--payload", required=True, help="JSON object or @file.json")
    project_decide = sub.add_parser("project-decide")
    project_decide.add_argument("project_id")
    project_decide.add_argument("action")
    project_decide.add_argument("--payload", default="{}", help="Additional production.decide arguments as JSON or @file.json")
    music = sub.add_parser("music")
    music.add_argument("path")
    return ap


def main() -> int:
    args = build_parser().parse_args()
    if not args.url:
        raise SystemExit("AIVIDEOEDIT_BRIDGE_URL or --url is required")
    client = BridgeClient(args.url, args.token)

    if args.command == "health":
        result = client.request("GET", "/health")
    elif args.command == "capabilities":
        result = client.request("GET", "/capabilities")
    elif args.command == "status":
        result = client.request("GET", "/production/status")
    elif args.command == "tools":
        result = client.request("GET", "/production/tools")
    elif args.command == "call":
        result = client.request(
            "POST",
            "/production/call",
            {"name": args.tool, "arguments": _json_arg(args.args)},
        )
    elif args.command == "decide":
        result = client.request(
            "POST",
            "/intelligence/decide",
            _json_arg(args.payload),
        )
    elif args.command == "music":
        result = client.request(
            "POST",
            "/intelligence/music/analyze",
            {"path": args.path},
        )
    else:
        raise SystemExit("unknown command")

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
