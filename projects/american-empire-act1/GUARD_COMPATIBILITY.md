# Movie-mode guard compatibility blocker

## Status
The Scene 01 project package and all 12 shot packages are prepared, but the current-main bootstrap/guard path cannot honestly PASS for this branch without a system-level compatibility change.

## Verified blockers in current main
1. `general/reusable/tools/production_guard.py` returns `production work must use song/<slug>` for every non-main branch that does not begin with `song/`.
2. `general/reusable/tools/narrative_guard.py` has the same `song/<slug>` branch restriction.
3. `MUSIC_ANALYSIS.json` validation only accepts song-oriented lyrics/genre/rhythm states and requires non-empty musical cues. Scene 01 is explicitly picture-first and the current user has deferred score/audio until picture lock; inventing tempo/genre/music cues would be false evidence.

## Current branch
`movie/american-empire-act1`

This is intentional movie-mode work and must not be silently renamed, spoofed as `song/...`, or passed to guards under a false branch name merely to obtain a green result.

## What is already ready
- six approved canonical Scene 01 hero panels, with exact hashes in `ASSET_MANIFEST.json`;
- locked storyboard and frame-followable 80-second script;
- 12 shot packages with media evidence, semantic motion regions, protected regions, and canonical FX assignments;
- rejected prior FX pass documented with named defects;
- candidate FX plan for visible 2.5D, region-limited weather/reflections, foreground/internal motion, and source-coupled lighting.

## Required before another production proof
Movie-mode must receive an honest bootstrap/guard path. Do not bypass the bootstrap, spoof the branch, invent music analysis, or render another full scene outside the contract.

No new FX implementation is required for Scene 01. The blocker is orchestration/contract compatibility, not missing visual capability.
