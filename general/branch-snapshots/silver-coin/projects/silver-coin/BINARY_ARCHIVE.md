# Silver Coin — Binary Asset Archive

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`

Silver Coin uses a dual-layer recovery strategy:

1. **GitHub** stores reproducible code, effect recipes, timing/configuration, manifests, QC records, hashes, reduced visual recovery assets, and production history.
2. **ChatGPT Library** stores large source binaries and production assets that are unsuitable for ordinary Git storage.

## Persistent Library root

`/Video Creation/Silver Coin/`

Subfolders:

- `Canonical Sources/`
- `Hero Paintings/`
- `Effect Assets/`
- `Historical Renders/`
- `V8 Working/`

## Canonical sources

- `/Video Creation/Silver Coin/Canonical Sources/Silver Coin (Remastered).wav`
  - Library ID: `libfile_8b456915f20c81918f80e239f596a918`
- `/Video Creation/Silver Coin/Canonical Sources/imagine-d04b484c.mp4`
  - Library ID: `libfile_45897fcb550c8191a0efc3a90104c8a3`
- `/Video Creation/Silver Coin/Canonical Sources/imagine-5558fc80.mp4`
  - Library ID: `libfile_ff0beb90e9188191aaa9dc163aafbbd2`

The SHA-256 values already recorded in `ASSET_MANIFEST.json` remain the canonical identity check.

## Accepted V6/V8 hero paintings

- `01_enchanted_woodland_coin_portrait.png` — `libfile_d956cb9a8914819191cd6838a1ee319e`
- `02_golden_path_to_the_village.png` — `libfile_65b2168f8c30819189fa993425127ff4`
- `03_golden_haired_maiden_at_sunset.png` — `libfile_5318c84b3e788191a2a517fc425f6fec`
- `04_twilight_inn_beneath_the_flower_crown.png` — `libfile_dcb94e4e167881918f631e9fc7c343dc`
- `05_first_toast.png` — `libfile_5905feaada4c8191b8eefe29eaaaa46e`
- `06_communal_dance.png` — `libfile_d504227f865881919eb7e34f6dcf962e`
- `07_fiddler.png` — `libfile_838ee765787c81919d7097ae7bc93364`
- `08_clap_rhythm.png` — `libfile_348481f0cef48191b7ecf50c872c749e`

These are the locked visual sources for the V8 effects-first reconstruction. Do not generate replacement paintings merely to increase shot count.

## Effect assets currently archived

- `fx_gaussian_light_sweep.png` — `libfile_cf3b3efe87e48191af7fa25e5c100f1b`
- `fx_fog_puff.png` — `libfile_ca4b6b165b3c81918093ec6eb8095a09`
- `v7_title.png` — `libfile_e601628894a48191aeab3f5b9deffd4d`
- `v7_end.png` — `libfile_76a4c1612a1c8191b2e32a999030130c`

V8 should add each approved rendered loop/effect asset to `Effect Assets/` and record its Library path/ID here or in a versioned V8 manifest as soon as it passes QC.

## Historical renders

- `Silver_Coin_V6_Full_MusicDirected_720p.mp4` — `libfile_9dda0c3c65b881919316578e0439af38`
- `Silver_Coin_V7_REJECTED_YouTube_Final_720p24.mp4` — `libfile_b1eb515f197c8191a15f6ddc69d770a9`
- `Silver_Coin_V6_Hero_Recovery_Sheet.jpg` — `libfile_a84636b7448881918ad8fac36e62a20b`
- `Silver_Coin_V7_QC_contact_clean.jpg` — `libfile_43896d5380ec819189e27910954924e4`

V7 is retained only as a rejected historical effects experiment. Do not use it as the V8 visual/effects source.

## V8 persistence rule

For every new V8 loop or effected shot:

1. render locally from the locked paintings;
2. QC the loop/shot visually and temporally;
3. copy approved binary output into `/Video Creation/Silver Coin/V8 Working/` or `Effect Assets/`;
4. commit its filename, role, timing range, SHA-256, and Library path/ID to GitHub before proceeding far enough that losing the runtime would require redoing substantial work;
5. do not create a user-facing final/download master until the complete V8 effects pass is assembled and QC-approved.

This dual archive is the required recovery path for Silver Coin.