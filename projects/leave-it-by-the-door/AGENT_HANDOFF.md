# Leave It by the Door — Agent Handoff

Branch: `song/leave-it-by-the-door`

## Current state

Native-24 V2 is complete and is the accepted picture baseline. Do not return to the old 10 fps intermediate workflow.

User feedback on V2: **better / awesome**, but wants the next pass to feel more like premium long-form animated-image YouTube videos:
- less camera/global shaking;
- more loop-safe internal motion;
- stronger animated fire, candles, embers, smoke and reflections;
- keep the painterly images stable and human-authored in feel;
- avoid obvious AI morphing or whole-image wobble;
- add intro and outro suitable for YouTube;
- final delivery must be wrapped in a ZIP.

## Canonical reusable FX

The centralized repository-wide runtime is now present on this branch at:
`general/reusable/fx_v2/`

Read:
- `general/reusable/fx_v2/AGENT_HANDOFF.md`
- `general/reusable/fx_v2/registry.json`
- `general/reusable/fx_v2/PRECOMPILE_FX_GATE.md`

Production must use the hard precompile gate. Do not substitute local placeholder effects if a canonical approved implementation exists.

Currently approved FX suitable for V3 include:
- `FX2-MOTION-002` localized living flow
- `FX2-MOTION-003` water flow
- `FX2-ATM-001` advected smoke
- `FX2-ATM-002` rain plane
- `FX2-FIRE-001` living flame
- `FX2-FIRE-002` embers
- `FX2-LIGHT-001` practical light breath
- `FX2-LIGHT-002` moving light field
- `FX2-SURFACE-001` temporal canvas lock

Transitions remain proof-gated unless their registry status has changed. Do not bypass that status.

## V3 objective

Use V2's 25-shot native-24 architecture as the base, but rebuild/refine selected shots with internal motion weighted above camera motion.

Primary visual targets:
1. stable characters/faces;
2. richer flames/candles/embers;
3. smoke and atmosphere with continuous advected motion;
4. water/wet reflections and storm layers moving independently;
5. hair/cloth/crowd micro-motion confined to shot-specific masks;
6. restrained camera travel only where it improves depth;
7. intro/outro integrated with the film's visual world;
8. final master QC + ZIP package.

## Read next

- `STATUS.md`
- `EFFECTS_PLAN.md`
- `V3_REFINEMENT_PLAN.md`
- `V3_FX_MANIFEST.json`
- `REFERENCE_MOTION_TARGETS.md`
- `FULL_V2_QC.json`
- `scripts/render_full_native24_v2.py`

## Delivery rule

Do not call V3 final until:
- FX manifest passes precompile gate;
- generated FX lock verifies immediately before render;
- final export is scanned for black/freeze/duplicate/temporal artifacts;
- the result is visually checked for excessive shake and missing effects;
- YouTube upload master and ZIP are created.
