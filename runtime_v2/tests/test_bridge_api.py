from pathlib import Path

from fastapi.testclient import TestClient

from runtime_v2.bridge.app import create_app
from runtime_v2.bridge.config import BridgeSettings


def test_health_is_public_and_has_request_id(tmp_path: Path):
    app = create_app(
        BridgeSettings(bearer_token="secret", workspace_root=str(tmp_path / "jobs"))
    )
    client = TestClient(app)

    response = client.get("/health", headers={"X-Request-ID": "test-health-1"})

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "test-health-1"
    assert response.json() == {
        "status": "ok",
        "service": "aivideoedit-agent-bridge",
        "version": "0.3.0",
    }


def test_protected_endpoint_rejects_missing_token(tmp_path: Path):
    app = create_app(
        BridgeSettings(bearer_token="secret", workspace_root=str(tmp_path / "jobs"))
    )
    client = TestClient(app)

    response = client.get("/version")

    assert response.status_code == 401
    assert response.json()["error"] == "unauthorized"
    assert response.json()["request_id"]


def test_version_accepts_valid_token(tmp_path: Path):
    app = create_app(
        BridgeSettings(bearer_token="secret", workspace_root=str(tmp_path / "jobs"))
    )
    client = TestClient(app)

    response = client.get(
        "/version",
        headers={"Authorization": "Bearer secret"},
    )

    assert response.status_code == 200
    assert response.json()["runtime"] == "runtime_v2"
    assert response.json()["api_version"] == "v1"
    assert response.json()["service_version"] == "0.2.0"


def test_capabilities_can_hide_planned_entries(tmp_path: Path):
    app = create_app(BridgeSettings(workspace_root=str(tmp_path / "jobs")))
    client = TestClient(app)

    response = client.get("/capabilities?include_planned=false")

    assert response.status_code == 200
    names = [item["name"] for item in response.json()["capabilities"]]
    assert {
        "bridge.health",
        "bridge.version",
        "bridge.capabilities",
        "cli.run",
        "boot.capsule",
        "gate.evaluate",
        "model.registry",
        "model.music_beat",
        "jev.decide",
        "harness.optional",
    }.issubset(set(names))


def test_audit_jsonl_is_written(tmp_path: Path):
    audit_path = tmp_path / "audit" / "bridge.jsonl"
    app = create_app(
        BridgeSettings(
            audit_log_path=str(audit_path),
            workspace_root=str(tmp_path / "jobs"),
        )
    )
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    data = audit_path.read_text(encoding="utf-8")
    assert '"path":"/health"' in data
    assert '"status_code":200' in data
