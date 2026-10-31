# TfR1 challenge 4 execution record

Approved scope: de novo 60–100 aa protein minibinders; human-first; mouse optional; avoid transferrin binding; His optional without pH validation; 72-hour wall-clock budget; only passing candidates, even fewer than three. No submission or synthesis.

Project root changed to D:\PRP\TfR1_challenge4_20261028 at the user's request.

Stages: prepare and smoke test; 64 initial backbones (up to 192); 8 MPNN sequences/backbone; up to 96 human initial predictions; human finalists 3 Boltz seeds and 2 ColabFold models; mouse bonus; audit and delivery.

Acceptance: Boltz >=2/3 runs with binder pLDDT >=85, pair ipTM >=0.70, bidirectional interface PAE <=10 A, target-aligned binder CA RMSD <=2.5 A; >=1/2 ColabFold models supports same interface; buried area (delta SASA/2) >=500 A2; no severe <2 A cross-chain clashes; compatible with full dimer, glycans, and transferrin.

Ruling: This is a standalone scientific workspace, not a git development branch. Keep all provenance and logs here; do not initialize or modify unrelated repositories.

Ruling: Old ipSAE approximation is excluded; implement and test explicit chain/token mapping and symmetric interface PAE instead.

Status: preparing target inputs. No candidate sequences generated yet.

2026-10-28T17:19:00.091054+08:00 patch1_60_80: exit=0, structures=16/16

2026-10-28T17:50:43.529084+08:00 patch1_80_100: exit=0, structures=16/16

2026-10-28T18:16:57.582634+08:00 patch2_60_80: exit=0, structures=16/16

2026-10-28T18:46:47.681624+08:00 patch2_80_100: exit=0, structures=16/16

2026-10-28T21:03:14.549822+08:00 ProteinMPNN patch1_60_80_0: 16 sequences

2026-10-28T21:03:18.308151+08:00 ProteinMPNN patch1_60_80_1: 16 sequences

2026-10-28T21:03:22.635414+08:00 ProteinMPNN patch1_60_80_10: 16 sequences

2026-10-28T21:03:26.651785+08:00 ProteinMPNN patch1_60_80_11: 16 sequences

2026-10-28T21:03:30.719170+08:00 ProteinMPNN patch1_60_80_12: 16 sequences

2026-10-28T21:03:35.232976+08:00 ProteinMPNN patch1_60_80_13: 16 sequences

2026-10-28T21:03:39.216109+08:00 ProteinMPNN patch1_60_80_14: 16 sequences

2026-10-28T21:03:43.334456+08:00 ProteinMPNN patch1_60_80_15: 16 sequences

2026-10-28T21:03:47.207101+08:00 ProteinMPNN patch1_60_80_2: 16 sequences

2026-10-28T21:03:51.116744+08:00 ProteinMPNN patch1_60_80_3: 16 sequences

2026-10-28T21:03:55.241661+08:00 ProteinMPNN patch1_60_80_4: 16 sequences

2026-10-28T21:03:59.297759+08:00 ProteinMPNN patch1_60_80_5: 16 sequences

2026-10-28T21:04:03.249269+08:00 ProteinMPNN patch1_60_80_6: 16 sequences

2026-10-28T21:04:07.625048+08:00 ProteinMPNN patch1_60_80_7: 16 sequences

2026-10-28T21:04:11.732384+08:00 ProteinMPNN patch1_60_80_8: 16 sequences

2026-10-28T21:04:15.747997+08:00 ProteinMPNN patch1_60_80_9: 16 sequences

2026-10-28T21:04:20.082794+08:00 ProteinMPNN patch1_80_100_0: 16 sequences

2026-10-28T21:04:23.957084+08:00 ProteinMPNN patch1_80_100_1: 16 sequences

2026-10-28T21:04:28.232483+08:00 ProteinMPNN patch1_80_100_10: 16 sequences

2026-10-28T21:04:32.380939+08:00 ProteinMPNN patch1_80_100_11: 16 sequences

2026-10-28T21:04:36.331597+08:00 ProteinMPNN patch1_80_100_12: 16 sequences

2026-10-28T21:04:40.446334+08:00 ProteinMPNN patch1_80_100_13: 16 sequences

2026-10-28T21:04:44.378333+08:00 ProteinMPNN patch1_80_100_14: 16 sequences

2026-10-28T21:04:48.339199+08:00 ProteinMPNN patch1_80_100_15: 16 sequences

2026-10-28T21:04:52.277382+08:00 ProteinMPNN patch1_80_100_2: 16 sequences

2026-10-28T21:04:56.667769+08:00 ProteinMPNN patch1_80_100_3: 16 sequences

2026-10-28T21:05:00.785632+08:00 ProteinMPNN patch1_80_100_4: 16 sequences

2026-10-28T21:05:04.656229+08:00 ProteinMPNN patch1_80_100_5: 16 sequences

2026-10-28T21:05:08.667602+08:00 ProteinMPNN patch1_80_100_6: 16 sequences

2026-10-28T21:05:12.725992+08:00 ProteinMPNN patch1_80_100_7: 16 sequences

2026-10-28T21:05:16.575173+08:00 ProteinMPNN patch1_80_100_8: 16 sequences

2026-10-28T21:05:20.585243+08:00 ProteinMPNN patch1_80_100_9: 16 sequences

2026-10-28T21:05:24.381665+08:00 ProteinMPNN patch2_60_80_0: 16 sequences

2026-10-28T21:05:28.052851+08:00 ProteinMPNN patch2_60_80_1: 16 sequences

2026-10-28T21:05:32.035049+08:00 ProteinMPNN patch2_60_80_10: 16 sequences

2026-10-28T21:05:35.891485+08:00 ProteinMPNN patch2_60_80_11: 16 sequences

2026-10-28T21:05:39.812242+08:00 ProteinMPNN patch2_60_80_12: 16 sequences

2026-10-28T21:05:43.577576+08:00 ProteinMPNN patch2_60_80_13: 16 sequences

2026-10-28T21:05:47.254683+08:00 ProteinMPNN patch2_60_80_14: 16 sequences

2026-10-28T21:05:51.047812+08:00 ProteinMPNN patch2_60_80_15: 16 sequences

2026-10-28T21:05:54.826527+08:00 ProteinMPNN patch2_60_80_2: 16 sequences

2026-10-28T21:05:58.553387+08:00 ProteinMPNN patch2_60_80_3: 16 sequences

2026-10-28T21:06:02.658612+08:00 ProteinMPNN patch2_60_80_4: 16 sequences

2026-10-28T21:06:06.639406+08:00 ProteinMPNN patch2_60_80_5: 16 sequences

2026-10-28T21:06:10.756409+08:00 ProteinMPNN patch2_60_80_6: 16 sequences

2026-10-28T21:06:14.478792+08:00 ProteinMPNN patch2_60_80_7: 16 sequences

2026-10-28T21:06:18.294435+08:00 ProteinMPNN patch2_60_80_8: 16 sequences

2026-10-28T21:06:22.027470+08:00 ProteinMPNN patch2_60_80_9: 16 sequences

2026-10-28T21:06:25.991075+08:00 ProteinMPNN patch2_80_100_0: 16 sequences

2026-10-28T21:06:29.838275+08:00 ProteinMPNN patch2_80_100_1: 16 sequences

2026-10-28T21:06:33.910842+08:00 ProteinMPNN patch2_80_100_10: 16 sequences

2026-10-28T21:06:37.823088+08:00 ProteinMPNN patch2_80_100_11: 16 sequences

2026-10-28T21:06:41.707501+08:00 ProteinMPNN patch2_80_100_12: 16 sequences

2026-10-28T21:06:45.801956+08:00 ProteinMPNN patch2_80_100_13: 16 sequences

2026-10-28T21:06:49.840340+08:00 ProteinMPNN patch2_80_100_14: 16 sequences

2026-10-28T21:06:53.637823+08:00 ProteinMPNN patch2_80_100_15: 16 sequences

2026-10-28T21:06:57.541781+08:00 ProteinMPNN patch2_80_100_2: 16 sequences

2026-10-28T21:07:01.478479+08:00 ProteinMPNN patch2_80_100_3: 16 sequences

2026-10-28T21:07:05.612738+08:00 ProteinMPNN patch2_80_100_4: 16 sequences

2026-10-28T21:07:09.662364+08:00 ProteinMPNN patch2_80_100_5: 16 sequences

2026-10-28T21:07:13.737484+08:00 ProteinMPNN patch2_80_100_6: 16 sequences

2026-10-28T21:07:17.661381+08:00 ProteinMPNN patch2_80_100_7: 16 sequences

2026-10-28T21:07:21.541250+08:00 ProteinMPNN patch2_80_100_8: 16 sequences

2026-10-28T21:07:25.539403+08:00 ProteinMPNN patch2_80_100_9: 16 sequences

2026-10-28T21:17:36.658285+08:00 Boltz human TFR1_001: complete

2026-10-28T21:18:17.194043+08:00 Boltz human TFR1_002: complete

2026-10-28T21:18:57.351928+08:00 Boltz human TFR1_003: complete

2026-10-28T21:19:39.418698+08:00 Boltz human TFR1_004: complete

2026-10-28T21:20:20.880794+08:00 Boltz human TFR1_005: complete

2026-10-28T21:21:04.329296+08:00 Boltz human TFR1_006: complete

2026-10-28T21:21:45.293866+08:00 Boltz human TFR1_007: complete

2026-10-28T21:22:27.202705+08:00 Boltz human TFR1_008: complete

2026-10-28T21:23:07.876101+08:00 Boltz human TFR1_009: complete

2026-10-28T21:23:48.372920+08:00 Boltz human TFR1_010: complete

2026-10-28T21:24:28.338729+08:00 Boltz human TFR1_011: complete

2026-10-28T21:25:09.586220+08:00 Boltz human TFR1_012: complete

2026-10-28T21:25:49.294515+08:00 Boltz human TFR1_013: complete

2026-10-28T21:26:28.447718+08:00 Boltz human TFR1_014: complete

2026-10-28T21:27:09.628054+08:00 Boltz human TFR1_015: complete

2026-10-28T21:27:50.376112+08:00 Boltz human TFR1_016: complete

2026-10-28T21:28:31.512692+08:00 Boltz human TFR1_017: complete

2026-10-28T21:29:12.406087+08:00 Boltz human TFR1_018: complete

2026-10-28T21:29:51.529792+08:00 Boltz human TFR1_019: complete

2026-10-28T21:30:32.537325+08:00 Boltz human TFR1_020: complete

2026-10-28T21:31:13.053706+08:00 Boltz human TFR1_021: complete

2026-10-28T21:31:52.999558+08:00 Boltz human TFR1_022: complete

2026-10-28T21:32:31.987048+08:00 Boltz human TFR1_023: complete

2026-10-28T21:33:12.085699+08:00 Boltz human TFR1_024: complete

2026-10-28T21:33:53.011989+08:00 Boltz human TFR1_025: complete

2026-10-28T21:34:32.242272+08:00 Boltz human TFR1_026: complete

2026-10-28T21:35:11.410031+08:00 Boltz human TFR1_027: complete

2026-10-28T21:35:50.621156+08:00 Boltz human TFR1_028: complete

2026-10-28T21:36:29.898804+08:00 Boltz human TFR1_029: complete

2026-10-28T21:37:11.020396+08:00 Boltz human TFR1_030: complete

2026-10-28T21:37:49.932672+08:00 Boltz human TFR1_031: complete

2026-10-28T21:38:28.685167+08:00 Boltz human TFR1_032: complete

2026-10-28T21:39:07.329544+08:00 Boltz human TFR1_033: complete

2026-10-28T21:39:48.392498+08:00 Boltz human TFR1_034: complete

2026-10-28T21:40:29.238417+08:00 Boltz human TFR1_035: complete

2026-10-28T21:41:08.813633+08:00 Boltz human TFR1_036: complete

2026-10-28T21:41:47.541514+08:00 Boltz human TFR1_037: complete

2026-10-28T21:42:27.115532+08:00 Boltz human TFR1_038: complete

2026-10-28T21:43:06.779953+08:00 Boltz human TFR1_039: complete

2026-10-28T21:43:46.969547+08:00 Boltz human TFR1_040: complete

2026-10-28T21:44:24.268549+08:00 Boltz human TFR1_041: complete

2026-10-28T21:45:03.093884+08:00 Boltz human TFR1_042: complete

2026-10-28T21:45:42.257419+08:00 Boltz human TFR1_043: complete

2026-10-28T21:46:21.466931+08:00 Boltz human TFR1_044: complete

2026-10-28T21:47:01.507643+08:00 Boltz human TFR1_045: complete

2026-10-28T21:47:42.478170+08:00 Boltz human TFR1_046: complete

2026-10-28T21:48:21.419347+08:00 Boltz human TFR1_047: complete

2026-10-28T21:49:01.333851+08:00 Boltz human TFR1_048: complete

2026-10-28T21:49:40.043092+08:00 Boltz human TFR1_049: complete

2026-10-28T21:50:20.303556+08:00 Boltz human TFR1_050: complete

2026-10-28T21:51:00.726354+08:00 Boltz human TFR1_051: complete

2026-10-28T21:51:40.183246+08:00 Boltz human TFR1_052: complete

2026-10-28T21:52:19.321676+08:00 Boltz human TFR1_053: complete

2026-10-28T21:52:59.299096+08:00 Boltz human TFR1_054: complete

2026-10-28T21:53:38.219471+08:00 Boltz human TFR1_055: complete

2026-10-28T21:54:15.896533+08:00 Boltz human TFR1_056: complete

2026-10-28T21:54:56.349789+08:00 Boltz human TFR1_057: complete

2026-10-28T21:55:35.995465+08:00 Boltz human TFR1_058: complete

2026-10-28T21:56:15.724821+08:00 Boltz human TFR1_059: complete

2026-10-28T21:56:57.444727+08:00 Boltz human TFR1_060: complete

2026-10-28T21:57:38.397729+08:00 Boltz human TFR1_061: complete

2026-10-28T21:58:17.869103+08:00 Boltz human TFR1_062: complete

2026-10-28T21:58:58.984941+08:00 Boltz human TFR1_063: complete

2026-10-28T21:59:39.422977+08:00 Boltz human TFR1_064: complete

2026-10-28T22:00:19.833146+08:00 Boltz human TFR1_065: complete

2026-10-28T22:00:59.253676+08:00 Boltz human TFR1_066: complete

2026-10-28T22:01:38.127983+08:00 Boltz human TFR1_067: complete

2026-10-28T22:02:18.793351+08:00 Boltz human TFR1_068: complete

2026-10-28T22:02:57.815117+08:00 Boltz human TFR1_069: complete

2026-10-28T22:03:37.146396+08:00 Boltz human TFR1_070: complete

2026-10-28T22:04:17.474904+08:00 Boltz human TFR1_071: complete

2026-10-28T22:04:58.142242+08:00 Boltz human TFR1_072: complete

2026-10-28T22:05:38.849972+08:00 Boltz human TFR1_073: complete

2026-10-28T22:06:19.154722+08:00 Boltz human TFR1_074: complete

2026-10-28T22:06:58.902227+08:00 Boltz human TFR1_075: complete

2026-10-28T22:07:38.836934+08:00 Boltz human TFR1_076: complete

2026-10-28T22:08:18.958984+08:00 Boltz human TFR1_077: complete

2026-10-28T22:08:59.079233+08:00 Boltz human TFR1_078: complete

2026-10-28T22:09:39.082935+08:00 Boltz human TFR1_079: complete

2026-10-28T22:10:19.061080+08:00 Boltz human TFR1_080: complete

2026-10-28T22:10:57.773919+08:00 Boltz human TFR1_081: complete

2026-10-28T22:11:37.229722+08:00 Boltz human TFR1_082: complete

2026-10-28T22:12:16.647862+08:00 Boltz human TFR1_083: complete

2026-10-28T22:12:55.503164+08:00 Boltz human TFR1_084: complete

2026-10-28T22:13:35.514216+08:00 Boltz human TFR1_085: complete

2026-10-28T22:14:14.160032+08:00 Boltz human TFR1_086: complete

2026-10-28T22:14:52.805905+08:00 Boltz human TFR1_087: complete

2026-10-28T22:15:32.528611+08:00 Boltz human TFR1_088: complete

2026-10-28T22:16:12.712955+08:00 Boltz human TFR1_089: complete

2026-10-28T22:16:52.104034+08:00 Boltz human TFR1_090: complete

2026-10-28T22:17:31.221803+08:00 Boltz human TFR1_091: complete

2026-10-28T22:18:10.798451+08:00 Boltz human TFR1_092: complete

2026-10-28T22:18:50.085778+08:00 Boltz human TFR1_093: complete

2026-10-28T22:19:30.899972+08:00 Boltz human TFR1_094: complete

2026-10-28T22:20:10.583598+08:00 Boltz human TFR1_095: complete

2026-10-28T22:20:53.657614+08:00 Boltz human TFR1_096: complete

2026-10-29T00:08:00+08:00 Round 2 started. Positive-control calibration completed; RFdiffusion is generating 32 backbones using apo 11QC and 6WRW/2DS25.5-bound target conformations. A WSL continuation controller is waiting to run geometry audit, ProteinMPNN, Boltz ensemble screening, and final export without further manual handoff.

2026-10-29T08:00:13.645123+08:00 Round2 final candidates complete: 5 sequences. See round2/final/final_candidates.fasta and report.

2026-10-29T11:41:38.830647+08:00 Round2 final candidates complete: 5 sequences. See round2/final/final_candidates.fasta and report.
