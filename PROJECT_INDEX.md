# AIVideoEdit — Project Index

Every complete song/video production lives on exactly one canonical `song/<slug>` branch. `main` contains only the Bible, this index, templates, and reusable cross-project technology.

## Active

- `song/irish-eyes` — active storyboard-linked preview / shot-package production. Do not assemble the full movie yet.

## Completed / delivered

- `song/silver-coin` — V8 final complete / QC passed. Canonical final SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`.
- `song/ironflame` — V1 rendered/delivered; exact final MP4 archive identity remains unrecovered.

## Historical recovery

- `song/leave-it-by-the-door` — partial recovery.
- `song/sigh-no-more` — partial recovery; completed render not confirmed.

## System rule

Song-specific media, storyboards, prompts, shot packages, manifests, QC, project docs and renders stay on the song branch.

Only generic reusable technology returns to `main/general/reusable/`.

For a new song:

1. create `song/<slug>` from `main`;
2. create `projects/<slug>/` on that branch using `projects/PROJECT_TEMPLATE.md`;
3. keep the entire production there;
4. promote reusable methods back to `main` only after they prove useful.

Read `BIBLE.md` for the production system.