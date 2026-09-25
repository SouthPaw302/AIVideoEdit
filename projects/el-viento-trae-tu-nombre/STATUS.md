# Status

Machine stage: **FX_LOCKED / MISSING-FX PASS PENDING**.

Active branch: `song/el-viento-trae-tu-nombre` only. **Main is untouched.**

Current preserved Route 4 baseline:
- 154.375 seconds
- 1920x1080 / 24 fps / 3705 frames
- source-audio authority: 154.480 seconds
- edit timing, hero order, audio, intro/outro, camera language and hand repair are locked
- technical decode / black / freeze QC passes
- current 1080 is **not FX-complete**

The obsolete 112.680-second S01-S11 script/assembly/QC/FX-lock records are archived under `archive/`.

## FX contract

The corrected `FX_REQUIREMENTS.json` now targets the current Route 4 edit and approved repo FX stack.

The canonical FX v2 precompile gate has **generated and verified** the new `fx.lock.json` against:
- corrected 154.375-second `SCRIPT.json`
- current Route 4 batch shot locks
- Batches 07-09 supplemental source manifests
- reopened Batch 01-06 + extended-act FX gates
- canonical registry/runtime/proof evidence

FX lock SHA-256: `107090e7e09b2686f1c56b44d78d027b8802b7cdd2a16a583b1e8a5bbd073530`

Current production gate: **APPLY MISSING FX TO PRESERVED EDIT**.

No rendering is authorized right now.

Rules:
- do not restart production
- do not regenerate accepted media
- do not replace the current edit
- do not create Batch 10
- do not modify main
- do not upscale until the 1080 FX master is complete and approved
