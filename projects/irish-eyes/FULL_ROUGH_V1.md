# Irish Eyes — Full Rough Movie V1

Status: **complete first-pass movie cut rendered and representative-frame QC completed.**

This is no longer a storyboard/planning-only state. A complete moving-footage cut now exists for essentially the full song.

## Full render

Workspace render:

- `IRISH_EYES_FULL_ROUGH_v1.mp4`
- H.264 video
- 720 x 1280 portrait
- 30 fps
- AAC stereo 48 kHz
- duration: 187.060026 s
- file size: 91,410,608 bytes
- SHA-256: `f4a7ca04c47c7910b4cfacc98b600520a641f028eaf3d5941852dee92ee3f6f2`

The video is muxed against the original `Irish eyes (Remastered).wav` as the soundtrack source.

## Act renders

### Act I

- `IRISH_EYES_ACT1_v1_57.59s.mp4`
- duration: 57.59 s
- source-led opening / real memory / approved 2.5D and source-derived movement

### Act II

- `IRISH_EYES_ACT2_v2_43.63s.mp4`
- duration: 43.63 s
- SHA-256: `f67e16c826f1bae9d6f6a80c5e6579654a2ed57354363dffa5d8411afe2559ce`
- reflection-memory expansion, environment-only support plate, return to real source

### Act III

- `IRISH_EYES_ACT3_v1_54.84s.mp4`
- duration: 54.84 s
- SHA-256: `ab264627056a422e2925f5db3c4a3f5a6224f9875f2bc44eacb73b2fd2d89f71`
- real dress/hand detail, rain-on-glass optical treatment, real refraction close passage, blue-hour environment plate, 2.5D, real slow-glance passage

### Act IV

- `IRISH_EYES_ACT4_v1_31.06s.mp4`
- actual encoded duration: ~31.00 s
- SHA-256: `ecc5e03210b6535567c88c63eddd8f00f0f3c92c5b438412b67fbdeea3643e74`
- effects progressively reduce; cut resolves back toward real source imagery

## New moving assets created for Act III

- `act3/real_dress_hands_detail_h264.mp4` — source-derived body/dress/watch/hands detail, no generated identity
- `act3/real_rain_glass_memory_h264.mp4` — real footage behind synthesized optical rain/glass foreground
- `act3/real_refraction_close_h264.mp4` — real footage close passage with moving glass/refraction distortion
- `act3/memory_blue_hour_water_h264.mp4` — environment-only support crop with camera drift and water movement; generated human excluded
- `act3/real_slow_glance_h264.mp4` — source-derived retimed real sequence

## Full rough QC

Representative frames sampled across the complete timeline show:

- portrait orientation maintained across accepted shots;
- no storyboard stills used as movie content;
- no generated replacement of Brandi in identity-critical passages;
- 2.5D shots visibly contain differential depth motion;
- environment-only generated plate is used without its generated human figure;
- rain/refraction effects are visibly present rather than plan-only;
- film repeatedly returns to the real 2017 source;
- final section resolves back toward source reality.

## Known V1 weakness / next-pass target

The full rough intentionally proves the pipeline and completes the song, but the limited 31.77-second real source causes some later passages to revisit similar compositions. The next production pass is therefore a **replacement and refinement pass**, not another storyboard pass.

Priority replacements:

1. add genuinely different real-world B-roll in Act II/III when available;
2. replace repetitive full-body waterfront returns with roads, interiors, windows, travel, weather, family/place detail, or additional real South Florida footage;
3. create additional environment-only or source-derived cinematic shots only where real B-roll is unavailable;
4. refine line-level lyric sync once exact lyrics are recovered/provided;
5. perform transition seam, temporal, and music-edit QC across act boundaries;
6. final grade/unification pass and high-quality final encode.

## Useful optional user B-roll

Production can continue without these, but any of the following real footage would materially improve the replacement pass:

- driving / road footage, especially dusk, rain, rural, mountain, or night;
- lake, ocean, river, shoreline, sunset, clouds, storms, rain, trees;
- house exterior/interior, porch, windows, warm lamp/candle light;
- travel details: dashboard, passenger-window view, roadside, signs without sensitive/private data;
- additional footage of Brandi from roughly the same era, especially candid walking, looking away, sitting, driving/passenger, indoors, water, or sunset;
- family/place footage that relates directly to the lyrics or the song's memories.

Do not stop production solely waiting for B-roll. Use it to replace weaker/repetitive passages when supplied.

## Storage note

The local full rough is below GitHub's ordinary 100 MB single-file ceiling but the current connector does not provide a practical binary-stream upload path for a ~91 MB movie. The exact filename, dimensions, duration, byte size, and SHA-256 are recorded here so the render can be matched/recovered exactly. Text/code/effect assets continue to be checkpointed normally on the branch.