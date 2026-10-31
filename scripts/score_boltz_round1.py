from pathlib import Path
import csv,json,math
import numpy as np
from Bio.PDB import MMCIFParser,PDBParser,ShrakeRupley,Superimposer
from Bio.SeqUtils import seq1
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); preds=R/'work/boltz_human_round1'; back=R/'work/backbones'
parser=MMCIFParser(QUIET=True); pp=PDBParser(QUIET=True); sr=ShrakeRupley(n_points=100)
rows=[]
def ca_coords(ch):
 rs=[r for r in ch if r.id[0]==' ' and 'CA' in r]
 return rs,np.array([r['CA'].coord for r in rs],dtype=float)
def sasa(st):sr.compute(st,level='S');return float(st.sasa)
for info in csv.DictReader((R/'work/human_shortlist.csv').open()):
 name=info['candidate_id']; root=preds/name/f'boltz_results_{name}'/ 'predictions'/name
 cj=root/f'confidence_{name}_model_0.json'; cif=root/f'{name}_model_0.cif'; pae_path=root/f'pae_{name}_model_0.npz'
 if not (cj.exists() and cif.exists() and pae_path.exists()): continue
 conf=json.loads(cj.read_text()); st=parser.get_structure(name,str(cif)); chains={c.id:c for c in st[0]}
 if not all(x in chains for x in ('A','B')): continue
 rec,rca=ca_coords(chains['A']); bind,bca=ca_coords(chains['B'])
 if len(rec)+len(bind)!=np.load(pae_path)['pae'].shape[0]: continue
 pae=np.load(pae_path)['pae']; dist=np.linalg.norm(rca[:,None,:]-bca[None,:,:],axis=2); ci,cjidx=np.where(dist<10.0)
 ipae=float(np.median((pae[ci,len(rec)+cjidx]+pae[len(rec)+cjidx,ci])/2)) if len(ci) else 99.
 pair=conf.get('pair_chains_iptm',{}); iptm=float(pair.get('0',{}).get('1',conf['iptm']))
 # B-factors carry per-residue pLDDT in Boltz CIF.
 bplddt=float(np.mean([a.bfactor for r in bind for a in r if a.name=='CA']))
 # One-sided buried area: SASA(receptor)+SASA(binder)-SASA(complex), divided by two.
 c_area=sasa(st)
 a_only=parser.get_structure('a',str(cif));
 for c in list(a_only[0]):
  if c.id!='A':a_only[0].detach_child(c.id)
 a_area=sasa(a_only)
 b_only=parser.get_structure('b',str(cif));
 for c in list(b_only[0]):
  if c.id!='B':b_only[0].detach_child(c.id)
 b_area=sasa(b_only); bsa=(a_area+b_area-c_area)/2
 # Target-align predicted chain A to design target chain A; evaluate binder backbone retention.
 design=pp.get_structure('d',str(back/f"{info['backbone']}.pdb")); dc={c.id:c for c in design[0]}
 dr,drca=ca_coords(dc['A']); n=min(len(rec),len(dr)); sup=Superimposer();sup.set_atoms([dr[i]['CA'] for i in range(n)],[rec[i]['CA'] for i in range(n)]);sup.apply(list(st.get_atoms()))
 pred_b,_=ca_coords(chains['B']); des_b,_=ca_coords(dc['B']); rms=float(np.sqrt(np.mean(np.sum((np.array([pred_b[i]['CA'].coord for i in range(min(len(pred_b),len(des_b)))])-np.array([des_b[i]['CA'].coord for i in range(min(len(pred_b),len(des_b)))]))**2,axis=1)))) if len(pred_b)==len(des_b) else 99.
 rows.append({**info,'iptm':iptm,'interface_pae_8A_median':ipae,'binder_plddt':bplddt,'interface_ca_pairs_lt10A':len(ci),'bsa_half_A2':bsa,'binder_pose_rmsd_A':rms,'pass_core':iptm>=.70 and ipae<=10 and bplddt>=85 and bsa>=500 and rms<=2.5})
rows.sort(key=lambda r:(not r['pass_core'],-r['iptm'],r['interface_pae_8A_median']))
out=R/'work/human_boltz_metrics.csv'
if rows:
 with out.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('scored',len(rows),'pass_core',sum(r['pass_core'] for r in rows))
for x in rows[:10]:print(x['candidate_id'],round(x['iptm'],3),round(x['interface_pae_8A_median'],2),round(x['binder_plddt'],1),round(x['bsa_half_A2']),round(x['binder_pose_rmsd_A'],2),x['pass_core'])
(R/'status.json').write_text(json.dumps({'stage':'boltz_human_round1_scored','structures_scored':len(rows),'pass_core':sum(r['pass_core'] for r in rows)},indent=2))
