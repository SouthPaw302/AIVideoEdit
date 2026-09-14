# Scene 01 FX Plan — Recovery Pass

This plan replaces the rejected full-scene FX attempt. It uses existing repo capabilities only. No new effect implementation and no new image generation are authorized.

## Governing rule
The storyboard drives the edit. Internal scene motion first, camera motion second. The score plays continuously underneath the scene and does not determine shot cuts.

Every effect is assigned to semantic regions in a shot package; no effect may default to the full frame merely because a global ROI is convenient.

## Layered 2.5D method — current user lock
For Scene 01, do not use an obvious whole-frame pseudo-depth warp as the primary 2.5D treatment.

Use the existing `depth-parallax-25d` lineage for subject isolation / alpha handling, but build the production shot like a practical multiplane composite:
1. preserve the approved hero image unchanged as the base plate;
2. duplicate the hero for the midground subject where needed;
3. cut out the closest real foreground objects (phone/table, curtain/picture edge, bed/books/chair, near architecture, etc.) into transparent RGBA layers;
4. animate those real layers independently with very small relative transforms;
5. composite them back over the untouched hero with alpha;
6. keep Claire's face, hands, phone and ink contours protected;
7. avoid destructive background inpainting unless a specific shot proves it is visually clean.

Parallax should read like real camera depth, not an effect. Foreground travel is measurable but small; midground moves less; background is near-locked. No global wobble.

## Existing repo methods to reuse
Use the proven principles from `song/silver-coin` and `song/leave-it-by-the-door` without reusing their media or story content:
- semantic cutout / local-mask compositing;
- localized living motion rather than global wobble;
- advected atmosphere;
- motivated weather particles;
- wet/reflection displacement only on plausible reflective surfaces;
- practical-light breathing and moving light fields tied to real sources;
- near-locked camera when internal motion carries the scene.

## Candidate canonical FX
These remain candidates until the representative proof and current precompile gate pass:
- `FX2-SPATIAL-001` — use its isolation/alpha lineage where useful; do not default to the full-frame warp treatment;
- `FX2-MOTION-002` — localized living flow for curtain/hair/foreground material only;
- `FX2-MOTION-003` — water/wet reflection movement where physically present;
- `FX2-ATM-001` — depth/region-limited haze or mist;
- `FX2-ATM-002` — exterior rain plane only;
- `FX2-ATM-003` — rain-on-glass only, window ROI only;
- `FX2-LIGHT-001` — practical-light breathing around actual lamp/phone sources;
- `FX2-LIGHT-002` — source-motivated moving light / lightning illumination;
- `FX2-SURFACE-003` — reflection shimmer only on glass/reflective regions.

## Shot families
### Exterior — S01/S02
Use near architecture as a transparent foreground plane, middle rooftops/facades as a lighter mid plane, and the skyline as an almost locked base. Exterior rain and wet-surface response remain region-limited. Do not exaggerate depth travel.

### Bedroom / phone — S03/S04
Untouched hero is the base. Phone/table is the closest foreground layer; Claire/bed is a protected midground layer; window/city remains background. Rain is forbidden on interior pixels and allowed only on/outside the window. Practical light stays localized to phone/lamp sources.

### Claire / warning — S05-S08
Claire is protected midground. Curtain/picture/near obstruction can be a separate foreground cutout. Window/city remains background. Localized hair/curtain motion is allowed outside protected masks. Camera stays near-locked.

### Lightning reveal — S09/S10
Bed/books/chair or other near room objects can form the foreground layer; Claire remains protected midground; window/city is background. Lightning is a coherent source-motivated illumination event, not shake or a global white flash.

### Isolation — S11/S12
Use near furniture/window edges as foreground only if they improve depth. Claire/reflection identity stays protected. Glass reflection, rain, haze and practical light remain independent subtle layers, then controlled fade.

## Score / editorial policy
The score is underscore, not an edit map. It plays continuously through storyboard-driven cuts. Musical events may support an existing storyboard event (for example lightning) but must not create new cuts or reorder the scene.

## Caption policy
Captions follow story/dialogue timing and storyboard readability, not beats. Keep captions away from faces, hands, the phone, lightning, and important foreground movement.

## Representative proof gate
Do not render the entire 80-second scene first. Build a short proof containing:
1. an exterior segment from H01 proving subtle real-layer depth;
2. an interior segment from H02/H03 proving phone/table foreground, Claire/bed midground, dry room and window-only weather;
3. a profile/window segment from H04/H06 proving a real foreground cutout plus stable Claire;
4. a brief H05 light-event segment proving coherent illumination without shake.

The proof fails if any of these are true:
- rain appears on interior walls, bedding, Claire or furniture;
- foreground motion looks like a software warp rather than physical depth;
- foreground travel is excessive;
- movement consists mostly of camera drift;
- lighting pulses globally without a plausible source relationship;
- Claire's face/hands/ink lines deform;
- the score dictates cuts instead of the storyboard;
- effect IDs are claimed but not visibly present.

Only after current-user acceptance and mode-aware QC may `FX_LOCKED` be claimed and the full Scene 01 render begin.
