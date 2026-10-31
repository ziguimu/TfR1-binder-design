from pathlib import Path
import csv,json,subprocess,datetime,sys
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); rows=list(csv.DictReader((R/'work/human_shortlist.csv').open()))
exe='/home/ziguimu/miniconda3/envs/boltz/bin/boltz'; yaml_dir=R/'inputs/boltz_round1'; out=R/'work/boltz_human_round1'; out.mkdir(exist_ok=True); logs=R/'logs/boltz_human_round1';logs.mkdir(exist_ok=True)
for i,r in enumerate(rows):
 name=r['candidate_id']; y=yaml_dir/f'{name}.yaml'; dst=out/name
 conf=list(dst.glob(f'boltz_results_{name}/predictions/{name}/confidence_{name}_model_0.json'))
 if conf: continue
 status={'stage':'boltz_human_round1','completed':i,'total':len(rows),'current_candidate':name,'updated_local':datetime.datetime.now().astimezone().isoformat()};(R/'status.json').write_text(json.dumps(status,indent=2))
 cmd=[exe,'predict',str(y),'--out_dir',str(dst),'--model','boltz2','--max_parallel_samples','1','--diffusion_samples','1','--accelerator','gpu','--devices','1']
 with (logs/f'{name}.log').open('w') as f: rc=subprocess.run(cmd,cwd=R,stdout=f,stderr=subprocess.STDOUT)
 log=(logs/f'{name}.log').read_text(errors='replace')
 if rc.returncode or 'Number of failed examples: 0' not in log:
  with (R/'progress.md').open('a') as f:f.write(f"\n{datetime.datetime.now().astimezone().isoformat()} Boltz failed {name}: rc={rc.returncode}\n")
  continue
 with (R/'progress.md').open('a') as f:f.write(f"\n{datetime.datetime.now().astimezone().isoformat()} Boltz human {name}: complete\n")
(R/'status.json').write_text(json.dumps({'stage':'boltz_human_round1_complete','completed':len(rows),'total':len(rows),'updated_local':datetime.datetime.now().astimezone().isoformat()},indent=2))
