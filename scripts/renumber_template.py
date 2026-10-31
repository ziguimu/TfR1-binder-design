from Bio.PDB import PDBParser,PDBIO
from Bio.SeqUtils import seq3
from pathlib import Path
import json
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); seq=json.loads((R/'inputs/target_metadata.json').read_text())['human_crop_sequence']
s=PDBParser(QUIET=True).get_structure('x',str(R/'inputs/human_apical.pdb'));ch=s[0]['A']
for i,r in enumerate(list(ch),1):r.id=(' ',i,' ')
out=R/'inputs/human_apical_renumbered.pdb'; tmp=R/'work/template_tmp.pdb';io=PDBIO();io.set_structure(s);io.save(str(tmp))
aas=[seq3(x).upper() for x in seq]; headers=[]
for start in range(0,len(aas),13):headers.append(f'SEQRES {start//13+1:3d} A {len(aas):4d}  '+ ' '.join(aas[start:start+13])+'\n')
out.write_text(''.join(headers)+tmp.read_text());print('sequence',len(seq),'seqres',sum(len(x.split())-4 for x in headers))
