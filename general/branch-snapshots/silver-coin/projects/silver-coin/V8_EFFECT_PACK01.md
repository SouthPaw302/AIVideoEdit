# Silver Coin V8 — Effect Pack 01

**Status:** APPROVED / backed up  
**Source rule:** existing locked paintings only; no new source imagery  
**Format:** 1280x720 H.264, 24 fps, 4.0 s each

This is the first true frame-by-frame effects pack for the V8 reconstruction. These are standalone animated clips rendered from the accepted paintings, not filters applied to V6/V7.

## Approved clips

| Effect | SHA-256 | Library ID | Notes |
|---|---|---|---|
| `V8_FX01_forest_breath_hair_garland.mp4` | `99ea7fcb651485a6c58c72deebb762ca51b6b9a75e5b4b7321784842422f3f0c` | `libfile_e20640c8a05c8191bb887c7a0ee6cd26` | localized foliage motion, hair/crown drift, Gaussian sunlight, breathing camera |
| `V8_FX02_coin_glint.mp4` | `35cfd8e1af3bf690c70fa1baab0a3d511aefd8153eeab932991a1ed8dee947f8` | `libfile_1ba4b76c3de48191875f7d5f2a30c39f` | localized silver specular sweep and ring pulse |
| `V8_FX03_tavern_firelight_smoke.mp4` | `fd06f0a65bf2a59d3331b8511d7f3c309676f5ede6ead9e038510c2fb1d4303a` | `libfile_376277bed4d481918af5b3e33b8640e9` | candle flame, practical-light breathing, garland sway, advected smoke |
| `V8_FX04_fiddler_impact.mp4` | `a80a20c303952fdae80880cc8ae5b2622dbe535a06ff0cb6665992131089008b` | `libfile_388454be35f881919c10f73e4f6e4440` | bow-region motion, rhythmic camera impacts, sparse sparks/glints |
| `V8_FX05_communal_crowd_sway.mp4` | `c7f1c296673ba9e927f6ba49cb51654b534727bbe8622c77639389d36eed9845` | `libfile_c56cea16cf888191aaeb1579ea0476d4` | separate left/right crowd layers sway around protected central heroine |
| `V8_FX06_lightning_wet_reflection.mp4` | `5acb928a337c499fdf240e94371dd37ad6b128cf5749e5bc010e83fe07f06ef4` | `libfile_15e3687d0974819188626dfd69510be0` | branching lightning, sky flash, wet-road reflected flash and shimmer |
| `V8_FX07_gaussian_light_shafts.mp4` | `bf71a7bdeb1c1e172ae5a5676d888fa95153bc01db05e79646cea31c3edba90a` | `libfile_6222b68d4c088191bc2cdd3b5fdc233e` | visibly moving 2D Gaussian light shafts/haze plus loop-safe camera path |
| `V8_FX08_fog_pigment_travel.mp4` | `88a24b139f14ced56d97f118ae68d07a9a8427f5eb5c60ce8da60e77000c4588` | `libfile_cda4d717e0e081918133cba7e7dd793c` | non-loop transition: low-frequency pigment/fog travel from forest to inn |

## QC

All clips were decoded as 96-frame 4-second assets at 24 fps and inspected via contact sheet and motion metrics. Loop assets were checked for first/last seam behavior. `FX08` is a transition and is intentionally not loop-seam constrained.

Persistent QC files:

- `V8_FX_PACK01_MANIFEST.json` — Library ID `libfile_aa087089451c8191a7413a05806145e0`
- `V8_FX_PACK_QC_CONTACT.jpg` — Library ID `libfile_1a2b86ea70cc8191bfb36b1950791cd5`
- `V8_FX_PACK_QC_METRICS.json` — Library ID `libfile_816c66d44b1c8191a0aee271d9f45e80`

## Claim guard

`FX07` uses image-space Gaussian fields, not 3D Gaussian Splatting. Actual 3DGS remains a separate spatial method in the repository catalog. V8 may use 2.5D parallax and existing compact-NeRF atmosphere in addition to these clips, but detailed subject geometry remains the original painting.
