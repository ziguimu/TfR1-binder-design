from pathlib import Path
import json,csv
import numpy as np
from Bio import SeqIO,Align
from Bio.PDB import PDBParser,PDBIO,Select,Superimposer,ShrakeRupley
from Bio.SeqUtils import seq1
ROOT=Path(__file__).resolve().parents[1]; IN=ROOT/'inputs'
h=str(SeqIO.read(IN/'human.fasta','fasta').seq);m=str(SeqIO.read(IN/'mouse.fasta','fasta').seq)
assert len(h)==760 and len(m)==763
p=PDBParser(QUIET=True); ref=p.get_structure('ref',IN/'11QC.pdb'); tf=p.get_structure('tf',IN/'3S9L.pdb')
common=sorted(set(r.id[1] for r in ref[0]['A'] if r.id[0]==' ' and 'CA' in r)&set(r.id[1] for r in tf[0]['A'] if r.id[0]==' ' and 'CA' in r))
sup=Superimposer();sup.set_atoms([ref[0]['A'][i]['CA'] for i in common],[tf[0]['A'][i]['CA'] for i in common]);sup.apply(list(tf.get_atoms()))
# Full ligand complex retained for downstream steric audits.
io=PDBIO();io.set_structure(tf);io.save(str(IN/'transferrin_aligned.pdb'))
class Crop(Select):
    def accept_chain(self,c):return c.id=='A'
    def accept_residue(self,r):return r.id[0]==' ' and 189<=r.id[1]<=383
io.set_structure(ref);io.save(str(IN/'human_apical.pdb'),Crop())
res=[r for r in ref[0]['A'] if r.id[0]==' ' and 189<=r.id[1]<=383]
assert [r.id[1] for r in res]==list(range(189,384))
assert ''.join(seq1(r.resname) for r in res)==h[188:383]
# Align with affine gaps and retain explicit 1-based UniProt mapping.
a=Align.PairwiseAligner();a.mode='global';a.match_score=2;a.mismatch_score=-1;a.open_gap_score=-10;a.extend_gap_score=-.5
al=a.align(h,m)[0];hm={int(i)+1:int(j)+1 for i,j in zip(*al.indices) if i>=0 and j>=0}
ms,me=hm[189],hm[383]
ShrakeRupley(n_points=100).compute(ref,level='R')
def xyz(atoms):return np.array([x.coord for x in atoms if x.element not in ('H','D')])
partner=xyz(ref[0]['B'].get_atoms());gly=xyz([x for x in ref.get_atoms() if x.parent.id[0].startswith('H_')]);lig=xyz([x for c in tf[0] if c.id in ('C','D') for x in c.get_atoms()])
def mind(x,y):return float(np.linalg.norm(x[:,None,:]-y[None,:,:],axis=-1).min()) if len(y) else 999.
rows=[]
for r in res:
    sc=xyz([x for x in r if x.name not in ('N','CA','C','O')])
    if not len(sc):sc=xyz(r.get_atoms())
    i=r.id[1];dp=mind(sc,partner);dg=mind(sc,gly);dt=mind(sc,lig)
    # Avoid observed glycans and all N-X-S/T sequons, not just resolved sugar atoms.
    seqsites=[j+1 for j in range(len(h)-2) if h[j]=='N' and h[j+1]!='P' and h[j+2] in 'ST']
    dn=min((float(np.linalg.norm(r['CA'].coord-ref[0]['A'][j]['CA'].coord)) for j in seqsites if (' ',j,' ') in ref[0]['A']),default=999)
    conserved=i in hm and h[i-1]==m[hm[i]-1]
    eligible=r.sasa>=35 and dp>=10 and dg>=10 and dt>=12 and dn>=10 and 195<=i<=377
    score=min(r.sasa,150)/50+int(conserved)+int(seq1(r.resname) in 'FWYILVM')
    rows.append(dict(residue=i,aa=seq1(r.resname),sasa=float(r.sasa),dimer_min=dp,glycan_min=dg,transferrin_min=dt,sequon_CA_min=dn,conserved=conserved,eligible=eligible,score=score))
ranked=sorted([r for r in rows if r['eligible']],key=lambda r:r['score'],reverse=True)
patches=[]
for rr in ranked:
    center=ref[0]['A'][rr['residue']]['CA'].coord
    if any(np.linalg.norm(center-ref[0]['A'][p['center']]['CA'].coord)<18 for p in patches):continue
    near=[r for r in ranked if r['residue']!=rr['residue'] and np.linalg.norm(center-ref[0]['A'][r['residue']]['CA'].coord)<=9]
    if not near:continue
    hotspots=[rr['residue'],near[0]['residue']]
    patches.append({'name':f'patch{len(patches)+1}','center':rr['residue'],'hotspots':hotspots})
    if len(patches)==2:break
assert len(patches)==2,ranked
with (IN/'surface_audit.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
meta={'human_accession':'P02786','mouse_accession':'Q62351','human_crop_start':189,'human_crop_end':383,'human_crop_sequence':h[188:383],'mouse_crop_start':ms,'mouse_crop_end':me,'mouse_crop_sequence':m[ms-1:me],'human_ectodomain':h[120:],'mouse_ectodomain':m[122:],'human_to_mouse':hm,'patches':patches,'transferrin_alignment_rmsd':float(sup.rms)}
(IN/'target_metadata.json').write_text(json.dumps(meta,indent=2));print(json.dumps({k:v for k,v in meta.items() if k in ['patches','transferrin_alignment_rmsd','mouse_crop_start','mouse_crop_end']},indent=2))
