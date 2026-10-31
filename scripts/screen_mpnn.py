from pathlib import Path
from Bio import SeqIO
import csv,re,json,datetime
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); root=R/'work/proteinmpnn'
rows=[]; seen=set()
for fa in sorted(root.glob('patch*/seqs/*.fa')):
 backbone=fa.stem
 for rec in SeqIO.parse(fa,'fasta'):
  head=rec.description; seq=str(rec.seq).upper()
  if not head.startswith('T='): continue
  if seq in seen: continue
  seen.add(seq)
  def val(k):
   m=re.search(rf'{k}=([0-9.]+)',head); return float(m.group(1)) if m else None
  run=max((len(m.group(0)) for m in re.finditer(r'(.)\1*',seq)),default=0)
  hydro=sum(x in 'AILMFWVY' for x in seq)/len(seq)
  alanine=seq.count('A')/len(seq)
  distinct=len(set(seq))
  flags=[]
  if not 60<=len(seq)<=100: flags.append('length')
  if run>5: flags.append('homopolymer')
  if hydro>0.65: flags.append('hydrophobic')
  if alanine>0.45: flags.append('alanine_rich')
  if distinct<12: flags.append('low_diversity')
  rows.append({'backbone':backbone,'sequence':seq,'length':len(seq),'temp':re.search(r'T=([0-9.]+)',head).group(1),'score':val('score'),'global_score':val('global_score'),'hydrophobic_fraction':round(hydro,4),'alanine_fraction':round(alanine,4),'distinct_AA':distinct,'max_run':run,'his_count':seq.count('H'),'flags':';'.join(flags),'status':'rejected' if flags else 'eligible'})
elig=[r for r in rows if r['status']=='eligible']
# lower ProteinMPNN scores rank first; cycle across backbones to retain structural diversity
for r in elig:r['_rank']=(r['score'] or 9)+(r['global_score'] or 9)*.1
by={}
for r in sorted(elig,key=lambda x:x['_rank']):by.setdefault(r['backbone'],[]).append(r)
selected=[]
for depth in range(2):
 for b in sorted(by,key=lambda b:by[b][0]['_rank']):
  if len(by[b])>depth:selected.append(by[b][depth])
selected=selected[:96]
(R/'work/candidate_pool.csv').parent.mkdir(parents=True,exist_ok=True)
with (R/'work/candidate_pool.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=[k for k in rows[0] if k!='_rank']);w.writeheader();w.writerows([{k:v for k,v in r.items() if k!='_rank'} for r in rows])
with (R/'work/human_shortlist.fasta').open('w') as f:
 for i,r in enumerate(selected,1):
  r['candidate_id']=f'TFR1_{i:03d}'
  f.write(f">{r['candidate_id']}|{r['backbone']}|temp={r['temp']}|mpnn={r['score']:.4f}|H={r['his_count']}\n{r['sequence']}\n")
with (R/'work/human_shortlist.csv').open('w',newline='') as f:
 keys=['candidate_id','backbone','sequence','length','temp','score','global_score','hydrophobic_fraction','alanine_fraction','distinct_AA','max_run','his_count','flags']
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows([{k:r.get(k) for k in keys} for r in selected])
(R/'status.json').write_text(json.dumps({'stage':'sequence_shortlist_complete','designed_sequences':len(rows),'eligible_sequences':len(elig),'human_shortlist':len(selected),'updated_local':datetime.datetime.now().astimezone().isoformat()},indent=2))
print(f'parsed={len(rows)} unique; eligible={len(elig)}; shortlisted={len(selected)}')
print('backbones represented',len(set(r['backbone'] for r in selected)))
print('top3',[(r['candidate_id'],r['length'],r['score'],r['global_score'],r['his_count']) for r in selected[:3]])
