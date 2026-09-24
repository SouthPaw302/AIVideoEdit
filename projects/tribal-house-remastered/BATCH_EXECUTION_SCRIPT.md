# Batch Execution Script — Tribal House Remastered

This is the production-following script for the active branch. It complements `SCRIPT.json`; the operational unit is a **batch**, not a storyboard panel.

## Mandatory batch cycle

For every batch:

`10 MAIN SOURCE IMAGES -> SAVE/HASH -> GITHUB + DRIVE -> SMALL FX GATE -> 10 SECONDARY FX/LOOP/GIF/MOTION VARIANTS -> SAVE/HASH -> GITHUB + DRIVE -> QC/LOCK -> NEXT BATCH`

Rules:
- Do not silently regenerate accepted media.
- Main source images establish picture/story coverage.
- Secondary media remains derived from the accepted batch world; it does not introduce a new story or identity.
- Resolve canonical FX from the current-main FX resolver before authoring the small FX gate.
- Internal scene motion first; camera second.
- Protect faces, hands, anatomy, hero identity, architecture, horizons and critical geometry as applicable.
- Every generated/derived asset gets a lifecycle state and durable locator.
- Heavy media goes to Drive/storage; GitHub stores manifests, hashes, IDs, QC, prompts/recipes and branch state.
- Do not advance to the next batch until the current batch's source + FX/secondary state is persisted and reviewed.

## Current position

**Batch 01 is the set already generated in this session — both the main Invocation source images and the secondary FX/emergence variants belong to Batch 01.**
They are not Batch 02.

The next operation is to normalize/persist Batch 01, run its small FX gate, lock it, then begin Batch 02.

## Batch 01 — Invocation — 00:00-00:30
Story function: The ritual chamber wakes from near-black. Ember, geometry, smoke and ash gather into the first restrained silhouette of the fire-spirit.

Main media: 10 source images: ember seed -> geometry wakes -> smoke gathers -> incomplete silhouette.

Secondary media: Secondary FX/motion candidates derived from the same Batch 01 world: fire, embers, smoke, glow, localized atmosphere; no new world/identity.

Protected: chamber topology, ritual circle, hero silhouette once visible, anatomy, lighting direction

Exit action: Persist all Batch 01 main + secondary media, run small FX gate, record PASS/REJECT per asset and effect, then lock Batch 01.

## Batch 02 — Gathering — 00:30-00:58
Story function: The awakened world answers. Distant ritual presences, circular movement, dust, cloth and torchlight assemble around the same sacred center.

Main media: 10 source images expanding the same world with perimeter figures, circles, dust, torchlight and ritual response.

Secondary media: 10 loop/GIF/motion or FX derivatives from approved Batch 02 source media.

Protected: hero continuity, faces/hands if visible, architecture, circle geometry

Exit action: FX gate Batch 02, then lock and continue.

## Batch 03 — First Manifestation — 00:58-01:46
Story function: The central spirit gains recognizable identity while remaining one coherent entity; close, mid and wide coverage establish the hero.

Main media: 10 source images establishing the hero identity library across compatible compositions.

Secondary media: 10 motion/loop/FX derivatives preserving exact hero identity.

Protected: face, anatomy, hero silhouette, world identity

Exit action: FX gate Batch 03, then lock identity canon.

## Batch 04 — Procession / Passage — 01:46-02:14
Story function: The spirit moves through thresholds, corridors, temple paths and reflective volcanic spaces.

Main media: 10 source images showing forward passage through the same mythic world.

Secondary media: 10 motion/loop/transition derivatives; bounded parallax/camera only after internal motion.

Protected: hero identity, axis, architecture, horizon, lighting direction

Exit action: FX gate Batch 04, then lock passage coverage.

## Batch 05 — Possession / Peak Build — 02:14-03:18
Story function: The environment becomes fully alive: fire, dust, cloth, smoke, reflected light and ritual energy escalate around the hero.

Main media: 10 source images with the densest ceremonial escalation and strongest controlled visual energy.

Secondary media: 10 FX/motion derivatives emphasizing independent materials and impact without global warping.

Protected: face, hands, anatomy, hero silhouette, critical props, architecture

Exit action: FX gate Batch 05, then lock peak-build media.

## Batch 06 — Threshold Crossing — 03:18-03:48
Story function: The spirit crosses from the earthbound ritual world into a more mythic plane through fire/water/reflection/gate imagery.

Main media: 10 source images for the crossing and palette/spatial state change.

Secondary media: 10 transition/loop/FX derivatives using reflection, fog, light and bounded depth.

Protected: hero identity, gate geometry, waterline/reflection geometry

Exit action: FX gate Batch 06, then lock crossing.

## Batch 07 — Apotheosis — 03:48-04:16
Story function: The spirit reaches full mythic manifestation in monumental, iconic compositions.

Main media: 10 apex hero images with wide, mid and iconic silhouette coverage.

Secondary media: 10 FX/motion derivatives with controlled lift, firelight, atmosphere and restrained camera.

Protected: face, anatomy, hero identity, symmetry, architecture

Exit action: FX gate Batch 07, then lock apex canon.

## Batch 08 — Release — 04:16-04:50
Story function: Power stabilizes. Motion becomes smoother, less aggressive and more fluid while the same world remains intact.

Main media: 10 source images easing from peak intensity into elevated calm.

Secondary media: 10 subtle living-scene loop/FX derivatives with reduced pulse intensity.

Protected: hero identity, world topology, lighting continuity

Exit action: FX gate Batch 08, then lock release.

## Batch 09 — Afterglow / Exit — 04:50-05:05
Story function: Ash, horizon glow, smoke and remaining embers settle into transformed stillness.

Main media: 10 closing-source options or fewer only if the repo/user explicitly authorizes a reduced closing batch; default remains 10.

Secondary media: 10 subtle loop/FX derivatives or long-hold variants from approved closing media.

Protected: final silhouette, horizon, architecture, end-state calm

Exit action: FX gate Batch 09, then assembly/proof path.

## Completion sequence after Batch 09
Batch locks -> representative moving proofs -> FX lock -> full assembly -> actual-export mode-aware QC -> Drive/final archive -> branch handoff.
