# TfR1 challenge 4 — provisional candidate package

These five sequences are computational follow-up candidates selected from 96 human-target Boltz predictions by interface confidence and distinct design backbones. They are not validated binders or affinity-ranked measurements.

## Structural result

The round-one gate passed **0/96**. Some predictions have high pair-chain ipTM (0.737–0.813) and low interface PAE, but all five fail the design-pose retention check: binder backbone RMSD after target alignment ranges from 29.7 to 50.3 Å. A template-assisted re-prediction of TFR1_041 reduced pair ipTM to 0.183, with interface PAE 18.12 Å and binder pLDDT 76.0. This disagreement makes the apparent high Boltz interface scores unreliable as evidence for binding.

## Recommended use

Treat the FASTA as a short list for future structural or experimental follow-up only. Human target was used for ranking. Mouse cross-reactivity has not been assessed. No pH-response feature was deliberately engineered; these sequences contain no histidines. No binding affinity was experimentally measured.

Full round-one metrics: ../work/human_boltz_metrics.csv.

## Additional local cross-check attempt

An offline ColabFold/AF2-Multimer single-sequence cross-check was attempted on the five provisional sequences. The first job stayed in initialization for over three minutes and consumed about 89% of WSL memory without producing a structure, so it was stopped. No binder sequences were sent to an external MSA service. A misdirected cache lookup briefly created a 29 MB partial model-weight file; it was deleted, and no ColabFold process remains running.
