# Silver Coin V6 — Music-Directed Camera & Effects Grammar

## Core rule

The painting stays sovereign. Music directs **camera energy, light, atmosphere, and transition timing**; it does not justify deforming the protagonist, hands, fiddle, architecture, or coin.

## Signal inputs

Use the canonical WAV to derive:

- transient/onset confidence
- short-window energy
- section boundaries
- optional brightness/high-frequency envelope

For V6 opening proof the camera/effects react to the actual waveform, not a guessed BPM clock.

## Camera vocabulary

### Slow push / pull
Base motion over 8–15 seconds. Transients may add a tiny optical emphasis (typically <= 0.4–0.6% scale), never a jump zoom.

### Lateral reveal
Move the crop through an oversized painting to reveal path, village, crowd, window, or instrument. This creates a new angle from static art without inventing geometry.

### Sub-degree angle drift
Use <= about 0.8 degrees over a scene. Best for threshold, travel, or chorus lift. Avoid constant rocking.

### Music-qualified angle settle
Let a strong transient finish a roll or crop travel rather than starting a random camera shake.

## Image-space Gaussian effects

### 2D Gaussian light-splat atmosphere
A low-resolution field of drifting Gaussian kernels is tinted and composited as light/haze. It adds depth and breathing light while preserving image texture.

This is **not** 3D Gaussian Splatting and must never be described as such.

### Gaussian-defocus light bridge
Around a strong cut/section boundary, briefly defocus outgoing/incoming images, crossfade, and add a small warm luminance veil. V6 uses a short ~0.84 s total window so faces are not soft for too long.

## Music-reactive effect limits

- transient micro-zoom: tiny optical emphasis only
- energy exposure lift: <= about 1–2%
- bloom: high-luminance regions only
- wet shimmer: lower-frame road/reflection region only
- fire/window glow: motivated sources only
- particles: only when physically justified

## V6 opening mapping

- 0:00–0:10 `forest_coin`: slow push and lateral reveal; soft gold-green splats
- 0:10–0:20 `path_reveal`: lateral travel toward village; counter-roll
- 0:20–0:30 `labor_end`: restrained pullback with transient-qualified micro push
- 0:30–0:39.3 `threshold_gold`: approach inn; practical glow + wet-road shimmer

Transitions near 0:10, 0:20, 0:30 use the Gaussian light bridge and are aligned to the music/scene structure.

## Reuse

Presets should be reusable across songs by changing scene-specific color, effect masks, and cue sensitivity. Keep the camera grammar generic in `tools/video_fx/`; keep song-specific cue maps under each project.
