# AIVideoEdit Architecture

AIVideoEdit is designed as a persistent, tool-orchestrated music-video production system.

## Core layers

### 1. Direction layer
Determines what the song wants to become visually.

Inputs:
- source audio
- lyrics
- genre/instrumentation
- emotional arc
- user intent

Outputs:
- visual DNA
- shot plan
- motion language
- visualizer role
- ending logic

### 2. Asset layer
Creates and catalogs:
- production stills
- character references
- environments
- textures
- masks
- depth layers
- particles
- procedural FX
- micro-loops
- visualizer assets

### 3. QC layer
Performs still-image and temporal checks before expensive assembly.

### 4. Animation layer
Turns stills/assets into living scenes using:
- parallax
- camera transforms
- selective local deformation
- particles
- light and shadow changes
- environmental loops
- audio reactivity

### 5. Edit layer
Builds the song timeline from actual musical/lyrical structure rather than evenly distributing scenes.

### 6. Render layer
Pre-renders expensive scenes, assembles efficiently, preserves source audio quality, and exports master + compact delivery files.

### 7. Archive/publish layer
Stores manifests and reproducible instructions in GitHub; stores large media in project/object storage where available.

## Scene graph concept

A single scene may contain independent layers:

```text
SCENE
  camera
  background
  architecture
  midground
  subject
  foreground
  practical_lights
  fire
  rain
  fog
  smoke
  steam
  dust_embers
  reflections
  shadow_fx
  visualizer_fx
  grade
```

Not every scene requires every layer.

## Audio-reactive data

Useful derived envelopes may include:
- RMS/overall loudness
- low/bass energy
- low-mid energy
- mid/vocal-band energy
- high-frequency energy
- onset/transient events
- beat estimates
- section boundaries

These envelopes should drive cinematic properties rather than defaulting to literal spectrum bars.

## Rendering strategy

Avoid recalculating an entire four-minute compositing graph frame-by-frame when motion is loopable.

Preferred strategy:
1. Render complex scene loops/segments once.
2. Validate them.
3. Reuse or extend where visually appropriate.
4. Assemble timeline.
5. Mux original/master audio late in the pipeline.
6. Validate exact duration and seekability.

## Future modularization

Potential reusable engine areas:

```text
engine/
  analysis/
  direction/
  qc/
  depth/
  animation/
  particles/
  visualizers/
  transitions/
  timeline/
  render/
  publish/
```

The repo may evolve toward MCP/plugin interfaces, command-line tools, or agent-callable modules, but the creative workflow remains tool-agnostic.