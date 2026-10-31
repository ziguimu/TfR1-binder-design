from pathlib import Path
import json,subprocess,os,time,datetime,sys
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); M=json.loads((R/'inputs/target_metadata.json').read_text())
RF='/home/ziguimu/RFdiffusion/env/RFdiffusion-main'; PY='/home/ziguimu/miniconda3/envs/rfdiff/bin/python'
(R/'work/backbones').mkdir(parents=True,exist_ok=True); (R/'logs/rfdiff_batches').mkdir(parents=True,exist_ok=True)
env=os.environ.copy();env['PYTHONPATH']=RF;env['TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD']='1';env['OMP_NUM_THREADS']='4';env['OPENBLAS_NUM_THREADS']='1'
status=R/'status.json'
def write_status(stage,done,total,job=None):
 status.write_text(json.dumps({'stage':stage,'completed':done,'total':total,'current_job':job,'updated_local':datetime.datetime.now().astimezone().isoformat(),'project_root':str(R)},indent=2))
jobs=[]
for p in M['patches']:
 for length in ('60-80','80-100'):
  jobs.append((p,length))
# 16 structures in each of four target-patch/length strata = 64 initial backbones.
for idx,(p,length) in enumerate(jobs):
 name=f"{p['name']}_{length.replace('-','_')}"
 out=R/'work/backbones'/name
 existing=list(out.parent.glob(name+'_*.pdb'))
 if len(existing)>=16: continue
 cmd=[PY,RF+'/scripts/run_inference.py',f'inference.input_pdb={R}/inputs/human_apical.pdb',f'inference.output_prefix={out}',f'inference.model_directory_path={RF}/models','inference.num_designs=16','inference.design_startnum=0','inference.deterministic=True','inference.write_trajectory=False',f'contigmap.contigs=[A189-383/0 {length}]',f"ppi.hotspot_res=[{','.join('A'+str(i) for i in p['hotspots'])}]",'denoiser.noise_scale_ca=0','denoiser.noise_scale_frame=0',f'hydra.run.dir={R}/logs/rfdiff_batches/{name}']
 write_status('rfdiffusion_batch1',idx,4,name)
 logfile=R/'logs/rfdiff_batches'/f'{name}.log'
 with logfile.open('w') as f: result=subprocess.run(cmd,cwd=R,env=env,stdout=f,stderr=subprocess.STDOUT)
 count=len(list(out.parent.glob(name+'_*.pdb')))
 with (R/'progress.md').open('a') as f: f.write(f"\n{datetime.datetime.now().astimezone().isoformat()} {name}: exit={result.returncode}, structures={count}/16\n")
 if result.returncode or count<16:
  write_status('rfdiffusion_batch1_failed',idx+1,4,name);sys.exit(2)
write_status('rfdiffusion_batch1_complete',4,4)
