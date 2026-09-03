# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V6 remains the picture-locked review base. V7 post-effects delivery is **rejected as an effects implementation** after direct V6/V7 frame comparison. Next work is a frame-by-frame/localized effects pass over the existing approved paintings and V6 edit; do not regenerate source art.

## Canonical visual rule

**Recreate Silver Coin from the visual language contained in the two user-supplied sample videos themselves.**

- Sample A: `imagine-d04b484c.mp4`
- Sample B: `imagine-5558fc80.mp4`
- Sample A's blonde flower-crowned woodland woman defines protagonist identity, face, hair, crown, costume family, painted surface, palette and world.
- The old V5 tavern/laborer storyboard may inform narrative history only. Its visual designs are rejected.

## V6 completed visual set used in the full render

The current full render intentionally favors the strongest accepted paintings instead of filling every narrative beat with weaker art.

High-resolution girl-first source paintings used:

- woodland / silver coin portrait
- woodland path / village reveal
- workers at sunset
- twilight inn exterior
- first-toast tavern scene
- clapping / rhythm tavern scene
- fiddler scene
- communal dance scene

Strong images recur through different crops, scale paths, lateral movement, angle paths, palette response and effect intensity where appropriate.

## Full V6 render

Artifact: `Silver_Coin_V6_Full_MusicDirected_720p.mp4`

- Duration: **207.416667 s**
- Canonical master duration: 207.44 s
- Video: **1280x720 H.264, 12 fps**
- Audio: **48 kHz stereo AAC, 256 kb/s**
- Bytes: **69,744,424**
- SHA-256: `20670789b2d76ac7c924a539ca2e55375f5abc8b9cef9d48af99d925192793f3`
- Visual QC: **PASS** across section/contact-sheet review

See `V6_FULL_RENDER_META.json`.

## V7 post-effects review — REJECTED

A YouTube-oriented V7 delivery was produced from V6 with title/end treatment, global grade/bloom, crop/zoom behavior and delivery conversion. Direct frame comparison showed that this did **not** create the localized living-painting motion requested by the user.

Observed failure mode:

- most scene geometry remained the same as V6;
- visible change was dominated by global color/bloom/title treatment;
- supposed loops were largely parameter modulation, not independently animated hair, foliage, flames, smoke, crowd, fabric or reflections;
- camera changes were crop/scale changes rather than convincing depth-aware camera movement;
- the 24 fps delivery mostly duplicated/interpolated a 12 fps base instead of adding new frame-level animation;
- therefore V7 must not be described as the completed effects pass.

The user specifically requested a return to the earlier single-image living-cover method: render frame-by-frame, create real effect/loop assets, composite them over the locked image/video, then edit the effected shots together.

## Required V8 correction — post/edit only, no new source images

Preserve the V6 picture edit and accepted paintings. Build actual reusable effect layers/loops and render them into the frames before assembly.

Priority effect families already supported by the repository:

- 2.5D parallax / layered camera travel
- cinemagraph micro-loops
- hair / flower-crown / foliage / cloth drift
- candle and fire flicker
- smoke / fog / rain / ash / dust
- moving practical light and shadows
- reflected fire / wet-road shimmer
- Gaussian bloom / localized light fields
- lightning / strong light accents where musically motivated
- beat/transient flashes and glints
- coin-object transitions
- painterly pigment / temporal-light transitions
- audio-reactive intensity changes

Render effects as real visual layers or frame sequences, QC them independently, then composite them with the existing paintings/V6 edit. Do not rely on tiny global parameter changes and call them loops.

## Music-directed motion language retained

The real master may still drive:

- smoothed energy -> camera and practical-light intensity
- transient peaks -> visible light/zoom/impact accents
- brightness proxy -> atmospheric lift
- section identity -> crop speed, angle amplitude, loop density and palette response

But the music control must produce visible frame-level consequences.

## Recoverable section rendering

Keep the six-section/global-time recovery method introduced by V6. Each musical section should be effect-rendered independently, QC'd, then concatenated so one bad loop or transition does not require a full-song rerender.

See `V6_SECTION_RENDER_RECOVERY.md`.

## Canonical source recovery

The branch contains lightweight full-duration visual proxies for both sample clips:

- `projects/silver-coin/references/source-clips/imagine-d04b484c-github-reference.mp4`
- `projects/silver-coin/references/source-clips/imagine-5558fc80-github-reference.mp4`

The canonical originals remain the uploaded 560x560/24fps files identified by SHA-256 in `ASSET_MANIFEST.json`.

Canonical audio:

`Silver Coin  (Remastered).wav`  
SHA-256: `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`

## Historical versions

- V5.1 / V5.2: technically valid but aesthetically rejected image direction.
- V6 opening proof: first validation of the girl-first image direction and music-cued camera/effects grammar.
- V6 full render: current picture-locked base.
- V7 YouTube post pass: **rejected for insufficient localized/frame-level effects**; keep only as a diagnostic experiment.

## Exact next action

1. Preserve V6 picture lock and source paintings.
2. Reuse repository effect methods and the earlier living-cover philosophy.
3. Create true effect-loop assets / frame sequences first.
4. Apply them frame-by-frame to each V6 musical section.
5. QC visible motion/effects before final assembly.
6. Assemble YouTube title/end only after the effected picture pass is genuinely visible.
7. Checkpoint every effect asset, preset, timing map and section render to GitHub.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume without the original chat.