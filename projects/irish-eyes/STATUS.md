# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: frame scan / living-asset build. No full-movie assembly yet.

Source restored in current runtime:

- `Brandi South Florida 2017.mp4`
- 1280x720
- 30 fps
- 31.766344 s
- 953 source frames

Native-cadence extraction completed in current runtime:

- `frame_000001.png` through `frame_000953.png`
- `FRAME_MANIFEST.csv`
- working extraction path: `/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

Raw extraction is working media; canonical selected frames, shot-package manifests, proofs and reusable results must be checkpointed on this song branch/archive system as production proceeds.

## Governing plan

Follow `projects/irish-eyes/PRODUCTION_EXECUTION_PLAN.md`.

Key rules now locked:

- tool/plugin/reusable-stack preflight before writing new effect code;
- use zoom and perception changes as authored cinematography, not generic Ken Burns motion;
- mix real footage/stills with generated support content when it improves the film;
- preserve Brandi's photographic identity;
- build stills into moving mini-scenes using 3DGS when viable, hybrid NeRF, 2.5D, living-image motion, reflection/water systems, weather/atmosphere, prism/halation, memory echoes, transformative transitions and music-directed behavior;
- proof and QC effects before long-form assembly;
- finish the assembled film with the complete editorial/color/texture stack in `EDITORIAL_FINISHING_STACK.md`;
- scan the actual final export before delivery.

## Tool preflight completed

Current GitHub connector surface exposes extensive repository and workflow-management functions (search, branches, commits, trees, blobs, file writes, comparisons, PR/issues, Actions logs/artifacts/retries). It is useful for recovery/checkpointing but is not itself a native video-effects engine.

Current repo reusable implementations include Silver Coin motion/effect/QC/NeRF tools, continuous 2.5D, and Irish Eyes restoration/water treatment.

Optional plugin fallbacks discovered include Cloudinary, CloudConvert, Seedance-based AI Video Maker, sync.labs, Pixlie and Krikey. Do not install/use paid/external services by default; use only when a specific production need justifies them.

## Exact next action

Scan the 953 extracted source frames and select the first hero-frame batch. For each selected moment record:

- frame number;
- timestamp;
- storyboard/narrative role;
- neighboring motion window;
- intended camera/perception move;
- intended effect family;
- whether generated support/environmental material is needed.

Then begin building the first real shot packages and short effect proofs.
