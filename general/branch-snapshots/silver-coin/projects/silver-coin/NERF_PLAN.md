# Silver Coin — Neural Radiance Field Plan

## User decision

Neural Radiance Fields are a required rendering component for this production.

## Runtime facts

The current environment has:

- CPU execution
- NumPy, SciPy, Pillow, and FFmpeg
- no GPU/CUDA
- no PyTorch
- no Nerfstudio
- no COLMAP
- no Tiny-CUDA-NN/Instant-NGP

## Honest implementation

Build a compact CPU neural radiance field whose MLP maps:

`(x, y, z, view_x, view_y, view_z) -> (density, red, green, blue)`

Use Fourier positional features and train it against designed pseudo-scene samples derived from the selected painted scene palette and depth/atmosphere layout.

Volume-render rays along controlled camera paths to produce:

- depth-dependent fog
- warm tavern light volumes
- smoke and airborne dust
- cool rain/mist volumes
- ember and coin-glint fields
- view-dependent highlights
- spatial motion and occlusion

Composite the learned volumetric output with multi-plane versions of the generated Living Pre-Raphaelite scenes. The detailed humans, instruments, architecture, and props remain painterly image layers; the NeRF supplies learned volumetric space and view response.

## Quality rule

The NeRF contribution must be visible and purposeful. It cannot be an unused technical token. Each rendered scene family must record:

- network/config version
- training seed and sample count
- loss/validation result
- camera path
- rendered loop path
- composite settings
- QC outcome

## Naming rule

Call the result **hybrid neural-radiance-field spatial rendering**.

Never call it a full photogrammetric/captured-scene NeRF, Nerfstudio reconstruction, Instant-NGP render, or complete 3D model.

## Scene families

1. cool wet village/road volume
2. warm threshold/window volume
3. smoky firelit tavern volume
4. coin-reflection transition volume
5. dawn/afterglow volume

## Checkpoint order

1. audio analysis
2. painted scene generation and artifact QC
3. NeRF renderer/config commit
4. per-family NeRF loop tests
5. composited scene tests
6. timeline assembly
7. final validation and archive
