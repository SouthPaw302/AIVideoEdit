# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V6 full-length music-directed living-painting render is complete and visually QC-reviewed. Production is now in refinement/review rather than storyboard generation.

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

## Music-directed motion language in the full render

The real master drives:

- smoothed energy -> camera and practical-light intensity
- transient peaks -> micro zoom / light accents
- brightness proxy -> atmospheric lift
- section identity -> crop speed, angle amplitude and palette response

Verse language stays slower and intimate. Choruses widen and move harder. The bridge cools/drifts. The final chorus gets the strongest camera amplitude before returning to the calm forest image.

## Reusable loops/effects active

- 2D Gaussian atmosphere drift
- tavern practical-light breathing
- wet-road reflection shimmer
- slow crop/angle camera loops
- clean music-bound dissolves
- candle-flare transition
- pigment soften transition
- shadow wipe
- fog bridge
- final light lift

Terminology guard: the Gaussian atmosphere is 2D image-space Gaussian compositing, **not** true 3D Gaussian Splatting.

## Recoverable section rendering

The CPU runtime could render the imagery quickly but a single monolithic full encode could exceed an execution window. V6 therefore introduced a preferred recovery method: render six global-time chunks, concatenate the intermediate video, then perform one final 720p/audio encode.

Because each chunk evaluates the original global song timestamp, music envelopes, camera curves and the two halves of transitions remain continuous across chunk boundaries.

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
- V6 full render: current review target.

## Exact next action

1. Preserve the full V6 render as the current review target.
2. Continue archiving the accepted hero-image set and the full-render scripts/metadata to GitHub.
3. Use user review to identify specific timing, image, transition or effect changes rather than restarting the visual direction.
4. Regenerate only affected sections using the six-chunk recovery workflow.
5. Keep expanding reusable production/effect methods when they prove useful.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume without the original chat.