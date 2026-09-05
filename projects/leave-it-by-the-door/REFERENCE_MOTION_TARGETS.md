# Leave It by the Door — Reference Motion Targets

Updated: 2026-09-05 UTC

The two user-supplied clips `imagine-f9c3e46d.mp4` and `imagine-1fb7bb42.mp4` are the current quality/motion references for the rebuild.

## Measured source properties

Both references are true 24 fps H.264, 560×560, ~6.04 seconds.

- `imagine-f9c3e46d.mp4`
  - 24 fps
  - video bitrate ≈ 5.15 Mbps
  - adjacent-frame mean absolute difference at normalized 320×180 analysis size ≈ 10.33
  - p10 ≈ 5.10, p90 ≈ 15.55
  - visual behavior: high-energy evolving waves, cloud deformation, fabric/hair flow, object drift, strong internal scene motion

- `imagine-1fb7bb42.mp4`
  - 24 fps
  - video bitrate ≈ 3.58 Mbps
  - adjacent-frame mean absolute difference at normalized 320×180 analysis size ≈ 5.32
  - p10 ≈ 0.77, p90 ≈ 10.66
  - visual behavior: slower cinematic cloud/wave evolution, flowing hair/fabric, warm/cool light migration, layered depth motion

## Direction adopted

The rebuild must NOT fake 24 fps by duplicating or interpolating a 10 fps working pass.

Required:
- every delivered frame is generated/rendered at native 24 fps
- internal scene motion first, camera motion second
- subjects/faces remain identity-stable
- separate semantic motion regions for ocean, clouds, rain, hair, fabric, smoke/fire, crowd, reflections and particles
- reference-derived optical-flow signatures may drive organic deformation instead of generic sine-wave wobble
- atmosphere and lighting should migrate through the frame over time
- wet surfaces should carry independent reflection/ripple motion
- rain/spray/embers use continuous trajectories across native frames
- final master target: 1920×1080, native 24 fps, H.264 CRF 16–18 or visually equivalent, high-bitrate AAC

## Native proof 01

Sandbox proof produced:
`Leave_It_By_The_Door_NATIVE24_LivingScene_PROOF01_720p24.mp4`

Properties:
- 1280×720
- 24 fps native
- 144 rendered frames / 6.0 s
- H.264 video bitrate ≈ 12.2 Mbps
- AAC ≈ 297 kbps
- adjacent-frame mean difference at normalized 320×180 ≈ 2.20

Proof 01 validates the native-24 pipeline and localized optical-flow transfer. Its motion energy is still deliberately below the supplied references. Subsequent shot tuning should increase organic internal motion toward the second reference's range while preserving faces and painted identity.
