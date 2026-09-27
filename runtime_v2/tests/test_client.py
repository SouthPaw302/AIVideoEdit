from __future__ import annotations

import io
import json
import urllib.error
from pathlib import Path

import pytest

from runtime_v2.client import BridgeClient, _json_arg, build_parser


class FakeResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, *args):
        return self.payload


def test_client_builds_authorized_json_request(monkeypatch):
    seen = {}

    def fake_urlopen(request, timeout):
        seen["url"] = request.full_url
        seen["authorization"] = request.headers.get("Authorization")
        seen["content_type"] = request.headers.get("Content-type")
        seen["body"] = json.loads(request.data.decode("utf-8"))
        seen["timeout"] = timeout
        return FakeResponse({"ok": True})

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    client = BridgeClient("https://bridge.example.test/", token="secret", timeout=9)
    result = client.request("POST", "/production/call", {"name": "production.status", "arguments": {}})

    assert result == {"ok": True}
    assert seen["url"] == "https://bridge.example.test/production/call"
    assert seen["authorization"] == "Bearer secret"
    assert seen["body"]["name"] == "production.status"
    assert seen["timeout"] == 9


def test_json_arg_supports_file(tmp_path: Path):
    p = tmp_path / "args.json"
    p.write_text('{"project_id":"demo"}', encoding="utf-8")
    assert _json_arg("@" + str(p)) == {"project_id": "demo"}


def test_client_rejects_relative_base_url():
    with pytest.raises(ValueError):
        BridgeClient("/relative")



def test_project_decide_cli_parses_project_and_action():
    args = build_parser().parse_args(
        [
            "--url",
            "https://bridge.example.test",
            "project-decide",
            "demo",
            "storyboard.set",
            "--payload",
            '{"checks":{"qc":true}}',
        ]
    )
    assert args.command == "project-decide"
    assert args.project_id == "demo"
    assert args.action == "storyboard.set"
    assert _json_arg(args.payload)["checks"]["qc"] is True
