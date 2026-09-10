# AIVideoEdit Production Modes

Production mode describes **what kind of finished visual experience is being made**. Direction authority describes **where the directing language comes from**. They are separate decisions.

## Direction authority
- `reference_led` — supplied visual reference teaches the visual/motion language. It does not automatically authorize content reuse.
- `music_led` — song structure, lyrics when applicable, genre, energy, rhythm, and musical events lead the direction.
- `user_directed` — the current user explicitly defines the visual route or overrides the inferred route.

A production may be both reference-informed and user-modified; record the highest current authority in the project Operating Order and preserve the supplied reference roles in `REFERENCE_MANIFEST.json`.

## Production modes

### `living_scene`
A strong stable image or illustration behaves like a living world. The composition remains recognizable while selected regions move independently: fire, smoke, rain, water, reflections, atmosphere, light, particles, hair, cloth, environmental motion, or intentional articulated subject motion. Camera motion is restrained and secondary.

Primary proof questions:
- Does the image remain authored and stable?
- Is internal motion visible and materially appropriate?
- Are different materials moving independently?
- Are faces/hands/anatomy stable?
- Are loops and joins unobtrusive?
- Is the camera helping rather than replacing animation?

### `cinematic`
A conventional evolving film with deliberate shot changes, action, locations, staging, coverage, continuity, character behavior, and cinematic progression.

Primary proof questions:
- Is the story/action readable?
- Is coverage sufficient and non-repetitive?
- Are character/world continuity and screen direction controlled?
- Do shots evolve with the music rather than merely decorate it?
- Are transitions and pacing intentional?

### `hybrid`
A deliberate combination of cinematic progression and living-scene construction. Sections or shots declare which behavior they use. This is not permission to mix methods randomly; each section must have a reason and mode-appropriate proof criteria.

Primary proof questions:
- Does each section clearly serve either living-scene or cinematic behavior?
- Do the two methods share one visual world and continuity language?
- Are transitions between methods intentional?
- Does complexity improve the film?

## Selection rule
Before production media generation, record both direction authority and production mode in the active project's `OPERATING_ORDER.json`.

When there is no usable visual reference, the existing no-reference visual-direction gate still applies: present materially distinct routes to the user, let the user select or combine them, then record the resulting direction authority and production mode.

When there is a supplied visual reference, analyze it before selecting production mode. Do not assume that a moving reference implies cinematic production; it may demonstrate a living-scene or hybrid motion language.
