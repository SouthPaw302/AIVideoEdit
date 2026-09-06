# IronFlame handoff

## Where this project lives

- ChatGPT Project: **Video Creation**
- Repository: `SouthPaw302/AIVideoEdit`
- Active IronFlame branch: `song/ironflame-20260905-0216`
- IronFlame project folder: `projects/ironflame/`

This song, lyrics, visual direction, stills, production attempts, and discussion all came from the Video Creation Project. If working on IronFlame in a new chat/agent, recover that Project context first instead of treating this like a new generic music-video job.

## What failed

V3.4 is technically clean but artistically failed the intended workflow.

The delivered result is mostly a sequence of still images with transitions and subtle motion. The repo's actual effect vocabulary, loops, visible animation, spatial movement, and internal scene motion did not survive strongly enough into the final film. The story also reads weakly because storyboard scenes were allowed to become long held shots instead of being developed into visibly animated sequences.

Do **not** treat V3.4 as the creative target. It is only a recovery/reference artifact showing what was attempted and what not to repeat.

The failure was not missing infrastructure. The repo already contains the effects, production rules, prior successful work, and workflow. The mistake was allowing technical gating/verification to become the production itself instead of using the existing system to create visibly living shots.

## Where to look in GitHub before continuing

Start here and follow the existing material; do not add a new rule system for this handoff.

- `BIBLE.md` — canonical production philosophy and workflow.
- `projects/ironflame/PROJECT.md` — project identity and direction.
- `projects/ironflame/LYRICS.md` — song/lyrics context.
- `projects/ironflame/SHOT_LIST.md` — existing shot/story structure.
- `projects/ironflame/V2_HERO_SHOT_MAP.md` — hero image/scene mapping.
- `projects/ironflame/ASSET_MANIFEST.json` — known assets.
- `projects/ironflame/RENDER_HISTORY.md` — prior render history.
- `projects/ironflame/STATUS.md` — existing status/recovery notes.
- `projects/ironflame/FX_REQUIREMENTS.fx.json` — IronFlame effect declarations.
- `general/reusable/fx_v2/` — canonical FX2 registry/runtime/proof system.
- `general/reusable/generative-engine/` — spatial/generative implementations, including living parallax and related work.

Also inspect the branches/projects for the previously successful videos, especially **Silver Coin**, for the actual working production behavior: create/derive frames, animate them, make visible loops/effects, render, inspect, keep improving, then assemble.

## Exact source/media pointers

### IronFlame song audio

The canonical song source is already archived on this branch.

- Recovery instructions: `projects/ironflame/AUDIO_RECOVERY.md`
- Asset record: `projects/ironflame/ASSET_MANIFEST.json`
- Canonical WAV parts: `projects/ironflame/assets/audio/canonical-wav.parts/`
- Reconstructed filename: `Ironflame (Remastered).wav`
- SHA-256: `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`
- Working MP3 parts: `projects/ironflame/assets/audio/working-reference.parts/`

### IronFlame generated visual library

The generated IronFlame still library is recorded in `projects/ironflame/ASSET_MANIFEST.json` and lives under:

- `projects/ironflame/assets/stills/`
- `projects/ironflame/assets/reference/`
- `projects/ironflame/assets/analysis/`

The manifest records that the production stills were generated with OpenAI built-in image generation at 1664x936 / 16:9 and gives the exact per-shot filenames and hashes. Use those files as raw source material to derive animated shots; do not simply hold them on screen.

### Successful/example videos and source references

The important example is the **finished Silver Coin video the user uploaded back into the Video Creation Project for comparison**:

- Project-uploaded benchmark filename: `Silver_Coin_V8_FINAL_YouTube_720p24-1.mp4`
- This is the actual finished video to inspect for motion density, living-image treatment, loop behavior, transitions, pacing, and overall feel. It is a benchmark/reference, not a template to copy.

Silver Coin's durable GitHub project is:

- Branch: `song/silver-coin`
- Project: `projects/silver-coin/`
- Asset map: `projects/silver-coin/ASSET_MANIFEST.json`

That manifest also points to the ChatGPT Library originals used by Silver Coin:

- `Silver Coin  (Remastered).wav` — Library file ID `libfile_7726133c84a4819186af6e0bdd63ffc6`
- `imagine-d04b484c.mp4` — Library file ID `libfile_6403a0b255708191b9c1cbe2110887ce`
- `imagine-5558fc80.mp4` — Library file ID `libfile_50d6865c2c248191b98b6313aa813b3e`

GitHub keeps reduced visual recovery proxies for the two supplied Silver Coin motion references at:

- `projects/silver-coin/references/source-clips/imagine-d04b484c-github-reference.mp4`
- `projects/silver-coin/references/source-clips/imagine-5558fc80-github-reference.mp4`

The originals in the ChatGPT Project/File Library are the authoritative visual references; the tiny GitHub proxies are only for recovery/identification.

Also recover the successful prior productions and their project chats from the **Video Creation** Project when available, rather than assuming IronFlame V3.4 demonstrates the intended workflow.

## Continuation point

Do not spend time polishing the existing V3.4 slideshow-like master.

Recover the existing IronFlame images/assets and song context, then continue the video by using the repo as the toolbox it was built to be: derive multiple moving shots from the stills, use the existing effects and loops visibly, render and inspect the actual results, and build the story through the edit.

No new rules were added by this handoff. It only records where the project is, what failed, and where the next agent should look to continue correctly.
