from pathlib import Path
import json,numpy as np
from Bio.PDB import PDBParser,Superimposer
from Bio.SeqUtils import seq1
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028')
P=R/'research/route_v2'
p=PDBParser(QUIET=True)
ref=p.get_structure('ref',R/'inputs/11QC.pdb')[0]
known=p.get_structure('known',P/'6WRV.pdb')[0]
tf=p.get_structure('tf',R/'inputs/transferrin_aligned.pdb')[0]
def atoms(c):return [a for a in c.get_atoms() if a.parent.id[0]==' ' and a.element not in ('H','D')]
def xyz(aa):return np.array([a.coord for a in aa])
def pairdist(a,b):return np.linalg.norm(a[:,None,:]-b[None,:,:],axis=-1)
rec=[c for c in known if sum(r.id[0]==' ' for r in c)>500]
bin=[c for c in known if 40<sum(r.id[0]==' ' for r in c)<200]
pairs=[]
for a in rec:
 for b in bin:
  d=pairdist(xyz(atoms(a)),xyz(atoms(b)))
  pairs.append(dict(receptor=a.id,binder=b.id,heavy_pairs_lt4p5=int((d<4.5).sum())))
best=max([v for v in pairs if v['receptor']=='A'],key=lambda v:v['heavy_pairs_lt4p5'])
a=known[best['receptor']];b=known[best['binder']]
ars=atoms(a);bs=atoms(b);d=pairdist(xyz(ars),xyz(bs))
foot=sorted(set((ars[i].parent.id[1],seq1(ars[i].parent.resname)) for i in np.where(d.min(1)<4.5)[0]))
common=[i for i in range(189,384) if (' ',i,' ') in a and (' ',i,' ') in ref['A']]
su=Superimposer();su.set_atoms([ref['A'][i]['CA'] for i in common],[a[i]['CA'] for i in common]);su.apply(list(known.get_atoms()))
bxyz=xyz(atoms(b))
out={'structure':'6WRV','pair_candidates':pairs,'selected_pair':best,'apical_alignment_rmsd_A':float(su.rms),'contact_residues_4p5A':foot,'old_hotspots':[],'rigid_overlay_transferrin':[]}
for i in [244,247,303,327,211]:
 r=ref['A'][i];dist=pairdist(xyz(atoms(r)),bxyz)
 out['old_hotspots'].append({'residue':i,'aa':seq1(r.resname),'min_distance_to_3DS18_A':float(dist.min()),'CA_distance_to_Y211_A':float(np.linalg.norm(r['CA'].coord-ref['A'][211]['CA'].coord))})
for c in ['C','D']:
 dist=pairdist(bxyz,xyz(atoms(tf[c])))
 out['rigid_overlay_transferrin'].append({'chain':c,'min_distance_A':float(dist.min()),'atom_pairs_lt2A':int((dist<2).sum()),'atom_pairs_lt4A':int((dist<4).sum())})
(P/'epitope_audit.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

