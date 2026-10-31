from pathlib import Path
from Bio.SeqUtils import seq3
p=Path('/mnt/d/PRP/TfR1_challenge4_20261028/inputs/human_apical_renumbered.pdb'); seq=''.join(Path('/mnt/d/PRP/TfR1_challenge4_20261028/inputs/target_metadata.json').read_text().split('human_crop_sequence')[1].split('"')[1])
aas=[seq3(x).upper() for x in seq]; lines=[]
for start in range(0,len(aas),13):
 n=start//13+1;chunk=' '.join(aas[start:start+13]);lines.append(f'SEQRES {n:3d} A {len(aas):4d}  {chunk}\n')
body=p.read_text();body=''.join(lines)+body;p.write_text(body);print('SEQRES',len(aas))
