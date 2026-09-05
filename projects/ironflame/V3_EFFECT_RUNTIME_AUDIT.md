# IronFlame V3 Effect / Model / Transition Runtime Audit

Date: 2026-09-05
Branch target: `song/ironflame-20260905-0216`
Status: **FAIL-CLOSED / existing V3 blocks remain exploratory proofs only**

## Purpose

Verify whether the current V3 shot-package renders actually execute the canonical AIVideoEdit FX V2 runtime/model/effect/transition implementations, rather than merely producing similar-looking pixels.

## Repository rule applied

`general/reusable/fx_v2/PRECOMPILE_FX_GATE.md` requires exact FX IDs, canonical registry resolution, real runtime wiring, approved proof/QC, pixel-level smoke tests, and lock verification. A render that looks correct but bypasses the canonical runtime is not production-verified.

## Static provenance audit

| Range | Render script | Canonical `fx_v2/runtime.py` imported? | FX2 IDs declared in renderer? | Canonical song controls used? | Result |
|---|---|---:|---:|---:|---|
| 00:00-00:42 | renderer provenance not preserved as a single script | UNPROVEN | UNPROVEN | evidence exists in shot package control streams | **FAIL / cannot verify canonical runtime** |
| 00:42-01:35 | `/mnt/data/render_v3_42_95.py` | NO | NO | YES | **FAIL canonical FX provenance** |
| 01:35-02:02 | `/mnt/data/render_v3_95_122.py` | NO | NO | YES | **FAIL canonical FX provenance** |
| 02:02-02:47 | `/mnt/data/ironflame_v3/render_122_167_v32.py` | NO | NO | YES | **FAIL canonical FX provenance** |
| 02:47-03:30 | `/mnt/data/ironflame_v3/render_167_210_v32.py` | NO | NO | YES | **FAIL canonical FX provenance** |
| 03:30-04:04.680 | `/mnt/data/ironflame_v3/render_210_244_v32.py` | NO | NO | YES | **FAIL canonical FX provenance** |

## What actually ran

The current V3 renders use custom OpenCV/FFmpeg procedures directly in the song render scripts:

- `cv2.warpAffine` for camera push/drift/rotation;
- `cv2.remap` for contour/ribbon deformation;
- luminance/color masks plus direct array additions for localized glow/shimmer;
- custom `ribbon_transition()` masks in several blocks;
- FFmpeg `xfade=smoothleft` in the 01:35-02:02 block;
- custom generated ring/filament overlays in the 00:42-02:02 blocks;
- canonical frame-aligned `ironflame_controls_24fps.json` values (`rms_n`, `onset_n`, `low_n`, `mid_n`, `high_n`) do drive those custom procedures.

This proves the shots are audio-reactive, but it **does not prove** that registered effects such as `FX2-MOTION-002`, `FX2-LIGHT-001`, `FX2-LIGHT-002`, `FX2-SURFACE-001`, or any registered transition were actually executed.

## Transition audit

Current transitions are not production-approved registry transitions:

- 00:42-01:35: custom wavy ribbon transport in song renderer;
- 01:35-02:02: FFmpeg `smoothleft` xfade;
- 02:02-04:04.680: custom contour/ribbon mask transport.

The canonical registry currently marks the FX2 transition family as `proof_required`, therefore none may be claimed production-approved until proof/QC promotion occurs. Current custom transitions have not been registered or gated.

## Model / spatial claim audit

No evidence was found in these V3 render scripts that NeRF, 3D Gaussian Splatting, SuperSplat, or the canonical streaming living-parallax adapter was actually executed. Therefore V3 must make **no NeRF/3DGS/model claim** for these blocks.

## Verification decision

1. Existing V3 videos remain useful visual experiments and narrative references.
2. Existing export QC (resolution, fps, black/freeze scan, hashes) remains valid only as export QC.
3. Existing blocks are **not effect-gate verified** and must not be promoted as production-approved shot packages.
4. No further shot is to be marked verified unless its proof package records the exact canonical runtime/effect IDs or an explicitly registered and approved new effect implementation.
5. Any custom transition intended to survive must be registered, proof-rendered, visually approved, and passed through the same fail-closed gate before production use.

## Next correction pass

Rebuild/validate shots from the effect layer outward:

- use only approved canonical FX IDs where their visual behavior fits the IronFlame source language;
- create dedicated proofs for any needed IronFlame-specific transition/effect not already approved;
- record source plate, effect ID, runtime method, parameters, proof binary SHA-256, temporal/pixel metrics, and visual QC decision;
- reject any no-op, generic, identity-damaging, or source-language-breaking result;
- only after individual effect proofs pass should a scene package be marked `verified_candidate`.

This audit intentionally does not create `FX_REQUIREMENTS.fx.json` or `fx.lock.json`; the project is still in shot/effect proof development, not production compile.
