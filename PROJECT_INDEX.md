# AIVideoEdit — Project Index

Every complete song/video production lives on exactly one canonical `song/<slug>` branch. `main` contains only the Bible, this index, templates, and reusable cross-project technology.

## Active

- `song/leave-it-by-the-door` — native-24 V2 complete and accepted as the picture baseline; V3 refinement active. Current direction: less global shake, more internal living-image loops, stronger animated fire/candles/embers/smoke/reflections, intro/outro for YouTube, final ZIP delivery. FX integration must use the centralized FX V2 precompile gate before compile/render.

## Reusable system state

- FX V2 has been promoted to `main/general/reusable/fx_v2/` and is part of the canonical production system. `fx/canonical-v2` is historical integration lineage, not the current source of truth.
- The current hard gate is `general/reusable/fx_v2/precompile_gate.py` schema v2. Production manifests must declare renderer inputs; lock verification reruns live deterministic evidence rather than trusting only stored top-level hashes.
- Canonical 3DGS/SuperSplat doctrine lives at `general/reusable/SPATIAL_3DGS_SUPERSPLAT.md`.
- Small cross-project utilities belong in `general/reusable/tools/`.

## Completed / delivered

- `song/irish-eyes` — **V1.3 FINAL COMPLETE / QC PASSED**. 16:9 / 1280x720 / 30 fps. Canonical artistic master `IRISH_EYES_V1_3_FINAL_YouTube_720p30.mp4`, SHA-256 `d0ace58c5e2b226cd08a928fc6f9b5ebcd3e2a949805adaa37fc94647ba603ae`, persistent Library ID `libfile_188ada3ee1c88191ae217eeb834402cd`. Canonical upload-with-outro `IRISH_EYES_V1_3_FINAL_UPLOAD_WITH_OUTRO_720p30.mp4`, SHA-256 `857b690b49e29724bcd625998e79f2fdc4873dc201c238628952ad4f53cc0763`, Library ID `libfile_0c67dfde60ec8191a37a97e520139892`. V1.3 preserves the V1.2 picture stream exactly and uses the newer user-supplied remaster. Point-in-time archive branch: `archive/video/irish-eyes`.
- `song/silver-coin` — V8 final complete / QC passed. Canonical final SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`.
- `song/ironflame` — V1 rendered/delivered; exact final MP4 archive identity remains unrecovered.

## Historical recovery

- `song/sigh-no-more` — partial recovery / historical Irish Eyes precursor; completed render not confirmed on that branch. The completed Irish Eyes film is `song/irish-eyes`.

## System rule

Song-specific media, storyboards, prompts, shot packages, manifests, QC, project docs and renders stay on the song branch.

Only generic reusable technology returns to `main/general/reusable/`.

For a new song:

1. create `song/<slug>` from `main`;
2. create `projects/<slug>/` on that branch using `projects/PROJECT_TEMPLATE.md`;
3. keep the entire production there;
4. promote reusable methods back to `main` only after they prove useful.

For Leave It recovery, open `song/leave-it-by-the-door` and read its project handoff/status files.

For reusable FX recovery, stay on `main` and read `general/reusable/fx_v2/README.md`, `PRECOMPILE_FX_GATE.md`, `registry.json`, and the proof records.

Read `BIBLE.md` for the production system.
