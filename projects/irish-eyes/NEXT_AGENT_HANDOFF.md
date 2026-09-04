# Irish Eyes — Next Agent Handoff

Branch: `song/irish-eyes`
Current production format: **16:9 landscape / 1280x720 / 30 fps**
Current phase: **landscape master build → 187.12 s rough-cut preparation**
Final master status: **BLOCKED until rough-cut, finishing, and full export QC pass**

Dated snapshot of this state:
`projects/irish-eyes/HANDOFF_2026-09-04_0324.md`

This document supersedes the old portrait-era/V4-only handoff.

## Creative law

Irish Eyes is a dynamic long-form YouTube music film, not a visualizer, slideshow, generic AI-video montage, or one source clip with barely visible effects.

Use a hybrid source-derived cinema workflow:

- real Brandi footage/frames = identity and emotional truth;
- real photography/environmental plates preferred where possible;
- 2.5D, depth separation, optical flow, temporal motion, compositing, shaders, water/reflection systems, volumetrics, prism/halation, camera/perception moves and spatial methods are encouraged;
- selective generated support is allowed for surreal extensions/transitions/environments/missing beats when it genuinely improves the film;
- do not replace Brandi with generated lookalikes;
- reject drifted generated content that changes the person/location/style;
- effects must be visibly present and artistically integrated;
- no final master until the magic is verified in sequence.

## Final-format law

**Finished film and YouTube packaging are 16:9 landscape only.**

Working/final picture target:
- 1280x720
- 30 fps
- 16:9

The source MP4 is encoded 1280x720 with a `-90°` display matrix. The correct displayed capture is portrait. Turning off rotation makes Brandi sideways and is not a landscape solution.

Landscape production uses authored reframing:
- real-source horizontal closeups/medium crops;
- subject/environment separation;
- source-derived background extension;
- 2.5D/environment reconstruction where useful;
- true widescreen environmental memory shots;
- **no blurred sidebars or pillarboxed phone-video treatment**.

Portrait effect-lab renders are reference/proof assets only.

Read `LANDSCAPE_MASTER_SPEC.md`.

## Primary source / extracted frames

Source: `Brandi South Florida 2017.mp4`

Known properties:
- 31.766344 s
- 30 fps
- 953 source frames

Current runtime extraction path:
`/mnt/data/irish_eyes_branch/projects/irish-eyes/source_frames/brandi_south_florida_2017/`

Contents:
- `frame_000001.png` … `frame_000953.png`
- `FRAME_MANIFEST.csv`

Do not assume `/mnt/data` survives into another chat. GitHub docs/manifests are the source of truth. Verify local media before using paths.

## Story / duration

Picture duration: **187.12 s / 03:07.12**.

Read:
- `LYRIC_FILM_MAP.md`
- `ROUGH_CUT_16X9_PLAN_V1.md`

The full story is already mapped from 00:00 to 03:07.12:
- Act I: real South Florida / Irish Eyes / Spanish Hair / memory opening;
- Act II: glasses→water→road, rain-glass travel, warm window/candle, dark lake/ridge;
- Act III: return to Brandi, deep-memory loop, water→lake→road→window→eyes;
- Act IV: progressive return to reality, effects fall away, last look, water/light ending.

The remastered `Irish eyes (Remastered).wav` is **not currently mounted**. Existing section timing comes from prior measured boundaries. Do not claim exact transient/phrase sync or audio-reactive timing until the WAV is restored.

## Magic Gate rule

A rendered asset is not accepted just because the render completed.

Promote only after:
1. technical QC — no black/frozen/corrupt frames, bad borders, accidental repeats, broken masks;
2. artistic QC — must feel cinematic/scene-native, not like an effect pasted over a still.

Rejected assets stay rejected.

## Current approved / provisional families

- P02 Reflection Portal V3 — KEEP
- P04 Spatial Entry V2 — KEEP
- P05 Still Here / Time Dilation — KEEP
- P06 Opening Arrival — KEEP
- P07 Hair Memory — KEEP
- P08 Return Human Anchor — KEEP
- P10 Eyes Within / Sunglasses Portal — KEEP
- T01 Sun / Water Memory Gate — KEEP
- T02 Water / Reality Return — KEEP
- P11 Water → Wet Road Memory V4 — KEEP provisional
- P12 Road Travel / Rain Glass V2 — KEEP provisional
- P13 Warm Window / Candle Memory V2 — KEEP provisional
- P14 Dark Lake / Ridge Horizon V2 — KEEP provisional
- T03 Glasses → Water → Road → Water V2 — KEEP provisional

Proven language includes source-derived spatial entry, altered perception/zoom, 2.5D depth differential, independent water/sky motion, real hair/dress temporal movement, face-protected trails, water/reflection portals, sunglasses-horizon portal, prism/refraction, motivated halation, Gaussian-shaped light fields, rain-glass, warm-window/candle memory, dark-lake/ridge/mist memory, and reality↔memory optical gates.

## Literal 3DGS decision

This clip was tested for true Gaussian Splatting viability. Stable waterfront background is mostly explained by planar/global camera motion with only ~1–2 px residual at proof resolution.

Decision:
- do not force/train true 3DGS from this clip;
- reserve real 3DGS/SuperSplat for deliberate translated/arc/multiview footage;
- continue source-derived depth/perception here;
- Gaussian-shaped light fields remain allowed but must not be mislabeled 3DGS.

Read `3DGS_VIABILITY_2026-09-04.md`.

## Rejected lineage — do not reintroduce silently

- P01 Breeze Memory V3 — animated-photograph feel
- P03 Storm Revelation V1–V4 — never crossed Magic Gate
- P09 Memory Clone Refraction V1–V3 — ghost/apparition feel
- early P02 portals — camera stretched/landed on subject
- generated clean-plate/support attempts that changed person/location/style
- P10 V2 — glowing white goggles
- P11 V1–V3 — fake lights / wedge / procedural road geometry
- T03 V1 — portal spread too broadly across Brandi's face
- L18 Full-Body Waterfront V1 — duplicate-person background failure

## 16:9 landscape master library

Read:
- `LANDSCAPE_MASTER_LIBRARY_V1.md`
- `LANDSCAPE_NATIVE_BATCH_01.md`

Earlier L00–L12 1280x720 continuity components remain working assets.

### Newly rendered landscape-native real Brandi masters

**L15 Arrival Real V1 — KEEP**
- SHA `38a2213e3bdc9521f4b072a5f0dd922470a76772008ee3016836efe2764c12d4`
- `landscape_16x9/masters/IE_L15_ARRIVAL_REAL_16x9_V1.mp4`

**L16 Irish Eyes Portrait V1 — KEEP**
- SHA `41e4e7157a62189731a2f8f14e461ad04e70f45e4de706bef58846bbada35745`
- `landscape_16x9/masters/IE_L16_IRISH_EYES_PORTRAIT_16x9_V1.mp4`

**L17 Hair Real Motion V1 — KEEP**
- SHA `1614cf2934039f80505e46db12b77f500feb970f8c64f1b7dfef3627e1f800d3`
- `landscape_16x9/masters/IE_L17_HAIR_REAL_MOTION_16x9_V1.mp4`

**L18 Full-Body Waterfront 2.5D V1 — REJECTED**
- giant duplicate Brandi remained in background.

**L18 Full-Body Waterfront 2.5D V2 — QC HOLD**
- rebuilt from clean real waterfront + one real Brandi alpha
- SHA `08ef5521787fa935ab3aca157a1c5ce8b5b4ec665782777d5cdaf3a33cf231e1`
- `landscape_16x9/masters/IE_L18_FULL_BODY_WATERFRONT_25D_16x9_V2.mp4`

**L19 Last Look Real V1 — KEEP**
- SHA `95d7b61aef858553f5e269cebde08619c68dbce037db62e9b96937df46d0d763`
- `landscape_16x9/masters/IE_L19_LAST_LOOK_REAL_16x9_V1.mp4`

Batch QC sheet:
`landscape_16x9/qc/LANDSCAPE_MASTERS_L15_L19_QC.jpg`

## Continuity proof

Current landscape continuity proof:
`landscape_16x9/continuity/IRISH_EYES_LANDSCAPE_CONTINUITY_REEL_V4_16x9.mp4`

- 1280x720
- 30 fps
- ~55.47 s

It proves the visual language survives landscape reframing. Portrait continuity reels are reference-only.

## YouTube packaging

Current 16:9 files:
- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_INTRO_16x9_V2.mp4`
- `landscape_16x9/youtube_packaging/IRISH_EYES_YOUTUBE_OUTRO_16x9_V2.mp4`

Rules:
- intro lives over the song opening;
- artistic film ends at 187.12 s on water/light;
- outro is separate post-film YouTube packaging;
- portrait intro/outro versions are obsolete/reference-only.

## Exact next action

Do this in order:

1. visually clear or revise **L18 V2**;
2. render 1280x720 landscape-native environmental masters:
   - **L20 Water → Road**
   - **L21 Road / Rain-Glass Travel**
   - **L22 Warm Window / Candle**
   - **L23 Dark Lake / Ridge**
3. assemble the first **187.12 s 16:9 visual rough** from `ROUGH_CUT_16X9_PLAN_V1.md`, using L15–L23 plus approved transition families;
4. preserve long real-Brandi passages so the edit does not become an effects reel;
5. restore the remastered WAV before claiming exact song sync;
6. inspect the rough for repetition, pacing, transition overuse, visual fatigue, crop quality and real-Brandi percentage;
7. add ancestry/architecture only if the rough reveals a genuine story gap;
8. **do not deliver the final master yet**.

## Mandatory finishing after picture lock

Read `EDITORIAL_FINISHING_STACK.md`.

Required final pass:
- shot-to-shot exposure and white-balance matching
- skin-tone and pink-dress continuity
- saturation/vibrance refinement
- contrast/black-level shaping
- highlight recovery
- selective sky/water/skin work
- halation/bloom refinement
- prism/refraction cleanup
- denoise where needed
- sharpening/detail recovery
- grain/texture matching
- stabilization/motion consistency
- transition cleanup
- full final-export QC

The film is not finished when the shots are concatenated.

## Tool-first / resilience rule

Before creating new rendering code:
1. inspect `general/reusable/` canonical effects;
2. inspect existing Irish Eyes assets/tools;
3. use GitHub tools/connectors;
4. inspect available ChatGPT tools/plugins;
5. use Cloudflare/Wrangler/R2 when available for heavy media/storage/review infrastructure;
6. only then create new custom tooling if required.

GitHub is the canonical brain for manifests, hashes, decisions, QC and recovery. Large media may be runtime/external but must remain recoverable through documented lineage.

Do not install/spend on paid services merely because they exist.

## User directives that remain binding

- dynamic long-form YouTube music film, not visualizer/slideshow
- effects must be artistically visible
- real footage remains central
- selective generated support is allowed, but no generic AI-video takeover
- use zoom/perception/spatial tricks artistically
- keep GitHub updated frequently
- scan actual exports before claiming success
- no final master until magic and full structure are verified
- final format is 16:9 landscape

## Read these first in the next chat

1. `NEXT_AGENT_HANDOFF.md`
2. `STATUS.md`
3. `LANDSCAPE_MASTER_SPEC.md`
4. `LANDSCAPE_MASTER_LIBRARY_V1.md`
5. `LANDSCAPE_NATIVE_BATCH_01.md`
6. `ROUGH_CUT_16X9_PLAN_V1.md`
7. `LYRIC_FILM_MAP.md`
8. `EDITORIAL_FINISHING_STACK.md`
9. `3DGS_VIABILITY_2026-09-04.md`
10. dated snapshot `HANDOFF_2026-09-04_0324.md`

## Recovery warning

Old references to the portrait V4 master are historical lineage, not the active final format. The active production is now 16:9 landscape.

Never claim runtime-local media exists until verified in the new runtime. If missing, recover/re-render it from documented source/manifests instead of inventing a path or silently substituting another asset.
