# IronFlame V3 — Artistic Review Checkpoint 02

Branch: `song/ironflame-20260905-0216`

## Why this checkpoint exists

The first full set of V3 shot-package blocks passed basic export QC, but contact-sheet review exposed a separate artistic failure mode: the late film reused the same few AI compositions too often. That would create a repetitive slideshow feel even if every block remained technically motion-clean.

This checkpoint records the correction before production assembly.

## Review finding

Late V3 contact-sheet review showed repeated use of:

- `crystalline_cosmic_encounter.png`
- `cosmic_mind_and_silent_witness.png`
- `cosmic_connection_through_light.png`
- `luminous_ai_spirit_in_her_hand.png`

The material remained in the correct visual family, but repetition was too high for a directed long-form film.

## V3.1 attempt

A more varied late-story pass was rendered from existing AI hero media only. No new portal/gate imagery was introduced.

The first revised 02:02–02:47 block failed shot-proof motion QC at the current threshold with two >=1.5 second low-motion/freeze detections. It was rejected and not promoted.

## V3.2 correction

Three late shot-package blocks were rebuilt with stronger but still restrained internal motion and explicit 16:9 camera travel:

### 02:02–02:47
Narrative states:
1. `crystalline_cosmic_encounter.png`
2. `celestial_ai_spirit_encounter.png`
3. `cosmic_recognition_in_blue_light.png`

Library master:
`/AIVideoEdit/IronFlame_V3_20260905/IRONFLAME_V3_2_SEQUENCE_122_167_1080p24.mp4`

QC:
`/AIVideoEdit/IronFlame_V3_20260905/SEQUENCE_122_167_V32_QC.txt`

Result: no black events and no >=1.5 second freeze events at the current shot-proof threshold.

### 02:47–03:30
Narrative states:
1. `cosmic_connection_through_light.png`
2. `ethereal_ai_spirit_and_silhouette.png`
3. `cosmic_encounter_orb_between_worlds.png`

Library master:
`/AIVideoEdit/IronFlame_V3_20260905/IRONFLAME_V3_2_SEQUENCE_167_210_1080p24.mp4`

QC:
`/AIVideoEdit/IronFlame_V3_20260905/SEQUENCE_167_210_V32_QC.txt`

Result: no black events and no >=1.5 second freeze events at the current shot-proof threshold.

### 03:30–04:04.680
Narrative states:
1. `cosmic_mind_and_silent_witness.png`
2. `meditation_beneath_the_cosmic_guardian.png`
3. `cosmic_connection_through_light.png`

Library master:
`/AIVideoEdit/IronFlame_V3_20260905/IRONFLAME_V3_2_SEQUENCE_210_244_1080p24.mp4`

QC:
`/AIVideoEdit/IronFlame_V3_20260905/SEQUENCE_210_244_V32_QC.txt`

Result: no black events and no >=1.5 second freeze events at the current shot-proof threshold.

## Motion language used in V3.2

- native 1920x1080 / 24 fps only;
- no vertical clip framing or blurred/mirrored portrait filler;
- restrained explicit 16:9 camera push/drift;
- internal contour/ribbon flow bounded to existing bright structures;
- existing warm/orb material breathes from the preserved song control bus;
- crystalline shimmer remains localized;
- state changes use contour/ribbon transport, not a magic portal/gate;
- no unrelated particles, smoke, rain, fire, or fantasy threshold effects.

## Gate status

These remain **shot-package proofs**, not production-gate approval and not final assembly.

Do not claim FX precompile approval from these renders. Project-level `FX_REQUIREMENTS.fx.json` and `fx.lock.json` are not created until the shot/effect set is mature enough for the repository's production compile stage.

Any reusable FX V2 ID used later in the production manifest must still obey `general/reusable/fx_v2/PRECOMPILE_FX_GATE.md` and the canonical registry status/proof rules.

## Next action

Continue artistic and temporal review of the earlier V3 blocks, especially 00:00–02:02, for repetition, narrative progression, transition quality, and visible internal motion. Revise failed shot packages before any full-timeline assembly.
