# Visible Memory FX Preset

Reusable photoreal effect preset proven during the Irish Eyes V4 rebuild.

This is a stronger presentation preset built from existing repository effects. It does not replace the underlying implementations in `south_florida_memory_fx.py`, `depth-parallax-25d`, or the Silver Coin reusable video-FX stack.

## Purpose

Use when a cinematic-memory sequence needs effects to be plainly visible to a normal viewer without turning the shot into a generic visualizer or breaking photographic identity.

## Core combination

1. **Depth travel**
   - continuous depth-field parallax;
   - stronger camera amplitude than the conservative proof preset;
   - modest zoom breathing;
   - avoid hard-cardboard subject separation.

2. **Temporal echo**
   - 3–5-frame weighted motion history;
   - low opacity;
   - strongest around moving hair, fabric, water, clouds, or silhouettes;
   - do not allow facial duplication to dominate.

3. **Prism edge separation**
   - small opposing red/blue horizontal shifts;
   - blend primarily around high-contrast edges;
   - keep center detail readable.

4. **Halation / bloom**
   - blur bright-pass layer;
   - warm-biased bloom for sun/reflection scenes;
   - cool-biased bloom for storm scenes;
   - visible but not clipped.

5. **Water / reflection displacement**
   - sinusoidal lower-frame remap;
   - small multi-frequency horizontal displacement;
   - independent vertical ripple;
   - use stronger amplitude only in dedicated dream passages.

6. **Volumetric light / haze**
   - broad soft light shafts from existing motivated highlights or storm openings;
   - low-opacity moving haze;
   - no arbitrary fantasy beams with no scene source.

7. **Lightning / wet-reflection accents**
   - short deterministic flash windows;
   - sky flash and lower-frame reflection should happen together;
   - reserve for storm/transition moments.

## Proven V4 balance

The V4 review master used this stronger preset in dedicated passages rather than over the entire movie. Successful result:

- visibly different from untreated source;
- no black frames;
- no long frozen 2.5D passage after amplitude revision;
- no identity replacement;
- remained compatible with 720x1280 / 30 fps H.264 delivery.

## QC rule

Do not accept the effect because the filter/code ran. Scan the exported result and verify:

- effects survived final compositing;
- temporal echo does not create distracting duplicate faces;
- depth motion is visible at normal playback speed;
- prism does not produce constant color fringing everywhere;
- water distortion stays spatially motivated;
- bloom does not destroy highlight detail;
- no source obstruction or foreground object reads as an effect glitch.

## Irish Eyes lesson

The first conservative preset was technically correct but perceptually too subtle. The reusable rule is now: **for a dedicated effect passage, visible intent matters as much as technical implementation.**