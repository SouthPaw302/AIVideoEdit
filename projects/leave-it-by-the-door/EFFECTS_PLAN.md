# Leave It by the Door — Effects Plan

Branch: `song/leave-it-by-the-door`

## Baseline

Native-24 V2 is the accepted picture base. The V3 pass is a refinement, not a restart.

User direction:
- reduce camera/global shake;
- increase internal living-image loops;
- animate fire/candles/embers/smoke/reflections more convincingly;
- keep the images painterly, stable, and human-authored in feel;
- avoid generic AI wobble/morphing;
- add YouTube intro/outro.

## Canonical FX V2 integration

Use `general/reusable/fx_v2/` rather than recreating local substitutes.

Approved production IDs currently selected for V3:

| ID | Role in V3 |
|---|---|
| `FX2-MOTION-002` | localized hair/cloth/crowd/instrument living motion |
| `FX2-MOTION-003` | water, puddle, wet-floor and reflection movement |
| `FX2-ATM-001` | smoke/fog/steam advection |
| `FX2-ATM-002` | storm/rain exterior planes |
| `FX2-FIRE-001` | true animated hearth/candle flame geometry + glow |
| `FX2-FIRE-002` | embers/sparks, restrained and scene motivated |
| `FX2-LIGHT-001` | practical fire/lantern light breathing |
| `FX2-LIGHT-002` | slow moving warm/cool light migration |
| `FX2-SURFACE-001` | scene-fixed painterly/canvas temporal stability |

These are gated through `V3_FX_MANIFEST.json`.

## Camera rule

No default shake. Camera movement is subordinate to internal scene motion.

Preferred camera behavior:
- locked or near-locked shots for fire/candle/community scenes;
- very slow asymmetric pushes where depth benefits;
- restrained lateral parallax only when foreground/background separation is convincing;
- no per-frame random jitter;
- no whole-frame wobble used as a substitute for animation.

## Loop design

Loop-friendly motion must use continuous phase/advection rather than visible clip restart:
- flame tongues and light pulse use overlapping non-identical periodic components;
- embers wrap/reseed deterministically;
- smoke/fog advects continuously;
- rain positions wrap outside frame boundaries;
- water uses phase-continuous displacement;
- hair/cloth localized flow stays inside masks and never controls faces/hands.

Long shots may combine multiple loop periods so the scene does not read as a short repeating GIF.

## Fire treatment

Fire is a primary V3 upgrade.

For hearth/candle/lantern shots, combine:
1. `FX2-FIRE-001` living flame in shot-specific ROI;
2. `FX2-LIGHT-001` practical light breathing tied to the same source;
3. `FX2-FIRE-002` sparse embers where physically motivated;
4. `FX2-ATM-001` subtle rising smoke/heat atmosphere;
5. optional wet/reflection response from `FX2-MOTION-003` on nearby floors/tables/windows.

The flame and its illumination must feel coupled. Do not draw orange blobs over the picture.

## Exterior storm treatment

Use independent layers:
- rain plane;
- moving sea/water;
- smoke/fog/mist as atmosphere where appropriate;
- localized cloth/hair motion;
- slow moving cool light field;
- minimal camera drift.

The exterior should feel alive even when the camera is almost locked.

## Transitions

The centralized transition family exists, but transition IDs remain blocked until they have their own rendered proof/QC approval.

Until an individual transition passes the hard gate:
- preserve V2's proven transition behavior where already accepted;
- do not mark an unapproved FX2 transition as production-ready;
- do not bypass the gate by embedding a placeholder under another name.

## Precompile rule

Before V3 final rendering:

`python general/reusable/fx_v2/precompile_gate.py --manifest projects/leave-it-by-the-door/V3_FX_MANIFEST.json --lock-out projects/leave-it-by-the-door/V3_FX_LOCK.json`

Immediately before compile/render, verify the lock again with the same gate tool.

No gate pass = no final V3 compile.
