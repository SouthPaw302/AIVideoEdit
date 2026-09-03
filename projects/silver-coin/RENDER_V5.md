# Silver Coin — V5 / V5.1 Full-Song Render Notes

## V5 milestone

V5 is the first complete 207.440-second render driven by the actual remastered WAV rather than preview-cycle timing.

### Core pipeline

1. Real-master audio analysis (`AUDIO_ANALYSIS.md`).
2. Beat-snapped 29-scene timeline (`TIMELINE_V5.json`).
3. 29 recovered/cleaned painted narrative sources.
4. Compact trained CPU NeRF volumes for village, threshold, tavern, coin, and dawn families.
5. Pseudo-depth camera motion and painterly micro-motion.
6. Audio-reactive modulation from normalized energy/transient/brightness/low/mid/high controls.
7. Motion amplitude clamped to the measured range of the two user-supplied style-reference clips.
8. Pigment/chroma transitions plus the brief silver-coin portal.
9. Canonical WAV muxed into the rendered MP4.

## V5 audio mapping

- energy → camera/parallax
- mid → cloth/crowd/hair/localized painted motion
- low → smoke, fire breath, heat haze, room warmth
- high + transient → rain/embers/metal glints
- transient → fiddler bow impulse and edit punctuation
- brightness → candle/window/light shafts

The controls are built locally with `tools/audio/build_reactivity.py`.

## V5 QC findings

A complete 640×360 / 12 fps full-song QC draft was rendered successfully with exact 207.440-second duration and the canonical stereo audio.

QC sampling found:

- the coin portal remains readable and brief; it transitions naturally into the barmaid rejection scene
- chorus/fiddler scenes preserve character/instrument readability under audio-reactive motion
- the opening source retained a tiny section-number remnant at the upper-left edge
- the original bridge cleanup enlarged several narrow storyboard subpanels too aggressively, producing fragmentary torso/hand/object compositions

The last two items triggered V5.1 rather than being accepted as final.

## V5.1 source repair

V5.1 uses no generative repair for the identified issues.

- opening numeral: removed through additional left-edge deterministic reframe
- bridge: rebuilt with the **narrative-ribbon reframing** method documented in `docs/MOTION_CALIBRATION_AND_NARRATIVE_RIBBON.md`
- bridge geometry/provenance: `BRIDGE_RIBBON_V51.json`
- repeated poor-in-coin chorus image: replaced by an alternate readable crowd reframe rather than an over-cropped text-removal fragment

## Integrity / terminology

Allowed technical description: **audio-reactive hybrid neural-radiance-field spatial rendering**.

The NeRF is an actual trained compact MLP carrying learned volumetric density/color/view response. Detailed people, instruments, clothing, props, and architecture remain painted image layers. Do not claim photogrammetric reconstruction, Instant-NGP, Nerfstudio, or a physically complete 3D scene.

## Next QC

After the V5.1 full render completes:

1. verify exact duration/audio streams
2. sample every macro section plus all section boundaries
3. inspect bridge composition continuity
4. inspect opening for residual text
5. inspect coin portal and both fiddle sequences
6. inspect final-chorus transient density
7. create reduced GitHub recovery preview and update manifest/status
