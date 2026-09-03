# Silver Coin — Source Video Reference Canon

**Locked:** 2026-09-03  
**Branch:** `song/silver-coin`

## User directive

The two supplied sample videos are the canonical visual source for the next Silver Coin rebuild.

The previous tavern/laborer storyboard art is **not** the visual target. It may be consulted only for broad lyric/narrative ideas.

## Canonical references

### Sample A — primary character/world anchor

Original filename: `imagine-d04b484c.mp4`  
Original SHA-256: `8f14739f3eb4f7e7dcc639dfe9fab398623f4a7b5c31ce8b2c0131fab89e6c9c`  
Original: 560x560, 24 fps, ~6.041667 s

GitHub visual recovery proxy:

`references/source-clips/imagine-d04b484c-github-reference.mp4`

**Opening scene canon:** blonde woman, flower crown, luminous pale/golden hair, deep green woodland, wildflowers and foliage, soft naturalistic face, romantic painted fabric, luminous skin and hair against darker vegetation, visibly hand-painted / Pre-Raphaelite surface.

This woman becomes the recurring Silver Coin protagonist unless the user changes the direction.

### Sample B — supporting world/motion anchor

Original filename: `imagine-5558fc80.mp4`  
Original SHA-256: `162b3c5cf6c41cc1b85800a1e6111a94df3e3dd829935521aa8c90de15e51803`  
Original: 560x560, 24 fps, ~6.041667 s

GitHub visual recovery proxy:

`references/source-clips/imagine-5558fc80-github-reference.mp4`

Use this clip to extend the environment, painterly texture, light behavior, composition, and motion vocabulary of sample A.

## What must be derived from the clips

Before generating new final scenes, extract and document:

- protagonist face and hair geometry
- flower-crown / botanical vocabulary
- costume silhouette, cloth weight, folds, and material
- skin rendering and facial softness
- woodland greens and shadow colors
- warm/cool light relationships
- brush / pigment / canvas surface behavior
- depth falloff and background softness
- foreground floral/foliage framing
- camera distance and portrait/environment ratios
- actual motion amplitude and direction from the clips
- how hair, fabric, leaves, flowers, light and camera move relative to one another

## New storyboard rule

Every storyboard frame must pass this question:

> Could this plausibly be a frame from a longer film made by the same visual artist as the supplied sample videos?

If not, reject it before animation.

The story can move from woodland to village, road, tavern, merchant encounter, communal dance, silver-coin imagery and dawn, but the **woman and her painted world must remain visually continuous**. Do not fall back to generic dark-fantasy, generic tavern concept art, photorealistic portraits, anime, game-CGI, or unrelated painterly styles.

## GitHub recovery note

The dedicated GitHub MP4s are intentionally lightweight full-duration visual proxies so agents can see the source sequences directly from the branch. They are not bit-identical replacements for the larger canonical originals. Original hashes/metadata in `ASSET_MANIFEST.json` remain authoritative.

## Production order

1. Frame extraction from both originals.
2. Character/style contact sheet and visual DNA analysis.
3. New storyboard centered on the sample-A woman.
4. Storyboard visual QC.
5. Only then: motion/NeRF/effects/audio sync.
6. GitHub checkpoint after each phase.
