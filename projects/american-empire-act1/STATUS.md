# American Empire Act I — Status

Branch: `song/american-empire-act1-scene1`
Canonical parent story branch: `movie/american-empire-act1`
Current stage: `STORYBOARD_LOCKED`
Director Brain: v2
Production mode: hybrid, implemented shot-by-shot primarily as living comic panels.

## Canon
The six approved Scene 01 hero panels are protected source canon. Do not regenerate or replace them. Their exact SHA-256 hashes are recorded in `ASSET_MANIFEST.json` and verified against the active workspace copies.

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
All 12 Scene 01 shot packages exist under `shot_packages/S01` through `S12`. Each records real hero media evidence, semantic motion regions, protected regions, and assigned existing FX IDs. Interior packages explicitly constrain rain to window/outside regions.

## Rejected proof
The previous full FX pass is rejected and must not be promoted. Named defects:
- rain visibly present inside the room;
- no convincing 2.5D foreground/midground/background separation;
- weak or absent foreground/internal motion;
- lighting animation not convincingly tied to scene light sources;
- global effect application instead of semantic region assignment.

## Current direction
No more image generation. Work only from the approved six hero panels and existing repo capabilities. Use the ingested score and captions as active production media.

## Prepared next proof
`PROOF_PLAN.md` defines a four-part representative proof using H01, H02, H04/H06 and H05. The proof must visibly demonstrate 2.5D separation, motivated foreground motion, region-limited weather/reflections, source-coupled lighting, identity stability and caption readability before FX lock or another full Scene 01 assembly.

## Guard compatibility
This child branch uses the existing `song/...` namespace expected by current-main production/narrative guards while preserving `movie/american-empire-act1` as the canonical parent story branch. Do not discard or rename the movie branch.
