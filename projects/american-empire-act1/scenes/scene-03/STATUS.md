# Scene 03 — Status

Branch: `project/american-empire-act1/scene-03`
Canonical project root: `project/american-empire-act1/main`
Stage: `APPROACH_LOCKED / STORYBOARD_LOCKED / SCORE_LOCKED / SCRIPT_LOCKED / MEDIA_GENERATION_NOT_STARTED`
Direction authority: `user_directed`
Production mode: `hybrid`

## Current continuity anchor
Scene 03 begins immediately from Scene 02 shot `S2-10`: Claire has moved away from the window, gathered an approved essential, retained her phone and committed to leave while the controlled systems transition continues outside.

Planning inheritance of this terminal state does not by itself promote any still-unapproved Scene 02 picture candidate to accepted master.

## Locked Scene 03 structure

- Title: `The City Was Ready`
- Duration: `98.000 seconds`
- Frame rate: `24 fps`
- Frame range: `0-2351`
- Total frames: `2352`
- Score: `L'Atmosphère.wav`
- Score SHA-256: `96ee4e0f5e34e0955272ab9e5327f1850254e82978e79aa9d9422e9898316b25`
- Script: `SCRIPT.md` + frame-followable `SCRIPT.json`
- Score map: `SCORE_ANALYSIS.json`
- Eight primary hero compositions remain exactly as defined in `MEDIA_PLAN.json`.

Shot timing:

1. `S3-01 / S3H01` — frames `0-191` — departure state
2. `S3-02 / S3H02` — frames `192-359` — apartment threshold
3. `S3-03 / S3H03` — frames `360-719` — hallway coordination
4. `S3-04 / S3H04` — frames `720-1175` — elevator already knows
5. `S3-05 / S3H05` — frames `1176-1583` — lobby handoff
6. `S3-06 / S3H06` — frames `1584-1871` — street threshold
7. `S3-07 / S3H07` — frames `1872-2135` — public proof
8. `S3-08 / S3H08` — frames `2136-2351` — forward into Paris

## Audio archive

The full mix and 12-stem package are archived in:

`AE / Act I / Audio & Scores`

- `AE_Scene03_LAtmosphere_Master.wav` — Drive file ID `1hOhmd5xt6nQvslYE-271Yg2SUskCJ64E`
- `AE_Scene03_LAtmosphere_Stems.zip` — Drive file ID `1Rv-60STTQY_kOZ91O01p8GaJP_ib0170`

The score is instrumental. Lead and backing vocal stems contain no meaningful vocal content. The full mix is the editorial authority; stems are available for smooth system/Foley space without hard music cuts.

## Dialogue and captions

No new dialogue is locked for Scene 03. Do not invent explanatory dialogue, narration or intelligible public announcements. Captions are not required unless dialogue is explicitly approved later; any later dialogue requires a caption-timing revision before assembly.

## Media status

No Scene 03 production images or video continuations have been generated yet.

Google Drive durable archive folder:

`AE / Act I / Scene 03`

All future generated media, including accepted, alternate, rejected, storyboard/contact-sheet, QC and proof material, must be archived according to the project handoff directive.

## Runtime gate and known compatibility fault

The American Empire branch policy explicitly authorizes:

`project/american-empire-act1/scene-03`

The current generic repository production guard still rejects non-`song/*` production branches. GitHub Actions successfully checked out and attempted to bootstrap Scene 03, then failed specifically on that branch-name incompatibility before media generation.

Do not bypass the guard and do not move Scene 03 into a song branch.

Next action:

1. add narrow fail-closed support on repository `main` for project branches declared by a project's `PROJECT_BRANCHES.md`;
2. synchronize that reusable fix into `project/american-empire-act1/main` and `project/american-empire-act1/scene-03`;
3. rerun bootstrap plus production/narrative/recut guards;
4. after PASS, generate the eight named hero compositions in script order, beginning with `S3H01`.
