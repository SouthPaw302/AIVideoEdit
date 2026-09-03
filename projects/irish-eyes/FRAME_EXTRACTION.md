# Irish Eyes — Frame Extraction / Source Mining

Branch: `song/irish-eyes`

## Source

`Brandi South Florida 2017.mp4`

## Native extraction

- source duration: approximately 31.766344 seconds
- frame cadence: 30 fps
- extracted frames: 953
- extraction mode: full native-cadence PNG sequence for frame-level analysis and effect development

This extraction is the preferred source pool for photographic enhancement, loop construction, masking, depth separation, 2.5D scene construction, optical-flow tests, motion interpolation, reflection/environment analysis, and effect proofs.

## Source-first rule

Before generating a replacement visual, search this frame sequence and neighboring temporal windows for usable real material. Individual frames and short frame ranges can become:

- restored/enhanced photographic plates;
- seamless or ping-pong micro-loops when they pass QC;
- slow-motion/retimed sequences;
- foreground subject plates;
- depth/parallax layers;
- environment plates;
- reflection/water texture sources;
- cloud/sky motion references;
- Gaussian-splat/3D reconstruction input where genuine parallax exists;
- transition source imagery.

## Initial automated loop-candidate scan

A first-pass endpoint-similarity scan was run on downsampled grayscale frames. This is only a candidate generator; it is not visual approval.

Early low-seam windows include approximately:

- 2.00s → 3.50s
- 2.50s → 4.00s
- 2.50s → 5.00s
- 2.67s → 4.17s
- 2.67s → 5.17s
- 8.00s → 10.00s
- 8.50s → 10.00s

Each candidate must still be inspected for:

- body/face pose discontinuity;
- camera movement mismatch;
- wind/hair direction;
- water/reflection phase;
- exposure/white-balance jump;
- horizon alignment;
- visible seam;
- whether a crossfade, optical-flow bridge, reverse/ping-pong strategy, or custom transition is appropriate.

Do not use a candidate merely because its numerical seam score is low.

## Enhancement policy

Enhancement should be temporal-aware whenever possible. Neighboring real frames may be used to recover detail and stabilize noise, but the process must not hallucinate facial identity or alter anatomy.

A frame or loop fails if enhancement creates:

- eye/teeth/hair hallucination;
- waxy skin;
- oversharpened halos;
- frame-to-frame facial drift;
- unstable texture;
- temporal flicker;
- inconsistent grain.

## Status

Full source extraction complete. Loop discovery and effect-proof generation are next gates.
