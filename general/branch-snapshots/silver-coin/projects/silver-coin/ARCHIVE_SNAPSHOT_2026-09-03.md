# Silver Coin — Exhaustive Media Archive Snapshot

**Snapshot date:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`

Before the V8 effects-first reconstruction, the active runtime was exhaustively scanned and checksummed.

## Snapshot coverage

- **181 media files total**
- **150 images** (`.png`, `.jpg`, `.jpeg`)
- **30 videos** (`.mp4`)
- **1 canonical WAV**
- Total runtime media size: **1,003,223,633 bytes**

The set includes canonical sources, all accepted hero paintings, old/rejected storyboard imagery, generated intermediates, V3–V7 renders, V6/V7 chunks, QC frames/contact sheets, effect test assets, and rejected experiments. Rejected work is preserved intentionally as production history.

The complete per-file SHA-256 ledger is stored persistently at:

`/Video Creation/Silver Coin/Archive Snapshots/ALL_MEDIA_SHA256.json`

Library ID: `libfile_6af6a88f14208191b1d492dd622f5c01`

## Verified archive volumes

Each ZIP was test-opened successfully before upload and then SHA-256 recorded.

| Archive | SHA-256 | Bytes | Library ID |
|---|---|---:|---|
| `Silver_Coin_All_Images_2026-09-03.zip` | `8525f34c558c7271f41db98fe6ed71936cf02e4f8fc55b0c106253526c7ae81e` | 80,981,226 | `libfile_8cbc23b8fdcc81918b0220b86ca8b98a` |
| `Silver_Coin_Canonical_Audio_2026-09-03.zip` | `c71e24cee5531160142dab1648d53000c510c714813e776fb87b677b44e164b3` | 39,851,393 | `libfile_cd163b3a701c8191976ef3d9a5273319` |
| `Silver_Coin_All_Videos_part01_2026-09-03.zip` | `1889f98c97f620c6e281b18c4d9d3fd9fe1a54b79e9a7607c9abbe31e616d2e0` | 209,975,447 | `libfile_12e51946f6e481919afda815aff887e2` |
| `Silver_Coin_All_Videos_part02_2026-09-03.zip` | `4e53c518d76bc798f4097f108f3f28eb1074cd98a3f5bba4d4a14a23c3fc6155` | 219,080,665 | `libfile_82b679bfc394819194691a8ff7fe4bea` |
| `Silver_Coin_All_Videos_part03_2026-09-03.zip` | `cd82176fe1bd87b79ff1e4d1c06dd209bf420c1420ad572aa791c29d94ecfa25` | 220,806,668 | `libfile_512afd7186e08191814db1f9ccecb529` |
| `Silver_Coin_All_Videos_part04_2026-09-03.zip` | `a5506cc011eb2f1defdc75c728cb10c5ff65b7077b81e522060d6637a3250fb8` | 229,701,777 | `libfile_4161bcf5a85881919a8acc9f1f637a71` |
| `Silver_Coin_All_Videos_part05_2026-09-03.zip` | `44896e5722ab0688b353a004be1d25dfc13c44a8e03777fa81c15aba20b8c85b` | 1,369,072 | `libfile_c7c24051d1988191a061559f98ee80db` |

Archive-volume metadata is also stored at:

`/Video Creation/Silver Coin/Archive Snapshots/ARCHIVE_VOLUMES.json`

Library ID: `libfile_d291dec9fc988191a735db1ff44b5a75`

## Recovery rule

GitHub remains the reproducible source of truth for code, timelines, effect recipes, decisions, hashes, QC, and archive indexes. ChatGPT Library holds the large exact binary snapshots. Any V8 effect clip that passes QC must be copied to Library and indexed in GitHub before the production advances far enough that losing the runtime would require substantial rework.
