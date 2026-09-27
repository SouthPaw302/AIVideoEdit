from pathlib import Path

from fastapi.testclient import TestClient

from runtime_v2.bridge.app import create_app
from runtime_v2.bridge.config import BridgeSettings


def _client(tmp_path: Path, **overrides) -> TestClient:
    values = {
        "workspace_root": str(tmp_path / "jobs"),
        "execution_timeout_seconds": 5.0,
        "max_output_bytes": 64 * 1024,
    }
    values.update(overrides)
    return TestClient(create_app(BridgeSettings(**values)))


def test_tools_endpoint_lists_registry(tmp_path: Path):
    client = _client(tmp_path)

    response = client.get("/tools")

    assert response.status_code == 200
    tools = {item["name"]: item for item in response.json()["tools"]}
    assert tools["runtime.python.version"]["available"] is True
    assert tools["runtime.python.version"]["accepts_user_args"] is False
    assert "runtime.python.probe" in tools


def test_python_version_executes_without_shell(tmp_path: Path):
    client = _client(tmp_path)

    response = client.post(
        "/tools/run",
        json={"tool": "runtime.python.version", "args": []},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["tool"] == "runtime.python.version"
    assert payload["exit_code"] == 0
    assert payload["timed_out"] is False
    combined = payload["stdout"] + payload["stderr"]
    assert "Python" in combined


def test_unregistered_tool_is_rejected(tmp_path: Path):
    client = _client(tmp_path)

    response = client.post(
        "/tools/run",
        json={"tool": "shell", "args": ["rm", "-rf", "/"]},
    )

    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]


def test_user_arguments_are_rejected_for_fixed_tool(tmp_path: Path):
    client = _client(tmp_path)

    response = client.post(
        "/tools/run",
        json={"tool": "runtime.python.version", "args": ["-c", "print(1)"]},
    )

    assert response.status_code == 400
    assert "does not accept user arguments" in response.json()["detail"]


def test_probe_creates_hashed_artifact_then_workspace_is_removed(tmp_path: Path):
    workspace_root = tmp_path / "jobs"
    client = _client(tmp_path)

    response = client.post(
        "/tools/run",
        json={"tool": "runtime.python.probe"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["exit_code"] == 0
    assert payload["artifacts"]
    artifact = payload["artifacts"][0]
    assert artifact["path"] == "probe.json"
    assert len(artifact["sha256"]) == 64
    assert not (workspace_root / payload["job_id"]).exists()


def test_keep_workspaces_preserves_job_directory(tmp_path: Path):
    workspace_root = tmp_path / "jobs"
    client = _client(tmp_path, keep_workspaces=True)

    response = client.post(
        "/tools/run",
        json={"tool": "runtime.python.probe"},
    )

    assert response.status_code == 200
    job_id = response.json()["job_id"]
    assert (workspace_root / job_id / "probe.json").exists()


def test_request_schema_rejects_excessive_timeout(tmp_path: Path):
    client = _client(tmp_path)

    response = client.post(
        "/tools/run",
        json={"tool": "runtime.python.version", "timeout_seconds": 121},
    )

    assert response.status_code == 422
