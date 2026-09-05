# IronFlame V3 — FX2 Verification Pass

## Shot 01 canonical FX proof

Status: **KEEP AS TECHNICAL/STYLE PROOF**. This is the first V3 rerender produced after the runtime-provenance audit.

Executed canonical FX IDs:
- FX2-MOTION-002 — localized_living_flow
- FX2-LIGHT-001 — practical_light_breath
- FX2-LIGHT-002 — moving_light_field
- FX2-SURFACE-001 — temporal_canvas_lock

Canonical runtime source: `general/reusable/fx_v2/runtime.py` blob `3355d5a63c3301d6f8fcbe8a369c8acd98b97c4c`.

Proof: 640x360, 24 fps, 144 frames, 6.0s.
Binary SHA-256: `2e9648c41a7fa8b99e61064a86e1bd483c78c8396f82ee4244bf4c2159df6646`.
Mean source delta: 2.171938. Max source delta: 2.450854.
Mean adjacent-frame delta: 0.141057; p95: 0.479925.
Export scan: zero black events; zero >=1.5s freeze events.

`runtime_trace.json` records, for every frame, audio control values plus every FX ID and its pixel delta from the incoming frame.

This does **not** claim NeRF, 3DGS, SuperSplat, streaming living parallax, or any `proof_required` transition/model. Those remain blocked until independently proven/approved.
