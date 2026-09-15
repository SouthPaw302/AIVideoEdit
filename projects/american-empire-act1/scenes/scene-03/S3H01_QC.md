# Scene 03 Hero 01 — Continuity QC

Status: `FAIL / DO NOT PROMOTE`
Shot: `S3-01`
Hero: `S3H01`
Role: `departure_state`

## Locked requirement

`S3H01` must be the immediate continuation of Scene 02 terminal narrative state while remaining inside the established Paris apartment. Claire is still the same person, with the same dark wavy hair, facial structure, apparent age, body proportions and established apartment wardrobe. She retains the phone and secures/carries the already-approved essential. Camera is locked. The storm/city transition may remain visible through the established window geometry, but the shot must not advance into hallway, lobby, street or public-authority imagery.

## Attempts reviewed

1. `S3H01-ATTEMPT01` — rejected for insufficient Claire/apartment identity continuity.
2. `S3H01-ATTEMPT02` — rejected because the generation advanced into street/public-authority imagery and introduced unapproved spectacle/branding.
3. `S3H01-ATTEMPT03` — rejected for poster/title treatment, drones, armed spectacle, invented branding and street-scale authority imagery.
4. `S3H01-ATTEMPT04` — rejected after a reference-isolated retry still jumped forward to lobby/street authority imagery, propaganda text and militarized surveillance.

All four generated files are archived under `AE / Act I / Scene 03 / Rejected & Alternates` and recorded in `ASSET_MANIFEST.json`.

## Diagnosis

The repeated failure is not a storyboard problem. The current image-generation route is over-expanding the broader American Empire premise and collapsing later Scene 03 beats into the first hero image. Additional blind retries would violate the project's diagnose-before-regenerate rule and the user's instruction not to generate random image volume.

The continuity reference also needs to be isolated from the multi-panel Scene 01 contact sheet before the next retry. A single Claire identity frame plus a single apartment topology frame should be used instead of the full contact sheet whenever the generation backend supports explicit reference roles.

## Hard negatives for the next retry

The next `S3H01` attempt must contain none of the following:

- no hallway, lobby, Metro entrance or street-level composition;
- no police/security/military foreground presence;
- no drones;
- no propaganda, title cards, slogans, logos or `AMERICAN EMPIRE` text;
- no floating UI or holograms;
- no new architecture or redesigned apartment;
- no outer coat unless it is introduced later at the apartment threshold;
- no camera push, orbit or dramatic poster framing;
- no new props beyond the already-approved essential and retained phone.

## Required next method

Do not generate another broad text-to-image interpretation. Use a tightly constrained continuity method:

1. isolate the strongest accepted Scene 01 Claire identity frame;
2. isolate the established apartment topology frame;
3. use those references with explicit roles or a source-derived edit/composite route;
4. make only the physical state change required by `S3-01`: essential unsecured -> secured/carried, phone retained;
5. run identity/topology/narrative QC before any animation or before starting `S3H02`.

No `S3H01` image is accepted yet.
