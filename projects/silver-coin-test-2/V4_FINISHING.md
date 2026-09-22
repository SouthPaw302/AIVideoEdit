# Silver Coin Test 2 — V4c finishing record

Branch: `song/silver-coin-test-2`. Do not merge this picture edit into `main`.

## Picture and sound

- Master: `Silver_Coin_Test2_v4c_Alpha_Bookends_1280x720_24fps.mp4`
- SHA-256: `12730b6ca3a9f6889bb917836e4c5dc53331b18009391d08b96fc7981efad178`
- Drive backup: `1w-2T5cDuy6rGyWZrHiF9h34Z2BJq4mYa` in the Silver Coin final-masters archive; metadata readback confirmed 93,356,352 bytes.
- 1280 × 720, 24 fps, 4,979 frames, 207.458333 seconds, H.264/AAC, Rec.709 limited-range signaling.
- Audio: unchanged canonical `media/Silver Coin (Remastered).wav`, encoded to AAC 48 kHz for delivery. Video and audio endpoints differ by 0.0183 seconds, less than one frame.
- The accepted V3b Test 2 picture/FX is retained between the modified sections. No old-video reference clip was introduced.

## Changed sections (frame-accurate)

| Frames | Picture decision |
| --- | --- |
| 0–141 | New intro: main-branch FX picture with title, transparent archived light sweep and fog layers; first three shots and music timing preserved. |
| 142–2127 | Existing V3b Test 2 picture/FX. |
| 2128–2401 | Replace SC15 backward-hand image: tight heroine/merchant crop without that hand, followed by a moving close-up of the silver coin on the table. At 1:33 the table coin is visible. |
| 2402–4871 | Existing V3b Test 2 picture/FX. |
| 4872–4978 | New outro: independently moving transparent heroine over a clean painted dawn plate, with archived fog, title, dissolve-in and final fade. |

## Layer sources

- `fx_assets/v4/heroine_outro_alpha.png` and `fx_assets/v4/dawn_clean_plate.png`: created from Test 2's `hero_025.png` for foreground/background separation, not from an old video.
- `fx_assets/v4/fx_gaussian_light_sweep.png` and `fx_assets/v4/fx_fog_puff.png`: archived original Silver Coin transparent effects, recovered from the Drive archive indexed by the Git branch.
- `analysis/INTRO_v4_proof.ass` and `analysis/OUTRO_v4_proof.ass`: final intro/outro titles.
- The generic FX engine is the version promoted on `main` under `general/reusable/fx_v2/`; the V3 picture had already used it. V4 does not promote a new canonical effect.

## QC

- Fresh `fx_v4.lock.json` created and verified after the older `fx.lock.json` failed because its manifest hash was stale; current gate result: PASS.
- `verify_promoted_effects.py`: PASS for all 52 promoted effects.
- Final master full-decode: PASS; no 0.3-second black intervals; frame count and Rec.709 tags verified.
- Visual inspection: intro, 1:33 hand replacement, scene boundaries and layered outro checked. The first outro test had a foreground pop; V4c uses a short dissolve to remove it.
