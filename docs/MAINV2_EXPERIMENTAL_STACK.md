# MainV2 Experimental Integration Branch

## Purpose
`MainV2` is the isolated integration and test branch for the next AIVideoEdit agent/runtime architecture.

## Branch Rules
- Do not modify `main` while MainV2 work is under test.
- New agent-bridge, harness, JEV, remote-tool, model-service, ONNX, MCP, and sandbox-runtime work lands here first.
- Existing production branches remain independent unless explicitly migrated.
- No automatic merge or back-port to `main`.
- Every major subsystem must be testable independently before promotion.
- Prefer surgical changes over broad rewrites.
- Preserve current production behavior unless a MainV2 test explicitly targets it.

## Target Stack
1. Remote Tool Bridge
2. Safe CLI worker
3. Repo integration
4. DeepSeek Harness as orchestration/router
5. JEV deterministic controller
6. ONNX and specialist model services
7. AIVideoEdit high-level production tools
8. Optional interchangeable LLM routing
9. MCP/tool discovery interface
10. Security, auditing, and regression testing

## Operating Model
- GitHub: durable source of truth
- SandAgent: authenticated reasoning/operator layer
- DeepSeek Harness: orchestration and routing, not a required DeepSeek model
- JEV: deterministic workflow and guardrails
- Agent Bridge: persistent external capability layer
- ONNX/vision/audio models: specialist services
- CLI/Git/FFmpeg: execution layer
- External LLMs: optional, interchangeable specialist reasoning

## Promotion Rule
Nothing from MainV2 moves to `main` until the relevant capability has passed sandbox tests and the user explicitly approves promotion.
