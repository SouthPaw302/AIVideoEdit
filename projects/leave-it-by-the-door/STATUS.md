# Leave It by the Door — Status

**Updated:** 2026-09-05 UTC  
**Branch:** `song/leave-it-by-the-door`  
**State:** Active production; handoff recovered; native-24-fps rebuild underway

## Recovered and confirmed

- Complete prior handoff ZIP was recovered into the active workspace.
- Canonical remastered source audio recovered: `Leave it by the door. (Remastered) (1).wav`.
- 13 named generated hero stills recovered.
- Prior reference clips, extracted reference frames, project/storyboard docs, QC sheets, masks, derivatives, render scripts and the previous full V1.1 render were recovered.
- Previous V1.1 was diagnosed as visually under-sampled because shot intermediates were rendered at 10 fps and then delivered inside a 24 fps container.
- That V1.1 is no longer the quality target.

## Current quality references

Two user-supplied clips are now the motion/effects references:
- `imagine-f9c3e46d.mp4`
- `imagine-1fb7bb42.mp4`

Both are true 24 fps. See `REFERENCE_MOTION_TARGETS.md` for measured bitrate/motion targets and the adopted effect language.

## Native 24 fps rebuild

A new living-scene proof engine has been implemented and checkpointed at:

`projects/leave-it-by-the-door/scripts/render_native24_living_scene_proof.py`

The engine uses:
- native per-frame 24 fps rendering
- optical-flow signatures measured from the supplied reference videos
- localized semantic motion masks
- separate sea/cloud/hair/skirt/crowd motion
- continuous rain, wave spray and ember trajectories
- wet reflection ripple
- reference-derived warm/cool light migration
- restrained camera motion secondary to internal image motion
- identity protection around principal faces/subjects

Sandbox proof produced:
`Leave_It_By_The_Door_NATIVE24_LivingScene_PROOF01_720p24.mp4`

Proof properties:
- 1280×720
- native 24 fps
- 144 unique rendered frames / 6.0 s
- H.264 video bitrate ≈ 12.2 Mbps
- AAC ≈ 297 kbps

## Next production action

1. Increase internal motion energy toward the slower supplied reference while keeping faces stable.
2. Convert the 25-shot full-song map to the native-24 living-scene engine.
3. Render in resumable per-shot chunks rather than one monolithic job.
4. QC every shot for frozen/repeated frames, identity drift, mask seams, black frames and motion discontinuities.
5. Assemble a 1920×1080 / native 24 fps full master.
6. Keep scripts, manifests, metrics and status checkpointed to this branch while large media remains in workspace/object storage.

## Storage

GitHub is the connected persistent control/source-of-truth layer for this production. The current environment does not expose an authenticated Cloudflare R2 connector, so no R2 upload should be claimed. Large media remains in the active workspace/Library until a legitimate object-storage connector is connected.
