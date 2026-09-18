# Handoff — IronFlame reference-driven production

Active branch: `song/ironflame-cleanroom-20260917`.

The later reference-driven production supersedes the earlier Molten Cartography route. Do not restart Molten Cartography and do not treat its browser proof as final authority.

Active visual authority:
- `REFERENCE_MANIFEST.json`
- Drive reference video: `01_reference/reference_video.mp4`
- Drive movement pack: `04_generated_stills/IronFlame_unique_movement_variants.zip`
- 12 source-derived movement sections covering 244.68 seconds.

Recovery facts:
- The repository movement ZIP was discovered to be a broken ~15 KB placeholder while the verified Drive pack is ~3.8 MB.
- A local recovery render proved the Drive media, section timing, and synchronized audio are usable.
- That render contains bounded movement/crossfades and passed technical container QC only.
- It did **not** pass the FX gate and is not the finished production.

Authoritative project state remains:
- stage: `SHOT_PACKAGES_BUILT`
- `shot_proofs_accepted=false`
- `mode_aware_proofs_accepted=false`
- `fx_lock_verified=false`
- `assembly_complete=false`
- `final_qc_passed=false`

Exact next action: remain in **Step 4 — Shots**. Build and wire the project FX manifest, create proof media showing visible temporal/pixel changes, run the FX v2 precompile gate, generate and re-verify `fx.lock.json`, then proceed to Assemble only after the gate passes.
