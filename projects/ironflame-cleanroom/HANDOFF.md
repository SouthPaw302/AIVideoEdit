# Handoff — IronFlame assembled FX/depth candidate

Active branch: `song/ironflame-cleanroom-20260917`.

The uploaded IronFlame video is now the accepted source library and continuity backbone. Do not replace its character, environment, sequence, timing, or audio.

Current production state:
- stage: `ASSEMBLED`
- shot proofs accepted: true
- mode-aware proofs accepted: true
- FX lock verified: true
- assembly complete: true
- final QC/creative acceptance: pending

What was added:
- canonical song-level FX requirements + verified `fx.lock.json`;
- 12 duplicate-derived depth/GIF support loops from original/moved still pairs;
- section-specific atmospheric/light/reflection/spark/heat support;
- FFmpeg production backend recorded in `RENDER_RECIPE.json`;
- before/after source integrity evidence in `REFINEMENT_QC.json`.

Assembled export identity:
- 244.680 s, 1280x720, 24 fps;
- original AAC audio copied bit-for-bit;
- SHA-256 `7ae715b7fbe254e802b51a00c0f1ea5641bec3e51b54a17136df4111c982eddc`.

Do not mark final acceptance automatically. Present the complete export to the user; if accepted, advance to `FINAL_QC_PASSED`, then archive.
