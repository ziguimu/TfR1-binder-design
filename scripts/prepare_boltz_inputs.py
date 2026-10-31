from pathlib import Path
import csv,json
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); IN=R/'inputs/boltz_round1'; IN.mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader((R/'work/human_shortlist.csv').open()))
target=json.loads((R/'inputs/target_metadata.json').read_text())['human_crop_sequence']
for r in rows:
 name=r['candidate_id']; b=r['sequence']
 y=f"version: 1\nsequences:\n  - protein:\n      id: A\n      sequence: {target}\n      msa: empty\n  - protein:\n      id: B\n      sequence: {b}\n      msa: empty\n"
 (IN/f'{name}.yaml').write_text(y)
print(f'prepared {len(rows)} Boltz human complex inputs; target={len(target)} aa')

