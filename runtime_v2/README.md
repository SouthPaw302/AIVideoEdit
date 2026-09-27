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
- strict Pydantic API schemas
- optional bearer-token protection via `BRIDGE_TOKEN`
- client/request-generated `X-Request-ID`
- configurable request timeout via `BRIDGE_REQUEST_TIMEOUT_SECONDS`
- JSONL audit logging via `BRIDGE_AUDIT_LOG`
- machine-readable OpenAPI schema

## Step 2: Safe Execution Worker

Implemented:

- `GET /tools` for machine-readable tool discovery
- `POST /tools/run` for registered tool execution
- no `shell=True` and no arbitrary shell endpoint
- static allowlist registry
- one isolated workspace per execution
- sanitized child-process environment
- execution timeouts
- bounded stdout/stderr capture
- artifact enumeration, size reporting, and SHA-256 hashing
- automatic workspace cleanup by default
- optional retained workspaces for debugging

Initial registered tools are intentionally narrow:

- `runtime.python.version`
- `runtime.python.probe`
- `system.git.version`
- `system.ffmpeg.version`
- `system.ffprobe.version`

The registry architecture is ready for approved repo scripts and read-only repo tools,
but those are connected in Step 3 rather than giving Step 2 broad filesystem access.

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

Optional worker configuration:

```bash
export BRIDGE_EXECUTION_TIMEOUT_SECONDS="20"
export BRIDGE_MAX_OUTPUT_BYTES="262144"
export BRIDGE_WORKSPACE_ROOT="/tmp/aivideoedit-runtime-v2/jobs"
export BRIDGE_KEEP_WORKSPACES="0"
```

Examples:

```bash
curl http://127.0.0.1:8787/health
curl -H "Authorization: Bearer replace-me" http://127.0.0.1:8787/tools

curl \
  -H "Authorization: Bearer replace-me" \
  -H "Content-Type: application/json" \
  -d '{"tool":"runtime.python.probe"}' \
  http://127.0.0.1:8787/tools/run
```

## Test

```bash
python -m pytest -q runtime_v2/tests
```

## Security boundary

The worker executes only commands registered server-side. The request cannot supply
an executable, shell string, working directory, environment variables, or filesystem
root. Built-in tools do not currently accept user arguments.

Each execution receives its own workspace. The worker returns only relative artifact
paths and hashes and removes the workspace unless debugging retention is explicitly
enabled.

This is process-level hardening, not a kernel/container security boundary. Network
and OS-level isolation should be provided by the deployment environment before
higher-risk tools are registered.

Repo mutation integration, external LLM routing, and broader MCP exposure remain later steps.
Jev and bounded model execution are now present in the Surgical Intelligence layer.


## Surgical Intelligence Integration

MainV2 layers bounded intelligence around the existing production system rather than
replacing it. Production boot still defaults to main. Experimental validation uses:

    python bootstrap.py boot --repo-root . --authority-ref MainV2

The stack now includes a portable boot capsule and attestation, Runtime Gatekeeper,
provider-neutral model registry, optional ONNX music/beat inference, existing
AIVideoEdit audio_map fallback, bounded Jev decisions, optional Harness requests,
and micro-fixture/golden regression verification.

ONNX remains optional:

    python -m pip install -r runtime_v2/requirements-onnx.txt
    export AIVIDEOEDIT_BEAT_ONNX_MODEL=/absolute/path/to/approved-beat-model.onnx

Large model binaries are not committed to normal repository history.
