# QC — FX/depth assembled candidate

## Current result
Assembly technical + mode-aware QC: **PASS**

Final artistic acceptance: **PENDING USER REVIEW**

## Export
- Duration: **244.680 s** (exact target)
- Frames: **5872**
- Video: H.264, 1280x720, 24 fps
- Audio: AAC, 48 kHz stereo
- Assembled SHA-256: `7ae715b7fbe254e802b51a00c0f1ea5641bec3e51b54a17136df4111c982eddc`

## Source integrity
- Accepted source SHA-256: `ddedf3632ebf3837518090dfa85bc437de7c07de2ad4c21af1b82b80f47b23d3`
- Audio stream is bit-for-bit identical before/after: **PASS**
- Minimum sampled source/output frame correlation: **0.958410**
- Sampled FX pixel delta range: **7.080970–9.878888**
- Black-frame scan: **0 source / 0 output**
- Freeze/low-motion detector: source **30 events / 63.125 s**; output **13 events / 30.167 s**. No new macro-freeze defect.

## Production evidence
- Song FX gate: **PASS**
- `fx.lock.json`: verified
- Shot proof direction: user approved
- Duplicate support: 12 original/moved pairs converted to depth/GIF support
- Production backend mapping: `RENDER_RECIPE.json`
- Before/after evidence: `REFINEMENT_QC.json`

Do not set `final_qc_passed=true` until the user reviews and accepts the complete assembled export.
