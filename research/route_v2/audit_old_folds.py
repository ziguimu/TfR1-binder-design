from pathlib import Path
import json,csv,numpy as np
from Bio.PDB import PDBParser,MMCIFParser,Superimposer
from Bio.SeqUtils import seq1
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028');P=R/'research/route_v2'
pp=PDBParser(QUIET=True);cp=MMCIFParser(QUIET=True)
ref=pp.get_structure('r',R/'inputs/human_apical.pdb')[0]['A']
def ca(c):return [r['CA'] for r in c if r.id[0]==' ' and 'CA' in r]
def sequence(c):return ''.join(seq1(r.resname) for r in c if r.id[0]==' ' and 'CA' in r)
def rms(a,b):
 s=Superimposer();s.set_atoms(ca(a),ca(b));return float(s.rms)
rows=[]
for v in csv.DictReader((R/'work/human_shortlist.csv').open()):
 n=v['candidate_id']; f=R/'work/boltz_human_round1'/n/f'boltz_results_{n}'/'predictions'/n/f'{n}_model_0.cif'
 if not f.exists():continue
 pred=cp.get_structure(n,f)[0];design=pp.get_structure('d',R/'work/backbones'/f"{v['backbone']}.pdb")[0]
 rows.append({'candidate_id':n,'target_sequence_match':sequence(ref)==sequence(pred['A']),'binder_sequence_match':sequence(pred['B'])==v['sequence'],'target_refold_rmsd_A':rms(ref,pred['A']),'binder_self_rmsd_A':rms(design['B'],pred['B'])})
out=P/'round1_fold_audit.csv'
with out.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('count',len(rows),'target_sequence_matches',sum(x['target_sequence_match'] for x in rows),'binder_sequence_matches',sum(x['binder_sequence_match'] for x in rows))
for k in ['target_refold_rmsd_A','binder_self_rmsd_A']:
 a=np.array([v[k] for v in rows]);print(k,'min/median/max',np.round([a.min(),np.median(a),a.max()],2).tolist())
for v in rows:
 if v['candidate_id'] in ['TFR1_041','TFR1_015','TFR1_088','TFR1_073','TFR1_066']:print(v)
name='TFR1_041_template';f=R/'work/boltz_template_probe'/f'boltz_results_{name}'/'predictions'/name/f'{name}_model_0.cif'
pred=cp.get_structure('t',f)[0];d=pp.get_structure('d',R/'work/backbones/patch1_60_80_2.pdb')[0]
print('template_probe',{'target_refold_rmsd_A':rms(ref,pred['A']),'binder_self_rmsd_A':rms(d['B'],pred['B'])})

