# IronFlame V2 — Reference Style Lock

**Branch:** `song/ironflame-20260905-0216`  
**Runtime source:** `main@e6ba077cabeed8e799090d3d505d82bc96d2fd02`  
**Status:** locked before hero-image expansion

## Authority order

1. The three user-supplied reference videos define the visual/effect grammar.
2. Lyrics and the canonical IronFlame song structure determine story function and timing.
3. The repository provides implementations and timing/reactivity systems only where they fit that grammar.
4. An available effect is not permission to use it. If it does not resemble the reference-motion language, it is excluded.

## Reference grammar

### REF-A — cosmic face / reaching silhouette
Source: `imagine-22d97f7e.mp4`

Keep:
- black human silhouette;
- enormous blue flowing face;
- contour/nebula line structure;
- small warm-white energy orb traveling between human and face;
- very restrained field drift;
- clean blue-to-dusk background;
- intimate symbolic contact.

### REF-B — glowing face / palm silhouette
Source: `imagine-3324e842.mp4`

Keep:
- profile silhouette;
- pale-blue clean field;
- warm cream/orange translucent head;
- palm-held glow;
- slow hover and breathing luminance;
- faint circuit-line geometry only where already native to the style.

### REF-C — crystalline head / spectral ring
Source: `imagine-ae835deb.mp4`

Keep:
- dark faceted blue head;
- flowing cyan/blue spectral ribbons;
- luminous circular ring/halo;
- smooth ring expansion/contraction;
- fine particles embedded in the ribbon/ring;
- clean abstract blue background.

## Explicit exclusions

Do not introduce unrelated cinematic-fantasy scenery, realistic houses, armor, forests, wolves, battlefield imagery, rain effects, forge fire, generic particle storms, lens-flare spectacle, or decorative visualizer overlays merely because those techniques exist in the repository.

The previous generated rainy-house/cosmic-spirit interpretation is rejected for this V2 direction.

## Approved effect families for proof

Only effects that can reproduce or support the reference grammar are candidates:

- `FX2-AUDIO-001 reactive_control_bus` — timing source.
- `FX2-MOTION-002 localized_living_flow` — only for face/ribbon internal motion.
- `FX2-MOTION-004 quiet_depth_breath` — proof-required; only if motion stays nearly imperceptible.
- `FX2-LIGHT-001 practical_light_breath` — reinterpret only as orb/head breathing luminance.
- `FX2-LIGHT-002 moving_light_field` — restricted to internal glow migration.
- `FX2-LIGHT-003 localized_glint` — restricted to tiny crystalline/specular points.
- `FX2-TRANS-003 light_peak_handoff` — candidate for orb/light-to-next-shot transitions.
- `FX2-VIS-001 organic_reactive_field` — proof-only as a source for flowing field/ribbon texture, never as a generic overlay.
- `FX2-SPATIAL-004 streaming_living_parallax` — proof-only for subtle layered breathing when a hero image supports it.

Everything else is excluded unless a proof demonstrates that it matches one of REF-A/B/C.

## Hero-image rule

Each lyric section gets a hero image selected or generated from the three reference families. Supporting media expands that hero image's world while preserving its silhouette geometry, palette, line/ribbon language, and motion family. New media must look as if it could be another frame from the supplied reference set.

## Production test

A shot passes visual-direction QC only if a side-by-side contact sheet with the source reference makes the relationship obvious without explanatory text.