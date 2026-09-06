# Style Contract

This repository's target look sits deliberately between two failure
modes. Use this table to self-check any shot before it's accepted.

| Trait | Static slideshow (FAIL) | Living-image animated still (TARGET) | Generic AI-generated video (FAIL) |
|---|---|---|---|
| Motion source | None — held frame | Parallax/depth layers, splat data, or particle/atmosphere systems acting on real source or locked-identity pixels | Model hallucinates new geometry/content per frame |
| Identity | N/A | Exact source likeness preserved, or a locked identity sheet reused consistently | Face/body regenerated shot-to-shot, drifting |
| Camera behavior | None or generic Ken Burns pan/zoom only | Depth-aware camera movement, internal scene motion (fire, smoke, water, embers) | Camera motion is a side effect of generation, not authored |
| Transitions | Hard cuts or basic crossfade | Authored pigment/object/recursive transitions from the effect registry | Transitions are whatever the generation model happened to produce |
| Traceability | N/A | Every visible effect traces to a registry ID, source input, and proof render | Effect can't be pointed to in code; "the model just did it" |

A shot passes only if every row lands in the TARGET column. A shot that
is technically clean (renders, plays, has no black frames) but reads as
slideshow or generic-AI-video has still failed — see
`general/reusable/LESSONS.md` for the IronFlame V3.4 case.

## Reference points

- **Internal benchmark:** `song/silver-coin` V8 final
  (`Silver_Coin_V8_FINAL_YouTube_720p24-1.mp4`). Copy its production
  discipline and visible motion quality, not necessarily its art style.
- **External reference:** the Mountainnoir YouTube channel demonstrates
  this target aesthetic. When starting a new production, review current
  uploads there for direction before locking a shot's motion treatment.
