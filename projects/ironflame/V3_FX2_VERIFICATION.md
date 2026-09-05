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

## Shot 02 canonical FX proof

Status: **TECHNICAL PASS PENDING HUMAN VISUAL QC**.

Executed canonical FX IDs: FX2-MOTION-002, FX2-LIGHT-001, FX2-LIGHT-002, FX2-SURFACE-001.
Song start: 18.0s. Proof: 640x360, 24 fps, 144 frames, 6.0s.
Binary SHA-256: `99dd3bc20fc6f400dd77f5c4adb27755f38d482589e7ccc351922c2b3a0d3f63`.
Mean source delta: 1.969811; max: 2.477173. Mean adjacent-frame delta: 0.153344; p95: 0.631129.
Export scan: zero black events; zero >=1.5s freeze events.

## Shot 03 canonical FX proof

Status: **TECHNICAL PASS PENDING HUMAN VISUAL QC**.

Source: `cosmic_recognition_in_blue_light.png`.
Executed canonical FX IDs: FX2-MOTION-002, FX2-LIGHT-001, FX2-LIGHT-002, FX2-SURFACE-001.
Song start: 42.0s. Proof: 640x360, 24 fps, 144 frames, 6.0s.
Binary SHA-256: `a38362a533c8273fe38731d36edfcf43bba03831f94c212009e82a09bcc3ab2c`.
Mean source delta: 2.249259; max: 2.638252. Mean adjacent-frame delta: 0.154784; p95: 0.520515.
Export scan: zero black events; zero >=1.5s freeze events.

## Shot 04 canonical FX proof

Status: **TECHNICAL PASS PENDING HUMAN VISUAL QC**.

Source: `crystalline_cosmic_encounter.png`.
Executed canonical FX IDs: FX2-MOTION-002, FX2-LIGHT-001, FX2-LIGHT-002, FX2-SURFACE-001.
Song start: 77.0s. Proof: 640x360, 24 fps, 144 frames, 6.0s.
Binary SHA-256: `ea775fde341e20033db1de416be1b200fe791d94dd6aed5937e8387802d1b79c`.
Mean source delta: 3.105593; max: 3.610826. Mean adjacent-frame delta: 0.223311; p95: 0.658765.
Export scan: zero black events; zero >=1.5s freeze events.

These proofs execute only effects already marked `approved` in the canonical registry. No unapproved transition, NeRF, 3DGS, SuperSplat, or living-parallax claim is made here.
