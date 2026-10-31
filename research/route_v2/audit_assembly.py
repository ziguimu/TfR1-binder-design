from pathlib import Path
P=Path('/mnt/d/PRP/TfR1_challenge4_20261028/research/route_v2')
exec((P/'audit_epitopes.py').read_text(encoding='utf-8-sig').split("print(json.dumps(out")[0])
orig=p.get_structure('orig',R/'inputs/3S9L.pdb')[0]
common2=sorted(set(r.id[1] for r in orig['A'] if r.id[0]==' ' and 'CA' in r)&set(r.id[1] for r in ref['A'] if r.id[0]==' ' and 'CA' in r))
s2=Superimposer();s2.set_atoms([ref['A'][i]['CA'] for i in common2],[orig['A'][i]['CA'] for i in common2])
rot,tran=s2.rotran
symrot=np.diag([-1.,1.,-1.]);symtran=np.array([231.676,0.,0.])
c0=xyz(atoms(orig['C'])); c1=c0@symrot+symtran
correct=[c0@rot+tran,c1@rot+tran]
audit={'assembly':'3S9L biological assembly 1, chains A,C plus BIOMT operator 2','reference_alignment_rmsd_A':float(s2.rms),'Y211_transferrin_distances_A':[float(pairdist(xyz(atoms(ref['A'][211])),c).min()) for c in correct],'3DS18_transferrin_overlay':[],'recommended_CA_distances':[],'corrected_transferrin_residue_distances':[]}
for j,c in enumerate(correct):
 d=pairdist(bxyz,c)
 audit['3DS18_transferrin_overlay'].append({'copy':j,'min_distance_A':float(d.min()),'atom_pairs_lt2A':int((d<2).sum())})
for n in [204,209,210,211,212,215,348,371]:
 audit['recommended_CA_distances'].append({'residue':n,'to_Y211_A':float(np.linalg.norm(ref['A'][n]['CA'].coord-ref['A'][211]['CA'].coord))})
for n in range(189,384):
 r=ref['A'][n];sc=[a for a in atoms(r) if a.name not in ('N','CA','C','O')] or atoms(r)
 audit['corrected_transferrin_residue_distances'].append({'residue':n,'min_distance_A':min(float(pairdist(xyz(sc),c).min()) for c in correct)})
(P/'corrected_assembly_audit.json').write_text(json.dumps(audit,indent=2))
print(json.dumps({k:v for k,v in audit.items() if k!='corrected_transferrin_residue_distances'},indent=2))

