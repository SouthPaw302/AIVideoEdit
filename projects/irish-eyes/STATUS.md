# Irish Eyes — Current Status

Branch: `song/irish-eyes`

## Current state

Production mode: frame scan / living-asset build / effect-laboratory proofing. **No full-movie assembly yet.**

Source restored in current runtime:

- `Brandi South Florida 2017.mp4`
- 1280x720 container / 720x1280 displayed portrait orientation
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
- include Cloudflare Wrangler/R2/Workers/Pages in that preflight when available and authenticated; see `projects/irish-eyes/CLOUDFLARE_WRANGLER.md`;
- use zoom and perception changes as authored cinematography, not generic Ken Burns motion;
- use a hybrid visual philosophy: real source footage/frames remain the identity and reality anchor, while generated support elements may extend environments, transitions, surreal memory space, textures, optical material and missing story beats when they improve the film;
- preserve Brandi's photographic identity;
- build stills into moving mini-scenes using 3DGS when viable, hybrid NeRF, 2.5D, living-image motion, reflection/water systems, weather/atmosphere, prism/halation, memory echoes, transformative transitions and music-directed behavior;
- proof and QC effects before long-form assembly;
- finish the assembled film with the complete editorial/color/texture stack in `EDITORIAL_FINISHING_STACK.md`;
- scan the actual final export before delivery.

## Tool preflight completed

Current GitHub connector surface exposes extensive repository and workflow-management functions (search, branches, commits, trees, blobs, file writes, comparisons, PR/issues, Actions logs/artifacts/retries). It is useful for recovery/checkpointing but is not itself a native video-effects engine.

Current repo reusable implementations include Silver Coin motion/effect/QC/NeRF tools, continuous 2.5D, and Irish Eyes restoration/water treatment.

Cloudflare Wrangler is now a canonical project capability for large-binary persistence and production support. Preferred first use is R2 for large source/frame/proof/render assets when GitHub is the wrong storage layer. Workers/Pages and other Cloudflare services are available only when a concrete production need justifies them. The current ChatGPT container does not expose `wrangler` on PATH, so no Cloudflare operation is claimed as completed in this runtime.

No useful dedicated Cloudflare ChatGPT plugin was discovered in the current plugin directory search. Optional media fallbacks discovered include Cloudinary, CloudConvert, Seedance-based AI Video Maker, sync.labs, Pixlie and Krikey. Do not install/use paid/external services by default; use only when a specific production need justifies them.

## Hero-frame batch 01 complete

See `projects/irish-eyes/HERO_FRAME_BATCH_01.md`.

Initial selected production candidates:

- frame 97 — arrival / reality anchor;
- frame 291 — portrait / sunlight;
- frame 420 — hair / sun / waterfront hero;
- frame 436 — transition geometry;
- frame 614 — dramatic backlit memory;
- frame 743 — return / human anchor;
- frame 840 — introspective closing buildup;
- frame 936 — closure.

## Effect-laboratory proof 01

Shot package: `IE_P01_BREEZE_MEMORY`, source frame `frame_000420.png`.

Working package created locally with:

- source frame;
- subject mask / alpha;
- inpainted background plate;
- depth field;
- source-derived 2.5D motion proof;
- water shimmer / halation / prism / temporal treatment iteration;
- internal QC samples.

**Magic Gate result: REVISE.**

The current proof demonstrates real dimensional motion and visible treatment, but it still reads too much like a sophisticated animated photograph. It is not yet approved for timeline use. See `projects/irish-eyes/MAGIC_GATE_01.md`.

## Exact next action

Iterate P01 to V3 using the canonical Silver Coin / Irish Eyes effect language:

1. moving Gaussian light fields anchored to the real cloud/sun opening;
2. stronger protected background depth travel;
3. independent water/reflection movement;
4. asymmetric virtual-camera push rather than uniform zoom;
5. localized prism/temporal behavior around hair, water and bright edges;
6. reflection or bright-cloud portal exit test;
7. identity and temporal QC.

If P01 V3 still fails the magic threshold, move the primary effect-laboratory target to `frame_000614.png` rather than forcing the wrong frame.

**Do not assemble the final Irish Eyes video until multiple distinct shot packages have passed the magic gate.**
