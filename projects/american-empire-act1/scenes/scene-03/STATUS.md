# Scene 03 — Status

Branch: `project/american-empire-act1/scene-03`  
Canonical project root: `project/american-empire-act1/main`  
Stage: `ASSEMBLED / TECHNICAL_PHASE_GATE_PASSED / FINAL_QC_NEXT`

## Continuity and timing
- Starts from the actual extracted final frame of Scene 02.
- Score authority: `L'Atmosphère.wav`.
- Duration: `98.000 s`; frame rate: `24 fps`; frames: `2352`; resolution: `1280x720`.

## User-approved picture basis
The current user explicitly approved the generated hero imagery. Scene 03 therefore preserves the eight approved hero plates `S3H01`–`S3H08` and does not regenerate their subjects or environments.

## Corrected movement implementation
The first effects pass used localized loops with `camera_motion:none`. The user then explicitly required copies of each hero at slightly different angles for movement. That correction is now implemented as eight source-locked matched-angle A/B pairs:

- A viewpoint: `-0.85°` Y-axis micro-yaw
- B viewpoint: `+0.85°` Y-axis micro-yaw
- overscan: `1.025x`
- focal model: `1700 px`
- no inpainting, no subject redraw, no new architecture, no translation wobble
- existing registered rain/reflection/haze/practical/access/elevator/display/traffic-state effects are retained inside the angle loops

Authoritative records: `ANGLE_PAIR_MANIFEST.json`, `FX_MANIFEST.json`, `project_fx/AE_S3_MATCHED_ANGLE.project-fx.json`, and its lock.

## Assembly02
`Scene03_ASSEMBLY02_ANGLE_FX_CAPTIONS.mp4`
- SHA-256 `3baa68d24c02e985f9c1c67396cec7ce8f9d1fc1940374837886e5402868efa5`
- exact `98.000 s`
- exact `2352` frames
- eight locked script shots at `192, 168, 360, 456, 408, 288, 264, 216` frames
- canon dialogue/captions burned in
- continuous Scene 03 score
- matched-angle GIF loops used as picture source for every shot

Assembly01 remains preserved as historical proof; Assembly02 supersedes it as the active technical candidate.

## Phase gate
The hero/shot proof requirement is satisfied by explicit user approval of the hero set. The matched-angle correction is a deterministic source-locked refinement, not new creative generation. Local geometry/frame/audio/caption QC is `PASS`. Project-local FX gate and exact GitHub production workflows must pass on this documentation commit before final-QC/mastering work.

## Drive recovery
Existing numbered recovery batches remain under `AE / Act I / Scene 03 / Recovery Batches`. Heavy Assembly02 media remains in the sandbox until the next cleanup/final checkpoint, per user storage policy.

## Next phase
`FINAL_QC`: inspect Assembly02 at shot boundaries and caption beats, verify no loop seam or continuity defect, then package the accepted Scene 03 candidate for integration with the Act I master. Final artistic/master acceptance remains a user decision.
