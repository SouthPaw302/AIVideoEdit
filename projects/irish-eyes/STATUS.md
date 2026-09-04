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

Native-cadence extraction completed:

- `frame_000001.png` through `frame_000953.png`
- `FRAME_MANIFEST.csv`
- working extraction path: `/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

Raw extraction is working media; canonical selected frames, shot-package manifests, proofs and reusable results are checkpointed on this song branch/archive system as production proceeds.

## Governing rules

Follow `projects/irish-eyes/PRODUCTION_EXECUTION_PLAN.md` and `projects/irish-eyes/USER_DIRECTIVES.md`.

Locked rules:

- tool/plugin/reusable-stack preflight before writing new effect code;
- Cloudflare Wrangler/R2/Workers/Pages are canonical support options when available/authenticated;
- zoom/perception changes are authored cinematography, not Ken Burns defaults;
- real source footage/frames remain the identity and reality anchor;
- generated support elements may extend environments, transitions, surreal memory space, textures, optical material and missing story beats when they improve the film;
- preserve Brandi's photographic identity;
- use actual 3DGS only when real source coverage supports it; see `3DGS_PIPELINE.md`;
- use hybrid NeRF, 2.5D, living-image motion, water/reflection systems, weather/atmosphere, prism/halation, memory echoes, transformative transitions and music-directed behavior where artistically appropriate;
- proof and QC effects before long-form assembly;
- professional editorial/color/texture finishing after picture lock;
- scan the actual final export before delivery.

## Hero-frame batch 01

See `projects/irish-eyes/HERO_FRAME_BATCH_01.md`.

Initial candidates:

- frame 97 — arrival / reality anchor;
- frame 291 — portrait / sunlight;
- frame 420 — hair / sun / waterfront hero;
- frame 436 — transition geometry;
- frame 614 — dramatic backlit memory;
- frame 743 — return / human anchor;
- frame 840 — introspective closing buildup;
- frame 936 — closure.

## Effect proof P01 — Breeze Memory

Shot package: `IE_P01_BREEZE_MEMORY`, source frame 420.

P01 V3 rendered and QC'd:

- 4.0 s / 30 fps / 360x640 proof;
- 120 frames;
- 0 black frames;
- SHA-256 `bcb66330bc072fbea61e4df3aca0b0e2fab8be0c1c8c6421195f0c95370b4867`.

Implemented: source-derived depth travel, protected subject separation, independent water, motivated Gaussian-shaped light fields, water light response, haze, hair/dress micro-motion, localized temporal echo, prism, source-derived portal behavior, halation and proof grade.

**Magic Gate: REVISE.** More dimensional than earlier versions, but still primarily reads as an animated photograph rather than a sufficiently strong spatial revelation.

See `EFFECT_PROOF_P01_V3.md`.

## Effect proof P02 — Reflection Portal

Shot package: `IE_P02_REFLECTION_PORTAL`, real source frames 270–315, hero frame 291.

P02 V1 rendered and QC'd:

- 4.5 s / 30 fps / 360x640 proof;
- 135 frames;
- 0 black frames;
- SHA-256 `770592871c3fda3f41211d3ae5d3bcde72d31fd25001c4bee96b1dcb91dfc422`.

Implemented: slowed real source motion, independent water, source-derived mirrored-sky reflection field, Gaussian-shaped light shafts, matched water glint, source-derived memory/reflection clone, localized prism, off-axis perception move and portal-bloom transition.

**Magic Gate: REVISE.** Temporal life is much stronger than P01, but the final perception dive lands too much on foreground subject/crop instead of cleanly entering the water portal.

See `EFFECT_PROOF_P02_REFLECTION_PORTAL.md`.

## 3DGS path clarified

See `projects/irish-eyes/3DGS_PIPELINE.md`.

For true 3D Gaussian Splatting, real video frames must first pass Structure-from-Motion/camera recovery and a separate splat trainer. PlayCanvas/SuperSplat is the preferred inspection/edit/camera-animation/video-render stage once compatible splat data exists. Do not confuse this with Gaussian-shaped light fields.

## Exact next production action

Do not assemble the final film.

Next proof target: a more favorable dramatic source window, especially around frame 614 or 743, using retained real motion plus a visibly authored atmospheric/perception event. Primary candidates:

1. **Storm Revelation** — cloud displacement, independent water, Gaussian light opening, rain/lightning/reflection response, dimensional camera travel, then return to real light;
2. **Reflection Portal V2** — fix camera target so the reflection actually becomes the destination;
3. **3DGS viability test** — isolate the strongest background/parallax window, test camera/SfM stability first, train only if the source supports it.

**No final Irish Eyes video until multiple distinct shot packages independently pass the Magic Gate.**
