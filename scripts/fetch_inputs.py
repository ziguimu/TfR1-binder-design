from pathlib import Path
from urllib.request import urlopen, Request
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
urls={"human.fasta":"https://rest.uniprot.org/uniprotkb/P02786.fasta","mouse.fasta":"https://rest.uniprot.org/uniprotkb/Q62351.fasta","11QC.pdb":"https://files.rcsb.org/download/11QC.pdb","3S9L.pdb":"https://files.rcsb.org/download/3S9L.pdb"}
meta={}
for name,url in urls.items():
    p=ROOT/'inputs'/name
    if not p.exists():
        with urlopen(Request(url,headers={'User-Agent':'TfR1-research-input-preparation/1.0'}),timeout=90) as r: data=r.read()
        assert len(data)>100, (name,len(data))
        p.write_bytes(data)
    data=p.read_bytes();meta[name]={'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    print(name,len(data),flush=True)
(ROOT/'inputs'/'sources.json').write_text(json.dumps(meta,indent=2))
print('FETCH COMPLETE',flush=True)
