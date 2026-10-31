from pathlib import Path
import csv,json
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); row=next(r for r in csv.DictReader((R/'work/human_shortlist.csv').open()) if r['candidate_id']=='TFR1_041')
t=json.loads((R/'inputs/target_metadata.json').read_text())['human_crop_sequence']; b=row['sequence']
y=f"version: 1\nsequences:\n  - protein:\n      id: A\n      sequence: {t}\n      msa: empty\n  - protein:\n      id: B\n      sequence: {b}\n      msa: empty\ntemplates:\n  - pdb: /mnt/d/PRP/TfR1_challenge4_20261028/inputs/human_apical.pdb\n    chain_id: A\n    template_id: A\n"
(R/'inputs/boltz_round1'/'TFR1_041_template.yaml').write_text(y)
