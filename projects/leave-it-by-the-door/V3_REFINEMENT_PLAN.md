# Leave It by the Door — V3 Refinement Plan

Branch: `song/leave-it-by-the-door`

## Goal

Turn the accepted native-24 V2 into the YouTube-ready final by increasing believable internal animation while reducing visible camera shake.

## Picture strategy

Keep:
- the 13 approved hero paintings and their story continuity;
- the 25-shot lyric-driven architecture;
- true native frame rendering;
- stable faces/characters;
- storm-to-warmth-to-dawn arc;
- V2 timing unless a scene-specific adjustment clearly improves flow.

Change:
- lower camera amplitude substantially;
- prefer locked/near-locked frames for tavern/fire scenes;
- increase independent internal movement in fire, candles, embers, smoke, water, reflections, rain, hair and cloth;
- use longer overlapping loop periods so motion does not advertise a short repeat;
- keep painterly surface temporally stable;
- use the canonical FX V2 runtime and hard gate.

## Scene families

### Storm / doorway
Use rain + water + smoke/mist + localized cloth/hair + slow cool light migration. Camera almost locked, with only a restrained depth push where useful.

### Hearth / tavern warmth
Make flame and light the hero motion. Couple flame geometry, practical-light breathing, smoke and reflections. Crowd/cloth/instrument movement remains subtle and localized.

### Burden / threshold
Use slow smoke/ash, small ember accents and wet reflection motion. Do not shake the scene to create drama.

### Celebration / dance
Use localized cloth/hair/crowd flow and warm moving practical light; preserve anatomy. Camera movement remains smooth and secondary.

### Dawn / release
Reduce storm density, soften smoke, transition palette toward dawn gold, add calm water/reflection movement and minimal camera drift.

## Intro

Add a short pre-song title section in the same painted world. It should feel integrated rather than like a generic graphic card.

Preferred behavior:
- 3–5 seconds;
- subtle internal fire/rain/light motion;
- clean title presentation;
- no abrupt loud visualizer behavior;
- transition naturally into the first song frame.

## Outro

Add a 5–8 second post-song YouTube end section after the artistic audio ending.

Preferred behavior:
- dawn/quiet-tavern visual world;
- gentle fire/light/water motion;
- room for `Mountainnoir` / thanks-for-watching presentation;
- preserve the artistic song ending before the separate post-roll card when possible.

## Technical target

- 1280×720 minimum YouTube master, true native 24 fps;
- H.264 high-quality delivery encode;
- original remastered song preserved through the artistic runtime;
- post-roll outro may extend container duration after the song;
- no 10 fps intermediates;
- no optical-flow interpolation used to fake base cadence;
- resumable shot-level rendering.

## Hard FX gate

Manifest: `V3_FX_MANIFEST.json`.

Before final render:
1. run `general/reusable/fx_v2/precompile_gate.py`;
2. save `V3_FX_LOCK.json`;
3. verify lock immediately before compile;
4. abort if any requested effect is no-op, unapproved, missing proof, or changed since lock creation.

## QC targets

V3 must pass:
- 0 black/damaged frames;
- no accidental near-duplicate cadence caused by low-rate intermediates;
- no obvious global shake in locked/near-locked scenes;
- no face/body warping from localized effects;
- visible flame motion wherever fire is meant to be alive;
- smoke/rain/water motion visibly independent rather than one whole-frame displacement;
- no short-loop seam that becomes obvious during normal playback;
- audio sync and exact artistic song runtime preserved;
- final intro/outro presentation checked at normal playback speed.

## Delivery

Create:
- artistic/master video;
- YouTube upload version with intro/outro as approved by final cut;
- final QC metadata/contact sheet;
- ZIP containing the upload master plus concise README/checksum.
