# Irish Eyes — Magic Gate 03: Storm Revelation

Branch: `song/irish-eyes`

## Purpose

Test whether the real South Florida source can cross from enhanced footage into authored magical cinema without replacing the real scene or Brandi's identity.

## Real source window

- source: `Brandi South Florida 2017.mp4`
- frames: 614–743
- native cadence: 30 fps
- proof duration: 4.333333 s
- proof resolution: 360x640 portrait

The source itself contains the required ingredients: backlit Brandi, large cloud mass, bright sun/cloud opening, shoreline horizon and reflective water.

## P03 V1

Implemented:

- source-motion base rather than a frozen still;
- cool storm pressure in upper sky;
- source-cloud image-space advection;
- independent water displacement;
- Gaussian-shaped motivated light fields from the real sun/cloud opening;
- layered procedural rain;
- deterministic lightning;
- synchronized lower-frame water reflection flash;
- halation/prism treatment;
- asymmetric camera push / perception movement.

QC:

- frames: 130
- black frames: 0
- mean frame delta: 3.764871799185329
- p05 delta: 2.459072337962963
- p95 delta: 7.710067129629626
- SHA-256: `37057a16c76af3cdaf4d15d598619d7a7243d4915034d904b6f52574511e10b5`

Decision: **REVISE**.

Reason: technically healthy and visibly effected, but the rain initially read too much like an overlay placed on top of footage. The weather was not yet sufficiently integrated into the spatial logic of the real scene.

## P03 V2

Changes:

- reduced generic rain-overlay feeling through depth-layered rain and center/face protection;
- stronger cloud and water coupling;
- lightning bolt and reflected flash synchronized;
- local motivated bounce light on the subject during lightning;
- source-derived reflected/duplicate Brandi element introduced into the water as a surreal memory apparition rather than a generated person;
- stronger final camera push into the storm;
- continued use of real source motion throughout.

QC:

- frames: 130
- black frames: 0
- mean frame delta: 3.519861391490813
- p05 delta: 2.275317708333333
- p95 delta: 7.039265914351848
- mean luma proxy: 97.19487301905272
- SHA-256: `0828ebb9a8049e6976150f7ae53693c1837b838249d2d6c995b5d24725897dfd`

Decision: **REVISE / PROMISING**.

V2 is more cinematic than V1 and the lightning now belongs to both sky and water. However, it still does not independently satisfy the project-wide Magic Gate. It is a viable effect vocabulary to reuse in a later storm passage, but not yet a proof that the photograph/world has truly opened spatially.

## What this proof established

Keep these elements:

- real-motion storm source window;
- coupled sky + water lightning;
- motivated Gaussian light field from a real highlight;
- face/body rain protection;
- source-derived reflection apparition idea;
- asymmetric push into storm rather than uniform zoom.

Do not mistake visible overlays for dimensional magic.

## Next Magic Gate experiment

Move away from simply strengthening weather. Build a proof whose primary trick is **spatial entry into the real image**.

Preferred next directions:

1. recover/construct the cleanest possible waterfront background from actual neighboring source frames and alignment where possible;
2. preserve a real Brandi foreground plate;
3. create a stronger camera path that travels laterally/past the subject toward water/horizon;
4. use depth differential, water movement, atmospheric occlusion and foreground exit to hide disocclusion limitations;
5. alternatively use the sunglasses/water reflection as a source-derived optical portal if the clean-background reconstruction cannot support a convincing camera move;
6. pursue actual SfM / 3D Gaussian Splatting from the extracted real video frames when the available execution environment exposes the necessary reconstruction/training toolchain.

No full-song assembly is allowed from this proof.
