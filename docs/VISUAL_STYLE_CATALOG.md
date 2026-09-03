# Visual Style and Rendering Catalog

This is the repository-wide reference for visual languages, rendering technologies, animation methods, audio-reactive systems, and transition techniques available to AIVideoEdit.

## Governing principle

**Each song chooses its own visual language.** This catalog is a menu, not a mandatory house style. Select and combine techniques according to the song's emotional arc, lyrics, instrumentation, structure, and production limits.

Do not reduce a production to a slideshow. Favor living scenes, meaningful motion inside each image, and seamless MP4/WebM loops where reusable motion is appropriate.

---

## 1. Spatial and 3D rendering technologies

### 3D Gaussian Splatting (3DGS)

Represents a navigable scene using many colored, translucent, oriented 3D Gaussian splats rather than conventional polygon meshes. Useful for photoreal spatial environments with genuine camera travel—for example, entering a tavern, circling a forge, or moving through a ruined landscape.

This is a scene-rendering/reconstruction technology, not an art style by itself. It may be combined with cinematic realism, dark fantasy, painterly treatment, or other visual languages.

### Neural Radiance Fields (NeRFs)

Neural view synthesis that reconstructs the appearance of a scene across viewpoints. It serves a purpose similar to Gaussian splatting but is generally a different, more neural and potentially slower rendering path.

### 2.5D parallax scene graphs

Separate a composed image into depth-aware layers such as background, architecture, midground, subject, foreground, atmosphere, lights, particles, reflections, and grade. Move the virtual camera through those layers for dimensional motion without requiring a complete 3D reconstruction.

---

## 2. Living-image approaches

### Cinematic living paintings

Highly composed still imagery becomes a miniature scene: breathing, hair and cloth movement, fire, smoke, rain, reflections, practical-light changes, facial micro-motion, particles, depth, and controlled camera motion.

### Temporal paintings

The image itself evolves over time. Lighting, weather, season, texture, age, atmosphere, or emotional state may transform continuously within the composition.

### Cinemagraph / micro-loop animation

Focused, seamless motion within a largely stable composition. Motion should be more substantial than a slow zoom and may feel GIF-like, but production delivery should normally use efficient MP4/WebM loops.

### Painterly animation

Brushwork, pigment, ink, illustrated texture, or surface detail visibly moves, dissolves, reforms, or repaints itself with the music.

---

## 3. Narrative visual languages

### Cinematic realism

Film-like composition, lighting, lenses, staging, and camera behavior without requiring strict photorealism.

### Photoreal narrative

Believable recurring characters and environments presented like footage from an actual film.

### Dark-fantasy narrative

Mythic or haunted worlds, symbolic environments, dramatic light, and recurring protagonists.

### Naturalism

Restrained and physically believable environments, performances, lighting, textures, and motion.

### Stock-footage / documentary realism

Observational imagery that feels found, historical, intimate, journalistic, or documentary-like.

### Sequential generated cinema

Connected Sora/Veo-style narrative clips constructed shot by shot with continuity of character, location, costume, props, direction, and screen geography.

---

## 4. Illustrated and graphic languages

### Graphic-novel animation

Inked frames, hard shadows, deliberate limited motion, panel transitions, and dramatic compositions.

### Collage animation

Photographs, drawings, paper, typography, objects, textures, and ephemera assembled into moving compositions.

### Cut-paper / layered illustration

Visible layered shapes and handmade theatrical depth, animated as articulated planes.

---

## 5. Abstract and audio-reactive languages

### Abstract generative visuals

Geometry, fluids, fields, interference patterns, recursive forms, and evolving systems driven by musical structure.

### WMP-era reactive visualizer

The energy and immediacy of classic Windows Media Player visualizers, deliberately modernized and integrated into cinematic presentation.

### Spectrum / waveform / oscilloscope

Frequency or waveform information incorporated into scenery, symbols, horizons, machinery, light, architecture, or graphic passages rather than automatically appearing as an overlay.

### Particle / tunnel / plasma worlds

Music-driven particles, recursive tunnels, plasma fields, sparks, embers, fog, smoke, and energy structures.

### Integrated audio-reactive cinematography

Musical data drives cinematic properties:

- bass or low end -> fire intensity, depth, fog density, or environmental weight
- mids -> particles, texture, and environmental movement
- highs -> sparks, glints, and highlights
- transients -> light accents, micro-shake, cuts, or impact motion
- vocals -> focus, depth, facial emphasis, and atmosphere
- sustained reverb -> fog, smoke, diffusion, or spatial expansion

---

## 6. Editing and transition languages

### Recursive dream transitions

Travel through an eye, mirror, doorway, coin, flame, smoke cloud, painting, window, or other meaningful object into the next scene.

### Object-morph narrative

One meaningful object transforms into another across scenes, preserving symbolic or compositional continuity.

### Continuous dream journey

The full video feels like one uninterrupted passage through changing environments or states.

### Hybrid visual film

Combine narrative realism, living paintings, Gaussian environments, painterly or graphic passages, generated cinema, and visualizers as the song changes. The blend should follow the music rather than displaying every available technique.

---

## IronFlame example—not a universal default

The IronFlame storyboard combines:

- cinematic realism
- dark fantasy
- painterly imagery
- naturalism
- selective animation
- integrated visualizer elements

That combination belongs to IronFlame's visual DNA. Other songs, including Silver Coin, must be allowed to establish their own blend.

## Selection rule for a new song

During **Listen & Decode** and **Visual DNA**, choose:

1. the primary visual language;
2. any secondary visual language;
3. the spatial/rendering method;
4. motion density and loop strategy;
5. the role of audio reactivity;
6. the transition language;
7. the ending logic.

Record the selected blend in the song project's `VISUAL_DNA.md` before full asset production.
