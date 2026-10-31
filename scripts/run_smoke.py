from pathlib import Path
import json,subprocess,os,datetime
R=Path(__file__).resolve().parents[1]
meta=json.loads((R/'inputs/target_metadata.json').read_text())
out=R/'work/backbones';out.mkdir(exist_ok=True)
rf='/home/ziguimu/RFdiffusion/env/RFdiffusion-main'
hs=','.join('A'+str(i) for i in meta['patches'][0]['hotspots'])
cmd=['/home/ziguimu/miniconda3/envs/rfdiff/bin/python',rf+'/scripts/run_inference.py',f'inference.input_pdb={R}/inputs/human_apical.pdb',f'inference.output_prefix={out}/patch1_short',f'inference.model_directory_path={rf}/models','inference.num_designs=1','inference.design_startnum=0','inference.deterministic=True','inference.write_trajectory=False','contigmap.contigs=[A189-383/0 60-80]',f'ppi.hotspot_res=[{hs}]','denoiser.noise_scale_ca=0','denoiser.noise_scale_frame=0',f'hydra.run.dir={R}/logs/rfdiff_smoke_hydra']
env=os.environ.copy();env['PYTHONPATH']=rf;env['TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD']='1';env['OMP_NUM_THREADS']='4'
(R/'logs/smoke_command.json').write_text(json.dumps(cmd,indent=2))
(R/'status.json').write_text(json.dumps({'stage':'rfdiffusion_smoke','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'project_root':str(R)},indent=2))
with (R/'logs/rfdiff_smoke.log').open('w') as f:
    p=subprocess.run(cmd,cwd=R,env=env,stdout=f,stderr=subprocess.STDOUT)
print('RFdiffusion smoke exit',p.returncode,flush=True)
print((R/'logs/rfdiff_smoke.log').read_text()[-5000:],flush=True)
raise SystemExit(p.returncode)
