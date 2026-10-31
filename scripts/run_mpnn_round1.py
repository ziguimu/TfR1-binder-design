from pathlib import Path
import json,subprocess,os,datetime,sys
R=Path('/mnt/d/PRP/TfR1_challenge4_20261028'); MP='/home/ziguimu/ProteinMPNN'; PY='/home/ziguimu/miniconda3/envs/proteinmpnn/bin/python'
env=os.environ.copy();env['OMP_NUM_THREADS']='2';env['OPENBLAS_NUM_THREADS']='1'
files=sorted(list((R/'work/backbones').glob('patch1_60_80_*.pdb'))+list((R/'work/backbones').glob('patch1_80_100_*.pdb'))+list((R/'work/backbones').glob('patch2_60_80_*.pdb'))+list((R/'work/backbones').glob('patch2_80_100_*.pdb'))); assert len(files)==64,len(files)
out=R/'work/proteinmpnn';out.mkdir(parents=True,exist_ok=True);(R/'logs/mpnn').mkdir(exist_ok=True)
for i,pdb in enumerate(files):
 name=pdb.stem; dest=out/name
 fa=dest/'seqs'/f'{name}.fa'
 if fa.exists() and fa.stat().st_size>100: continue
 dest.mkdir(parents=True,exist_ok=True)
 st={'stage':'proteinmpnn_round1','completed':i,'total':64,'current_job':name,'updated_local':datetime.datetime.now().astimezone().isoformat(),'project_root':str(R)};(R/'status.json').write_text(json.dumps(st,indent=2))
 cmd=[PY,MP+'/protein_mpnn_run.py','--path_to_model_weights',MP+'/vanilla_model_weights','--model_name','v_48_020','--pdb_path',str(pdb),'--pdb_path_chains','B','--out_folder',str(dest),'--num_seq_per_target','8','--sampling_temp','0.1 0.2','--batch_size','8','--seed',str(1000+i),'--save_score','1','--save_probs','0','--suppress_print','1']
 with (R/'logs/mpnn'/f'{name}.log').open('w') as f:r=subprocess.run(cmd,cwd=R,env=env,stdout=f,stderr=subprocess.STDOUT)
 if r.returncode or not fa.exists():
  (R/'status.json').write_text(json.dumps({'stage':'proteinmpnn_failed','completed':i,'total':64,'current_job':name,'exit':r.returncode},indent=2));sys.exit(2)
 with (R/'progress.md').open('a') as f:f.write(f"\n{datetime.datetime.now().astimezone().isoformat()} ProteinMPNN {name}: 16 sequences\n")
(R/'status.json').write_text(json.dumps({'stage':'proteinmpnn_round1_complete','completed':64,'total':64,'updated_local':datetime.datetime.now().astimezone().isoformat()},indent=2))

