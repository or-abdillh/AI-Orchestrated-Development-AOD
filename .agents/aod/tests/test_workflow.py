import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'.agents/skills/aod-orchestrator'
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
w=module('workflow',BASE/'scripts/workflow.py')
i=module('installer',BASE/'scripts/install_package.py')

class WorkflowTests(unittest.TestCase):
 def setUp(self):
  self.r=w.registry();self.s=w.baseline(self.r,ROOT,'test','state.json');self.s['active_phase']='1'
  self.s['authorization']={'start':True,'phase':'1'}
  self.s['steps']['discovery'].update(status='Completed',approved=True,evidence=['source review'])
 def step(self,key): return next(s for s in self.r['steps'] if s['id']==key)
 def test_no_confirmation_no_execution(self):
  self.s['authorization']={};self.assertEqual(w.candidates(self.s,self.r),[])
  with self.assertRaises(ValueError):w.transition(self.s,self.step('brd'),'In Progress')
 def test_dependency_waves_and_step_stop(self):
  self.assertEqual(w.candidates(self.s,self.r),['brd','flow'])
  w.transition(self.s,self.step('brd'),'Ready');w.transition(self.s,self.step('brd'),'In Progress')
  self.assertEqual(w.candidates(self.s,self.r),[])
  self.s['mode']='phase-parallel';self.assertEqual(w.candidates(self.s,self.r),['flow'])
 def test_draft_not_approved(self):
  u=self.s['steps']['brd'];u.update(status='Awaiting Review',evidence=['draft'])
  with self.assertRaises(ValueError):w.transition(self.s,self.step('brd'),'Completed')
  u['approved']=True;w.transition(self.s,self.step('brd'),'Completed')
 def test_skip_and_phase_gate(self):
  with self.assertRaises(ValueError):w.transition(self.s,self.step('brd'),'Skipped')
  self.assertFalse(w.close_phase(self.s,self.r))
 def test_invalidation_only_affected(self):
  for u in self.s['steps'].values():u.update(status='Completed',approved=True,evidence=['review'])
  affected=w.invalidate(self.s,self.r,{'data'})
  self.assertIn('contract',affected);self.assertNotIn('brd',affected)
  self.assertEqual(self.s['steps']['brd']['status'],'Completed')
 def test_missing_source_revalidates(self):
  self.s['steps']['brd']['sources']={'absent':'hash'}
  self.s['steps']['brd']['status']='Completed'
  self.assertIn('brd',w.reconcile(self.s))
 def test_resume_atomic_conflict_and_corruption(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'state.json';saved=w.save(p,self.s,self.r,-1)
   self.assertEqual(w.validate(json.loads(p.read_text()),self.r),saved)
   with self.assertRaises(ValueError):w.save(p,self.s,self.r,-1)
   before=p.read_bytes()
   with patch.object(w.os,'replace',side_effect=OSError('interrupted')):
    with self.assertRaises(OSError):w.save(p,saved,self.r,0)
   self.assertEqual(p.read_bytes(),before)
   p.write_text('{broken')
   with self.assertRaises(ValueError):w.save(p,saved,self.r,0)
   self.assertEqual(p.read_text(),'{broken')
 def test_schema_and_lock(self):
  self.s['schema_version']=9
  with self.assertRaises(ValueError):w.validate(self.s,self.r)
  self.s['schema_version']=1
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'s.json';p.with_suffix('.json.lock').write_text('active')
   with self.assertRaises(FileExistsError):w.save(p,self.s,self.r,-1)
 def test_dynamic_graph(self):
  item=copy.deepcopy(self.step('brd'));item.update(id='impl:orders',phase='4',depends_on=['tech','plan','dod'])
  self.s['dynamic_steps']=[item];self.assertEqual(w.effective_registry(self.s,self.r)['steps'][-1]['id'],'impl:orders')
  item['depends_on']=['impl:orders']
  with self.assertRaises(ValueError):w.effective_registry(self.s,self.r)
 def test_registry_rejects_duplicate_missing_and_cycle(self):
  for mutate in [lambda r:r['steps'].append(r['steps'][0]),lambda r:r['steps'][0].update(depends_on=['unknown']),lambda r:r['steps'][0].update(depends_on=['prd']),lambda r:r['steps'][0].update(skill='aod-absent')]:
   r=copy.deepcopy(self.r);mutate(r)
   with tempfile.NamedTemporaryFile(mode='w') as f:
    json.dump(r,f);f.flush()
    with self.assertRaises(ValueError):w.registry(f.name)
 def test_saved_draft_cannot_unlock_dependencies(self):
  self.s['steps']['brd'].update(status='Completed',evidence=['draft'],approved=False)
  with self.assertRaises(ValueError):w.validate(self.s,self.r)
 def test_scoped_decision_preserves_independent_work(self):
  self.s['pending_decisions']=[{'id':'route-mode','blocks':['contract']}]
  self.assertEqual(w.candidates(self.s,self.r),['brd','flow'])
 def test_explicit_continue_replenishes_one_unit(self):
  self.s['authorization']['unit_consumed']=True
  w.continue_step(self.s)
  self.assertEqual(w.candidates(self.s,self.r),['brd','flow'])
 def test_as_is_override_requires_evidence_and_preserves_review(self):
  self.s['baseline_overrides']=[{'step_id':'brd','scope':'as-is','depends_on':[], 'evidence':['existing screening'], 'authorization':'selected BRD as-is'}]
  r=w.effective_registry(self.s,self.r)
  self.assertEqual(next(s for s in r['steps'] if s['id']=='brd')['depends_on'],[])
  self.s['baseline_overrides'][0]['evidence']=[]
  with self.assertRaises(ValueError):w.effective_registry(self.s,self.r)
 def test_pause_and_pending_material_decision(self):
  self.s['paused']=True;self.assertEqual(w.candidates(self.s,self.r),[])
  self.s['paused']=False;self.s['pending_decisions']=['route-mode'];self.assertEqual(w.candidates(self.s,self.r),[])

class InstallerTests(unittest.TestCase):
 def test_clean_install_excludes_root_and_maintainer_tooling(self):
  with tempfile.TemporaryDirectory() as tmp:
   t=Path(tmp)
   subprocess.run(['bash',str(ROOT/'install.sh'),'--yes',tmp],check=True,capture_output=True)
   for rel in ['scripts','tests','test','.agents/aod/scripts','.agents/aod/tests']:
    self.assertFalse((t/rel).exists(),rel+' must not be injected')
   runtime=t/'.agents/skills/aod-orchestrator/scripts/workflow.py'
   self.assertTrue(runtime.is_file())
   result=subprocess.run(['python3',str(runtime),'validate-registry'],check=True,capture_output=True,text=True)
   self.assertIn('Registry valid',result.stdout)
 def test_reinstall_preserves_app_tooling_and_legacy_file(self):
  with tempfile.TemporaryDirectory() as tmp:
   t=Path(tmp)
   originals={'scripts/build.sh':b'app build\n','tests/app_test.py':b'app tests\n',
    'test/app.test.js':b'project tests\n','scripts/sync_workflow.py':b'locally modified legacy AOD helper\n',
    '.agents/aod/scripts/custom.py':b'project-owned helper\n'}
   for name,data in originals.items():
    p=t/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
   for _ in range(2):subprocess.run(['bash',str(ROOT/'install.sh'),'--yes',tmp],check=True,capture_output=True)
   for name,data in originals.items():self.assertEqual((t/name).read_bytes(),data,name)
   for folder in ['scripts','tests','test','.agents/aod/scripts']:
    actual={str(p.relative_to(t)) for p in (t/folder).rglob('*') if p.is_file()}
    expected={name for name in originals if name.startswith(folder+'/')}
    self.assertEqual(actual,expected)
 def test_manifest_excludes_maintainer_tooling(self):
  files=json.loads((ROOT/'.agents/aod-package.json').read_text())['files']
  self.assertFalse(any(p.startswith(('scripts/','tests/','test/','.agents/aod/')) and p!='.agents/aod/bin/arc' for p in files))
 def test_markers_preserve_and_reject(self):
  block='<!-- aod:start -->new<!-- aod:end -->'
  self.assertEqual(i.inject('before<!-- aod:start -->old<!-- aod:end -->after',block),'before'+block+'after')
  for text in ['<!-- aod:start -->','<!-- aod:end --><!-- aod:start -->',block+block]:
   with self.assertRaises(ValueError):i.inject(text,block)
 def test_reinstall_preserves_project(self):
  with tempfile.TemporaryDirectory() as tmp:
   t=Path(tmp);(t/'AGENTS.md').write_text('custom before\n')
   for rel,data in [('docs/aod/WORKFLOW_STATE.json','active'),('docs/business/PRD.md','product'),('.agents/rules/aod-architecture-engineering.md','approved architecture'),('.agents/skills/custom/SKILL.md','custom')]:
    p=t/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data)
   for _ in range(2):subprocess.run(['bash',str(ROOT/'install.sh'),tmp],check=True,capture_output=True)
   self.assertTrue((t/'AGENTS.md').read_text().startswith('custom before\n'))
   self.assertEqual((t/'AGENTS.md').read_text().count('<!-- aod:start -->'),1)
   self.assertEqual((t/'docs/aod/WORKFLOW_STATE.json').read_text(),'active')
   self.assertEqual((t/'docs/business/PRD.md').read_text(),'product')
   self.assertEqual((t/'.agents/rules/aod-architecture-engineering.md').read_text(),'approved architecture')
   self.assertEqual((t/'.agents/skills/custom/SKILL.md').read_text(),'custom')
 def test_write_failure_is_reported(self):
  with tempfile.TemporaryDirectory() as tmp:
   with patch.object(i,'atomic',side_effect=OSError('write denied')):
    with self.assertRaises(OSError):i.install(ROOT,tmp)
 def test_missing_runtime_fails(self):
  with tempfile.TemporaryDirectory() as tmp:
   result=subprocess.run(['/bin/bash',str(ROOT/'install.sh'),tmp],env={'PATH':tmp},capture_output=True,text=True)
   self.assertNotEqual(result.returncode,0)
   self.assertIn('Missing dependency: python3',result.stderr)
 def test_malformed_marker_prevents_package_writes(self):
  with tempfile.TemporaryDirectory() as tmp:
   t=Path(tmp);(t/'AGENTS.md').write_text('custom<!-- aod:start -->')
   with self.assertRaises(ValueError):i.install(ROOT,t)
   self.assertFalse((t/'.agents').exists())
   self.assertEqual((t/'AGENTS.md').read_text(),'custom<!-- aod:start -->')
 def test_generated_maps(self):
  subprocess.run(['python3',str(ROOT/'.agents/aod/scripts/sync_workflow.py'),'--check'],check=True)

if __name__=='__main__':unittest.main()
