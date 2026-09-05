# Leave It by the Door — Status

**Updated:** 2026-09-05 UTC  
**Branch:** `song/leave-it-by-the-door`  
**State:** Native-24 V2 full render complete; awaiting user review

## Recovered source package

- Canonical remastered source audio: `Leave it by the door. (Remastered) (1).wav`.
- 13 named generated hero stills recovered from the previous production handoff.
- Prior reference clips, extracted frames, storyboard/project docs, masks, derivatives, render scripts, QC sheets and V1.1 were recovered.
- V1.1 was diagnosed as visually under-sampled because its shot intermediates were rendered at 10 fps and then delivered inside a 24 fps container. V1.1 is retired as the quality target.

## Motion/effects references

User-supplied references:
- `imagine-f9c3e46d.mp4`
- `imagine-1fb7bb42.mp4`

Both are true 24 fps. Their optical-flow and luminance behavior are used as irregular motion drivers. See `REFERENCE_MOTION_TARGETS.md`.

## V2 production architecture

Full renderer:
`projects/leave-it-by-the-door/scripts/render_full_native24_v2.py`

Render plan:
`projects/leave-it-by-the-door/FULL_V2_RENDER_PLAN.md`

V2 uses:
- true per-frame native 24 fps rendering
- 25 independently encoded/resumable shot masters
- 1280×720 H.264 CRF 16 shot masters
- reference-motion-driven exterior/weather and local character/fabric/instrument movement
- rain, sea spray, moving wave/foam bands and wet shimmer
- smoke/fog advection
- warm/cool light migration
- fire/candle breathing and volumetric warm shafts
- embers and burden/ash motif
- lightning/reflection accents
- dawn birds and storm-to-gold progression
- pigment/fog travel transitions
- scene-fixed canvas texture
- face/identity protection masks
- camera motion intentionally secondary to internal scene motion

## Full V2 render complete

Final workspace/Library master:
`Leave_It_By_The_Door_NATIVE24_FULL_V2_720p24.mp4`

Properties:
- duration: 198.833333 s
- resolution: 1280×720
- frame rate: true 24 fps
- frames: 4,772
- H.264 video bitrate: ~7.23 Mbps
- audio: AAC stereo, 48 kHz, ~320 kbps
- file size: ~187.9 MB
- SHA-256: `c82bdb31e7610c7de8d3da506940ebfade5fa6fa1a5af6d6d2ae6e2c4c43c05e`

Every one of the 25 shot masters validated against its exact expected native frame count before assembly. Final video assembly used stream copy for the already-encoded shot video, avoiding a second generational video encode.

## QC

Direct reduced-resolution adjacent-frame scan:
- V2 mean adjacent-frame motion: 3.1315
- V1.1 mean adjacent-frame motion: 1.9270
- V2 therefore carries ~62% more measured frame-to-frame motion than V1.1
- V2 near-exact duplicate frame pairs: 0
- V1.1 near-exact duplicate frame pairs: 7

Reference comparison:
- high-energy storm reference mean adjacent motion: 10.0214
- warm/light reference mean adjacent motion: 5.1089
- V2 intentionally remains below the references' maximum motion energy to preserve painted character identity while substantially increasing living-scene motion over V1.1

QC record:
`projects/leave-it-by-the-door/FULL_V2_QC.json`

## Current decision point

V2 should now be reviewed by the user for artistic intensity and scene-specific motion. Do not revert to the V1.1 10-fps-intermediate workflow. Further revisions should build from the native-24 V2 engine and completed shot architecture.

## Storage

GitHub remains the persistent control/source-of-truth layer for scripts, status, plans and QC metadata. The current environment does not expose an authenticated Cloudflare R2 connector. The 187.9 MB final master is saved persistently in ChatGPT Library; it is too large for a normal single-file GitHub repository object under GitHub's 100 MB file limit.