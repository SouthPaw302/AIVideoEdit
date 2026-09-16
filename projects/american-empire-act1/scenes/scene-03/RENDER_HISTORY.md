# Scene 03 Render History

## 2026-09-15 — Pre-production and score lock

- Locked `L'Atmosphère.wav` to 98.000 editorial seconds / 2352 frames at 24 fps.
- Locked storyboard, script and canon caption timing.
- Preserved Scene 02 terminal frame as Scene 03 continuity anchor.

## 2026-09-15 — Hero and Assembly01 pass

- Generated eight Scene 03 hero plates and received explicit user approval of the hero imagery.
- Built initial localized diegetic FX loops.
- Rendered `Scene03_ASSEMBLY01_HERO_FX_CAPTIONS.mp4`.
- Assembly01 was technically valid but its loop manifest correctly recorded `camera_motion:none`.

## 2026-09-15 — User-directed matched-angle correction

The user required copies of each hero with slightly different angles for movement. Rather than generatively redraw the approved heroes, the correction uses deterministic source-locked projection:

- hero A: `-0.85°` Y-axis micro-yaw
- hero B: `+0.85°`
- 1.025x overscan / 1700 px focal model
- existing localized FX retained before viewpoint projection
- no identity or environment regeneration

Created eight matched-angle pairs and eight corrected GIF loops.

## Assembly02 — approved pre-production basis

Rendered `Scene03_ASSEMBLY02_ANGLE_FX_CAPTIONS.mp4`.

- SHA-256: `3baa68d24c02e985f9c1c67396cec7ce8f9d1fc1940374837886e5402868efa5`
- 1280x720
- 24 fps
- exactly 98.000 s
- exactly 2352 frames
- canon captions burned in
- continuous score
- exact script shot frame counts preserved

The current user accepted Assembly02 as good pre-production: the feel, character continuation and city design are the foundation for further work.

## Assembly03 — effects-completion proof

Built directly from Assembly02 using the same eight shot spans. Added/strengthened coherent rain/reflection response, corridor/access-light progression, elevator route progression, lobby state progression, traffic/transit synchronization and public-system progression.

`Scene03_ASSEMBLY03_EFFECTS_PROOF.mp4`
- SHA-256: `77e2ea51c3ea22ed3c1b3dab4c46a64d9f99ae71bf301fd25bfa866246584438`
- exactly 98.000 s / 2352 frames
- Drive ID: `1sNbipscEqAKSoCQX_FpljMKsrc7mlbXI`

Assembly03 remains the effects rollback reference.

## Assembly04 — artifact-clean effects review

Built from Assembly03 while suppressing production/debug corner-note contamination. The same eight storyboard images still dominated the picture structure, so it remained a transitional review pass rather than the desired final media architecture.

`Scene03_ASSEMBLY04_CLEAN_ACTION_PASS.mp4`
- SHA-256: `07bccc75f5e54b6b89b0142c90c3d7224cd976d2a91afce1030997f9219a5bb7`
- exactly 98.000 s / 2352 frames
- Drive ID: `1udCJWNJMpK2oSdSir6Qfwmcndzx6p9Og`

## Assembly05 — multi-image GIF review

User correction: Scene 03 has a full media pool and must not be reduced to eight enlarged storyboard cards. The storyboard remains the eight-beat timing/narrative authority, while final picture coverage may use multiple approved media assets inside each beat.

Assembly05 therefore uses 29 existing clean media segments across the eight locked beat durations. Explicitly rejected media is excluded. No new artwork was generated for this pass.

For every still segment:
- deterministic A/B slight-movement companion frames were created from the same source image;
- a real GIF motion asset was rendered;
- the GIF was used as shot media rather than represented by a production label;
- production/debug storyboard labels are absent from final picture media.

`Scene03_ASSEMBLY05_MULTIIMAGE_GIF_FX_REVIEW_COMPACT.mp4`
- SHA-256: `3969e3a12020d5f7d7cd71a80ba0a8f19833ba55d164188d03fd86d6e8eaa9b1`
- 1280x720
- 24 fps
- exactly 98.000 s
- exactly 2352 frames
- 29 media segments
- existing Scene 03 audio retained
- media mapping recorded in `ASSEMBLY05_MEDIA_PLAN.json`

Assembly05 is the current visual review candidate. Assembly02 remains the approved pre-production rollback reference until Assembly05 or a successor receives explicit user acceptance.
