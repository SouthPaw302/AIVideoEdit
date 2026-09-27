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


## Remote SandAgent deployment

Runtime V2 can be the single public HTTPS-facing endpoint while the existing
Studio Tool API remains private.

The included Compose topology runs:

- `bridge`: public Runtime V2 API, bearer-token protected
- `studio`: private existing AIVideoEdit Tool API, not published to the host
- persistent job, Studio-state, and model-cache volumes

Start locally:

```bash
cp runtime_v2/.env.example .env
# edit BRIDGE_TOKEN
docker compose -f runtime_v2/docker-compose.yml up --build
```

SandAgent can then use the dependency-free client:

```bash
export AIVIDEOEDIT_BRIDGE_URL="https://your-runtime.example.com"
export AIVIDEOEDIT_BRIDGE_TOKEN="..."
python -m runtime_v2.client health
python -m runtime_v2.client capabilities
python -m runtime_v2.client tools
python -m runtime_v2.client call production.status --args '{"project_id":"demo"}'
```

Production calls sent to `/production/call` are reverse-adapted to Studio's
existing `/api/tools/call`; Runtime V2 does not implement a parallel production
mutation engine. On MainV2-capable workspaces the underlying Tool API performs
Gatekeeper -> canonical operation -> capsule refresh.

In production, terminate TLS at the hosting platform/reverse proxy and expose
only the bridge port. Do not publish the Studio port directly.


## Hardened production integration

MainV2 production mutations now layer Runtime V2 enforcement in front of the
existing canonical AIVideoEdit Tool API rather than replacing it.

For each attested MainV2 mutation the runtime:

1. re-runs the canonical production guard;
2. verifies the signed boot capsule and current branch;
3. rejects stale HEAD, project-state, operating-order, and media-manifest state;
4. maps the requested Tool API operation to bounded change tags;
5. enforces active refinement/recut allowed and forbidden scope;
6. performs the existing canonical operation;
7. refreshes the boot capsule after a successful state change.

The deployed Compose topology requires a separate
`AIVIDEOEDIT_ATTESTATION_KEY` and sets
`AIVIDEOEDIT_REQUIRE_SIGNED_ATTESTATION=1`.

Studio music analysis also consumes the Runtime V2 music worker directly.
The pinned Beat This ONNX provider is preferred when its verified model is
provisioned; otherwise the registry falls back to existing/built-in deterministic
DSP evidence. The older RMS energy/section analysis remains in place and is
recorded alongside the embedded rhythm evidence.

A real pinned-model CPU inference fixture remains a promotion checkpoint; model
metadata and preprocessing compatibility are verified independently without
committing the 83 MB model to normal git history.

Director Brain `operating.*` mutations use the same guard/attestation/refresh path; they are no longer a separate mutation bypass.


### Project-aware decision preview

Remote SandAgents can call the normal production proxy with
`production.decide` to evaluate a proposed action against the actual Studio
project workspace. The response combines the Runtime Gatekeeper, bounded Jev
decision, and optional Harness escalation. This is advisory/read-only; executing
the action performs the gate again so a stale preview cannot authorize a later
mutation.
