# AIVideoEdit Runtime V2

Runtime V2 is an isolated experimental capability layer for the `MainV2` branch.
It does not replace the current production system. It consumes the existing repo as
a backend/source of truth while the new remote-agent architecture is proven.

## Step 1: Remote Agent Bridge foundation

Implemented:

- FastAPI service isolated under `runtime_v2/`
- `GET /health`
- `GET /version`
- `GET /capabilities`
- strict Pydantic response schemas
- optional bearer-token protection via `BRIDGE_TOKEN`
- client/request-generated `X-Request-ID`
- configurable request timeout via `BRIDGE_REQUEST_TIMEOUT_SECONDS`
- JSONL audit logging via `BRIDGE_AUDIT_LOG`
- machine-readable OpenAPI schema
- unit tests

Not implemented yet:

- arbitrary or allowlisted CLI execution
- Git/repo write operations
- JEV evaluation
- DeepSeek Harness routing
- ONNX/model execution
- external LLM routing
- MCP exposure

Those are deliberately excluded from Step 1.

## Run locally

```bash
python -m pip install -r runtime_v2/requirements.txt
python -m runtime_v2.bridge
```

The development service listens on `127.0.0.1:8787`.

For a protected bridge:

```bash
export BRIDGE_TOKEN="replace-me"
python -m runtime_v2.bridge
```

Then:

```bash
curl http://127.0.0.1:8787/health
curl -H "Authorization: Bearer replace-me" http://127.0.0.1:8787/version
curl -H "Authorization: Bearer replace-me" http://127.0.0.1:8787/capabilities
```

## Test

```bash
pytest -q runtime_v2/tests
```

## Security boundary

The bridge currently executes no shell commands and has no repository mutation
endpoint. Health is intentionally public for infrastructure liveness checks.
All other endpoints require a bearer token when `BRIDGE_TOKEN` is configured.

HTTPS should be terminated by the deployment platform or reverse proxy. Secrets
remain server-side and must never be committed to the repository.
