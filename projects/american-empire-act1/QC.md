# Scene 01 QC

Current status: **NOT PASSED**. The previous FX render was rejected by the current user and cannot advance production state.

## Required representative-proof checks
The next proof must be visually inspected, not merely decoded or measured.

### Living-scene / hybrid checks
- **Internal motion visible:** at least one foreground/internal material region moves independently in applicable shots.
- **2.5D readable:** foreground, midground and background show relative displacement; a viewer should perceive depth without being told an effect is active.
- **Weather motivated:** exterior rain stays exterior; interior rain is forbidden except on/through explicit window/glass regions.
- **Reflection separation:** reflection motion is confined to reflective regions and does not deform Claire.
- **Light-source coupling:** practical/lightning changes visibly originate from plausible sources and affect nearby surfaces coherently.
- **Identity stability:** Claire's face, hands, body silhouette and comic linework remain stable.
- **Camera restraint:** no whole-frame wobble or generic drift substitutes for scene motion.
- **Comic integrity:** halftone/ink/value structure survives animation without crawling or smearing.

## Technical checks
- native target cadence: 24 fps;
- no black/frozen accidental frames;
- no broken joins or loop snaps inside long holds;
- correct 16:9-ish source framing and no unintended crop of critical composition;
- every claimed effect traceable to `FX_MANIFEST.json` and its shot package;
- current precompile/FX gate must pass before `FX_LOCKED`.

## Acceptance rule
Technical metrics are evidence only. `SHOT_PROOFS_ACCEPTED` remains false until the current user accepts the representative visual proof.
