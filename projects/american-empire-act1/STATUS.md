# American Empire Act I — Status

Branch: `movie/american-empire-act1`
Current stage: `STORYBOARD_LOCKED`
Director Brain: v2
Production mode: hybrid, implemented shot-by-shot primarily as living comic panels.

## Canon
The six approved Scene 01 hero panels are protected source canon. Do not regenerate or replace them. Their exact SHA-256 hashes are recorded in `ASSET_MANIFEST.json` and verified against the active workspace copies.

## Shot-package preparation
All 12 Scene 01 shot packages now exist under `shot_packages/S01` through `S12`. Each package records real hero media evidence, semantic motion regions, protected regions, and assigned existing FX IDs. Interior packages explicitly constrain rain to window/outside regions.

The project deliberately remains at `STORYBOARD_LOCKED` rather than falsely claiming `SHOT_PACKAGES_BUILT`, because current-main bootstrap/guards cannot honestly validate a `movie/...` branch yet. See `GUARD_COMPATIBILITY.md`.

## Rejected proof
The previous full FX pass is rejected and must not be promoted. Named defects:
- rain visibly present inside the room;
- no convincing 2.5D foreground/midground/background separation;
- weak or absent foreground/internal motion;
- lighting animation not convincingly tied to scene light sources;
- global effect application instead of semantic region assignment.

## Current direction
No more image generation. Work only from the approved six hero panels and existing repo capabilities.

Scene 01 now also requires:
- captions/subtitles from `CAPTION_PLAN.md` before picture lock;
- a new instrumental Suno score following `SCORE_BRIEF.md`;
- score ingest and real music analysis before claiming music evidence.

No invented BPM, section, or music-analysis evidence is permitted before the actual score file is received.

## Prepared next proof
`PROOF_PLAN.md` defines a four-part representative proof using H01, H02, H04/H06 and H05. The proof must visibly demonstrate 2.5D separation, motivated foreground motion, region-limited weather/reflections and source-coupled lighting before FX lock or another full Scene 01 assembly.

## Current blocker
Current-main `production_guard.py` and `narrative_guard.py` reject non-`song/` production branches. Adding a real score resolves the music-evidence side once ingested, but the `movie/...` branch-prefix restriction remains a separate guard compatibility issue unless the production is moved/mirrored to an allowed branch name or the guard is extended.