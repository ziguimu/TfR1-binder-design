from pathlib import Path
import json,glob,numpy as np
from Bio.PDB import MMCIFParser
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028')
p=next((R/'work/boltz_human_round1/TFR1_001/boltz_results_TFR1_001/predictions/TFR1_001').glob('confidence_*.json'))
d=json.loads(p.read_text()); print('confidence keys',d.keys()); print('pair chains',d.get('pair_chains_iptm')); print('chain pTM',d.get('chains_ptm'))
z=np.load(p.with_name(p.name.replace('confidence_','pae_').replace('.json','.npz'))); print('PAE shapes',[(k,z[k].shape) for k in z.files])
cif=p.with_name(p.name.replace('confidence_','').replace('.json','.cif')); s=MMCIFParser(QUIET=True).get_structure('x',cif)
for c in s[0]:
 rs=list(c.get_residues()); print('chain',c.id,'residues',len(rs),'span',[r.id[1] for r in rs[:2]],[r.id[1] for r in rs[-2:]])
