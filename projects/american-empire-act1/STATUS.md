# American Empire Act I — Status

Branch: `song/american-empire-act1-scene1`
Canonical parent story branch: `movie/american-empire-act1`
Current stage: `STORYBOARD_LOCKED`
Director Brain: v2
Production mode: hybrid, implemented shot-by-shot primarily as living comic panels.

## Canon
The six approved Scene 01 hero panels are protected source canon. Do not regenerate or replace them. Their exact SHA-256 hashes are recorded in `ASSET_MANIFEST.json` and were verified against the original active-workspace copies.

### Canonical-byte materialization status
The current Git branch does **not** contain the six canonical PNG bytes at the manifest paths under `scenes/scene-01/hero_frames/`; it contains only their identities, hashes, dimensions, roles and shot-package references. The previously rendered recovery proof is likewise referenced only by an `active-workspace://` locator in `PROOF01_QC.json` and is not committed as a GitHub artifact or release asset.

This remains a fail-closed production blocker. No agent may regenerate lookalike replacements, substitute other images, recover canon from a rejected/compressed proof, or claim a new representative proof from metadata alone. Before another render, the exact original canonical PNG bytes must be materialized into the production workspace and verified against all six SHA-256 values in `ASSET_MANIFEST.json` (or recovered from a byte-identical persistent artifact if one is later located).

## Proof05 — REJECTED BY CURRENT USER
Reviewed artifact: `Scene01_LAYERED_FX_PROOF05.mp4`, 8.0 seconds, 720x404, 24 fps.

Current-user verdict: **FAILED — REDO IT.**

Proof05 is rejected production media. It must not be promoted, used as an accepted baseline, used to satisfy the representative proof gate, or used as a surrogate source for the missing canonical hero frames.

Redo policy:
- return to the six canonical hero panels, not Proof05 frames;
- build actual multiplane depth with independently moving real foreground/midground layers rather than a weak whole-picture drift;
- make foreground/internal motion materially readable while keeping Claire/phone/window geometry locked;
- constrain rain/reflection behavior to exterior/window/glass semantic regions only;
- tie practical illumination and lightning to visible scene sources with coherent falloff/decay rather than generic brightness changes;
- keep camera movement subordinate to scene motion;
- captions must remain readable without obscuring faces, phone, lightning or foreground action;
- do not carry Proof05 forward as the foundation of Proof06.

## Score
`Pre-dawn in Paris.wav` is ingested as the real Scene 01 score.
- Source duration: 84.36s
- Measured tempo: ~68 BPM
- Estimated tonal center: C minor
- Scene master use: 0.0–80.0s with fade beginning at 77.5s
- Measured structural turn: ~58.35s, synchronized to the lightning/revelation beat
See `SCORE_INGEST.json`, `SCORE_MAP.md`, and `MUSIC_ANALYSIS.json`.

## Captions
Captions are required before picture lock. Exact wording and working timings are recorded in `CAPTION_PLAN.md` and `CAPTION_TIMING.json`. The first revelation caption clears before the ~58.35s lightning/music turn, and S12 remains a clean text-free final hold.

## Shot-package preparation
All 12 Scene 01 shot packages exist under `shot_packages/S01` through `S12`. Each records canonical hero media evidence, semantic motion regions, protected regions, and assigned existing FX IDs. Interior packages explicitly constrain rain to window/outside regions.

## Rejected earlier full FX pass
The previous full FX pass is rejected and must not be promoted. Named defects:
- rain visibly present inside the room;
- no convincing 2.5D foreground/midground/background separation;
- weak or absent foreground/internal motion;
- lighting animation not convincingly tied to scene light sources;
- global effect application instead of semantic region assignment.

## Current direction
No more image generation. Work only from the approved six hero panels and existing repo capabilities. Use the ingested score and captions as active production media. Proof05 is rejected; the next proof is a clean rebuild from canon after the original bytes are restored and hash-verified.

## Prepared next proof
`PROOF_PLAN.md` remains the governing four-part representative proof using H01, H02, H04/H06 and H05. The redo must visibly demonstrate stronger practical 2.5D separation, motivated foreground/internal motion, region-limited weather/reflections, source-coupled lighting, identity stability and caption readability before FX lock or another full Scene 01 assembly.

## Guard compatibility
This child branch uses the existing `song/...` namespace expected by current-main production/narrative guards while preserving `movie/american-empire-act1` as the canonical parent story branch. Do not discard or rename the movie branch.
