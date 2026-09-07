# ATD-FX-001 — Threshold Prism Bleed

## Purpose
Turn a door opening into a dimensional transfer event without covering the whole frame in a generic glow or rainbow filter.

## Research basis
The design borrows from real optical behaviors: light can diffract/spread at edges and apertures, different wavelengths can separate under dispersive/diffractive behavior, scattering can make suspended media reveal a light path, and aperture/obstruction geometry can influence diffraction pattern shape. The production implementation is intentionally artistic and computationally bounded.

## Visual construction
1. derive a narrow mask from the luminous threshold/door edge
2. build oriented edge-normal rays rather than radial full-screen bloom
3. split the edge energy into restrained R/G/B wavelength-offset lobes
4. shape intensity with a central peak plus decaying side lobes to evoke diffraction/interference structure
5. advect sparse dust/scatter only where the threshold light volume exists
6. insert low-opacity ghost exposures of alternate rooms/selves into selected side lobes
7. drive opening width, side-lobe separation, dust density, and ghost exposure from smoothed audio controls
8. collapse all side lobes back into neutral light as the transition completes

## Truthfulness
Do not call this a physical diffraction renderer, ray tracer, wave-optics solver, hologram, NeRF, or 3DGS. It is a stylized 2D/2.5D compositing effect informed by optical behavior.

## Acceptance criteria
- localized to threshold geometry
- effect visible at normal playback speed
- stable edge tracking
- no uncontrolled global RGB split
- no more than brief ghost-image dominance
- transition ends in a clean destination frame
- actual encoded proof must preserve the effect
