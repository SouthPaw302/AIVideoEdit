# Scene 01 FX Plan — Recovery Pass

This plan replaces the rejected full-scene FX attempt. It uses existing repo capabilities only. No new effect implementation and no new image generation are authorized.

## Governing rule
Internal scene motion first, camera motion second. Every effect is assigned to semantic regions in a shot package; no effect may default to the full frame merely because a global ROI is convenient.

## Existing repo methods to reuse
The current user explicitly authorized consulting successful prior branches for methods. Use the proven principles from `song/silver-coin` and `song/leave-it-by-the-door` without reusing their media or story content:
- pseudo/depth-assisted relative foreground/background displacement;
- localized living motion rather than global wobble;
- advected atmosphere;
- motivated weather particles;
- wet/reflection displacement only on plausible reflective surfaces;
- practical-light breathing and moving light fields tied to real sources;
- near-locked camera when internal motion carries the scene.

## Candidate canonical FX
These remain candidates until the representative proof and current precompile gate pass:
- `FX2-SPATIAL-001` — hybrid 2.5D / depth parallax adapter;
- `FX2-MOTION-002` — localized living flow for curtain/hair/foreground material only;
- `FX2-MOTION-003` — water/wet reflection movement where physically present;
- `FX2-ATM-001` — depth/region-limited haze or mist;
- `FX2-ATM-002` — exterior rain plane only;
- `FX2-ATM-003` — rain-on-glass only, window ROI only;
- `FX2-LIGHT-001` — practical-light breathing around actual lamp/phone sources;
- `FX2-LIGHT-002` — moving light field for slow motivated warm/cool migration and the existing light-envelope treatment for the lightning beat;
- `FX2-SURFACE-003` — reflection shimmer only on glass/reflective regions.

## Shot families
### Exterior — S01/S02
Required: visible multi-plane parallax, exterior rain, distant haze, localized wet-surface response. Foreground architecture must move measurably more than distant skyline while remaining restrained.

### Bedroom / phone — S03/S04
Required: phone foreground / Claire midground / window background separation. Rain is forbidden on interior pixels and permitted only on/outside the window. Practical light must be localized to its source and nearby surfaces. Foreground furnishing/curtain may move subtly.

### Claire / warning — S05-S08
Required: protected face/hands/phone; localized hair or curtain motion outside protected masks; window-only rain/reflection; deeper city/haze plane movement; local warm/cool light response. Camera near-locked.

### Lightning reveal — S09/S10
Required: stable Claire silhouette, readable depth layers before/after event, and coherent source-motivated illumination of room/glass. Rain stays outside. No shake effect is permitted as a lightning substitute.

### Isolation — S11/S12
Required: glass reflection moves as a reflective layer rather than deforming Claire, window rain only, very slow depth haze, minute practical-light breathing, then controlled fade.

## Representative proof gate
Do not render the entire 80-second scene first. Build a short proof containing:
1. an exterior segment from H01 proving 2.5D + exterior rain;
2. an interior segment from H02/H03 proving phone/Claire/window depth, dry room, window-only rain and practical-light coupling;
3. a profile/window segment from H04/H06 proving foreground motion plus reflection/glass separation;
4. a brief H05 light-event segment proving coherent illumination without shake.

The proof fails if any of these are true:
- rain appears on interior walls, bedding, Claire or furniture;
- foreground and background travel together so parallax is not visually readable;
- movement consists mostly of camera drift;
- lighting pulses globally without a plausible source relationship;
- Claire's face/hands/ink lines deform;
- effect IDs are claimed but not visibly present.

Only after current-user acceptance and mode-aware QC may `FX_LOCKED` be claimed and the full Scene 01 render begin.
