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

## Continuation point

Do not spend time polishing the existing V3.4 slideshow-like master.

Recover the existing IronFlame images/assets and song context, then continue the video by using the repo as the toolbox it was built to be: derive multiple moving shots from the stills, use the existing effects and loops visibly, render and inspect the actual results, and build the story through the edit.

No new rules were added by this handoff. It only records where the project is, what failed, and where the next agent should look to continue correctly.
