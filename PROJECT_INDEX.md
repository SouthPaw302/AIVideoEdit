# AIVideoEdit — Project Index

Every complete song/video production lives on exactly one canonical `song/<slug>` branch. `main` contains only the Bible, this index, templates, and reusable cross-project technology.

## Active

No currently indexed active production.

## Completed / delivered

- `song/irish-eyes` — **V1.2 FINAL COMPLETE / QC PASSED**. 16:9 / 1280x720 / 30 fps. Canonical artistic master `IRISH_EYES_V1_2_FINAL_YouTube_720p30.mp4`, SHA-256 `a7bc3cd9674b8eaf6a55c28dc6898dc136afc5c668bd95409dce06dc9f10dba7`, persistent Library ID `libfile_f35a75d11c748191ae3d25960667b0a9`. Canonical upload-with-outro SHA-256 `edae4a9b65a23c705228d58a41aa1e6eba14a378e3096657f6f22d62c9f3e362`. Point-in-time archive branch: `archive/video/irish-eyes`.
- `song/silver-coin` — V8 final complete / QC passed. Canonical final SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`.
- `song/ironflame` — V1 rendered/delivered; exact final MP4 archive identity remains unrecovered.

## Historical recovery

- `song/leave-it-by-the-door` — partial recovery.
- `song/sigh-no-more` — partial recovery / historical Irish Eyes precursor; completed render not confirmed on that branch. The completed Irish Eyes film is `song/irish-eyes`.

## System rule

Song-specific media, storyboards, prompts, shot packages, manifests, QC, project docs and renders stay on the song branch.

Only generic reusable technology returns to `main/general/reusable/`.

For a new song:

1. create `song/<slug>` from `main`;
2. create `projects/<slug>/` on that branch using `projects/PROJECT_TEMPLATE.md`;
3. keep the entire production there;
4. promote reusable methods back to `main` only after they prove useful.

For recovery of Irish Eyes V1.2, open `song/irish-eyes` and read `projects/irish-eyes/STATUS.md`, `FINAL_MASTER.md`, and `FINAL_QC.md`.

Read `BIBLE.md` for the production system.
