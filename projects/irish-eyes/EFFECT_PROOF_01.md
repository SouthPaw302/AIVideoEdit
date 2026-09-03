# Irish Eyes — Effect Proof 01

Status: **provisional PASS** for restoration + restrained memory FX; loop seam still requires motion QC in sequence.

## Source

- `Brandi South Florida 2017.mp4`
- portrait-oriented display after source rotation metadata is respected
- extracted source library: 953 frames @ 30 fps

## Proof A — Cinematic restoration

Source section: approximately 00:02.00–00:08.00 of the real video.

Implemented, not merely planned:

- local luminance recovery using LAB + restrained CLAHE;
- gentle subject-shadow lift;
- restrained warm balance;
- slight saturation recovery;
- bilateral cleanup;
- subtle unsharp detail recovery.

QC:

- identity: PASS — effect is pixel-processing only; no generated face/body;
- sky retention: PASS in representative sample;
- color: PASS, restrained;
- artificial skin/face detail: none introduced;
- effect visibility: intentionally subtle but present.

Workspace proof SHA-256:
`56f10a36d754c9785abde5f05002193cdcfb3eac1bfa261ec83398bd5a7770eb`

## Proof B — Source-derived loop

Seed window: approximately 00:02.83–00:05.33.

Method:

- endpoint candidate selected from frame-difference + motion-difference search;
- 75-frame real source seed;
- repeated from real motion;
- short cross-blended seams built from source frames only;
- proof duration approximately 6.83 s.

Status: **requires final seam-motion review before timeline approval**. Mathematical endpoint similarity alone is not acceptance.

## Proof C — South Florida Memory FX

Applied to the source-derived loop and driven by measured RMS from `Irish eyes (Remastered).wav` starting near 00:08.

Implemented effects:

- the same cinematic restoration baseline;
- high-luminance selective warm halation/bloom;
- restrained water-region displacement/shimmer;
- song-RMS-driven modulation of shimmer and halation strength;
- smoothing/bounding to avoid strobe behavior.

QC representative frame:

- Brandi identity preserved: PASS;
- water motion remains subtle: PASS in sampled frame;
- bloom remains motivated by existing highlights: PASS;
- no face morphing/generation: PASS;
- effect is actually present in rendered output: PASS.

Workspace proof SHA-256:
`4658a7339017a31710ef2849bcd64e5557ed6d7a4014ff7ebdcf66e8e4500639`

## Promotion decision

The underlying restoration / halation / water-shimmer / audio-envelope method is reusable beyond Irish Eyes. Promote the code to `main/general/reusable/irish-eyes-tools/` with documentation, while keeping song-specific timing/configuration on `song/irish-eyes`.

## Next gate

1. finish seam-motion QC on at least three source loops;
2. build first 2.5D depth proof;
3. build reflection/dream transition proof;
4. test whether any source segment has enough parallax for a clean 3DGS waterfront reconstruction;
5. only then begin assembling Act I of the final movie.