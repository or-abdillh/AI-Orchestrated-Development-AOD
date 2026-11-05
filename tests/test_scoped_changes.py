"""Execution-contract simulations, not claims of end-to-end agent performance."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'.agents/skills/aod-orchestrator'
spec=importlib.util.spec_from_file_location('scoped_workflow',BASE/'scripts/workflow.py')
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)

class ScopedChangeTests(unittest.TestCase):
 def setUp(self):
  self.r=w.registry()
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.project=Path(self.tmp.name)
  self.plan={'id':'serial','scope':'Add serial field; unique per equipment; no architecture change',
   'document_changes':[{'path':'docs/business/DATA_DICTIONARY.md','section':'Equipment.serial','reason':'new optional field','timing':'before-code'}],
   'implementation':['migration, validation and existing equipment form'],
   'verification':['field persistence and authorization regression tests']}
  self.state=w.change_baseline(self.r,self.project,self.plan,'Setuju, implementasikan','changes/serial.json')
  self.r=w.effective_registry(self.state,self.r)
 def stage(self,name):return next(s for s in self.r['steps'] if s['id']=='cr:serial:'+name)
 def finish(self,name):
  d=self.stage(name);w.transition(self.state,d,'Ready');w.transition(self.state,d,'In Progress')
  self.state['steps'][d['id']]['evidence']=['fixture: '+name+' checked against accepted plan']
  w.transition(self.state,d,'Completed')
 def test_one_authorization_crosses_all_change_stages(self):
  for name in ['contracts','implementation','verification','documentation']:
   self.assertEqual(w.candidates(self.state,self.r),[self.stage(name)['id']])
   self.finish(name)
  self.assertTrue(w.close_phase(self.state,self.r))
  self.assertEqual(len(self.state['approvals']),1)
  self.assertFalse(any(self.state['steps'][s['id']]['approved'] for s in self.state['dynamic_steps']))
  self.assertEqual(self.state['steps']['prd']['status'],'Pending')
 def test_no_new_authorization_for_clear_apply_directive(self):
  s=w.change_baseline(w.registry(),self.project,self.plan,'Tambahkan field serial sesuai rencana ini','s.json')
  self.assertTrue(w.candidates(s,w.effective_registry(s,w.registry())))
 def test_empty_authorization_and_mutated_scope_rejected(self):
  with self.assertRaises(ValueError):w.change_baseline(w.registry(),self.project,self.plan,'','s.json')
  self.state['change_plan']['implementation'].append('unapproved payment integration')
  self.assertEqual(w.candidates(self.state,self.r),[])
  with self.assertRaises(ValueError):w.validate(self.state,self.r)
 def test_pipeline_cannot_drop_verification_dependency(self):
  self.state['dynamic_steps'][3]['depends_on']=[]
  with self.assertRaises(ValueError):w.validate(self.state,self.r)
 def test_no_implementation_before_contract_and_no_close_before_docs(self):
  with self.assertRaises(ValueError):w.transition(self.state,self.stage('implementation'),'Ready')
  for name in ['contracts','implementation','verification']:self.finish(name)
  self.assertFalse(w.close_phase(self.state,self.r))
 def test_material_decision_blocks_only_affected_and_descendants(self):
  self.state['pending_decisions']=[{'id':'auth','question':'Access scope?','blocks':[self.stage('implementation')['id']]}]
  self.assertEqual(w.candidates(self.state,self.r),[self.stage('contracts')['id']])
  self.finish('contracts');self.assertEqual(w.candidates(self.state,self.r),[])
  self.assertFalse(w.close_phase(self.state,self.r))
 def test_missing_decision_dependency_is_not_implicitly_approved(self):
  self.finish('contracts');d=self.stage('implementation');d['decision_dependencies']=['route-mode']
  self.assertEqual(w.candidates(self.state,self.r),[])
  self.state['decisions']['route-mode']={'approved':True,'evidence':'prior explicit scope decision'}
  self.assertEqual(w.candidates(self.state,self.r),[d['id']])
 def test_pause_and_opt_in_step_mode(self):
  self.state['paused']=True;self.assertEqual(w.candidates(self.state,self.r),[])
  self.state['paused']=False;self.state['mode']='step';self.finish('contracts')
  self.assertEqual(w.candidates(self.state,self.r),[])
  w.continue_step(self.state)
  self.assertEqual(w.candidates(self.state,self.r),[self.stage('implementation')['id']])
 def test_editorial_change_preserves_history_and_does_not_fan_out(self):
  p=self.project/'PRD.md';p.write_text('Original approved requirement')
  key=self.stage('contracts')['id'];u=self.state['steps'][key]
  u['sources']={'PRD.md':w.fingerprint(p)}
  self.finish('contracts');self.finish('implementation')
  p.write_text('Original approved requirement\nLast Updated: new date')
  changed=w.reconcile(self.state)
  self.assertEqual(changed,{key})
  self.assertEqual(self.state['steps'][self.stage('implementation')['id']]['status'],'Completed')
  self.assertEqual(w.candidates(self.state,self.r),[])
  w.resolve_source_change(self.state,key,'editorial',['reviewed diff: timestamp only'],self.r)
  self.assertEqual(u['status'],'Completed')
  self.assertEqual(len(self.state['approvals']),1)
  self.assertEqual(w.candidates(self.state,self.r),[self.stage('verification')['id']])
 def test_contract_change_revalidates_change_not_baseline(self):
  p=self.project/'contract.md';p.write_text('old')
  key=self.stage('contracts')['id'];self.state['steps'][key]['sources']={'contract.md':w.fingerprint(p)}
  self.finish('contracts');self.finish('implementation');p.write_text('changed behavior')
  w.reconcile(self.state)
  affected=w.resolve_source_change(self.state,key,'contract',['actual contract delta'],self.r)
  self.assertIn(self.stage('implementation')['id'],affected)
  self.assertNotIn('prd',affected)
  self.assertEqual(self.state['steps'][self.stage('implementation')['id']]['status'],'Needs Revalidation')
 def test_missing_source_cannot_be_editorial(self):
  key=self.stage('contracts')['id'];self.state['steps'][key]['sources']={'missing':'old'}
  with self.assertRaises(ValueError):w.resolve_source_change(self.state,key,'editorial',['not enough'],self.r)
 def test_resume_preserves_authorization_without_phase_replay(self):
  self.finish('contracts');p=self.project/'change.json'
  saved=w.save(p,self.state,self.r,-1)
  loaded=json.loads(p.read_text());w.validate(loaded,w.effective_registry(loaded,w.registry()))
  self.assertEqual(w.candidates(loaded,self.r),[self.stage('implementation')['id']])
  self.assertEqual(saved['authorization'],loaded['authorization'])
 def test_readiness_respects_review_policy(self):
  self.state['steps']['existing'].update(status='Completed',evidence=['read-only screening'],approved=False)
  d={'depends_on':['existing'],'decision_dependencies':[]}
  self.assertTrue(w.ready(self.state,d))
  self.state['steps']['prd'].update(status='Completed',evidence=['draft'],approved=False)
  self.assertFalse(w.ready(self.state,{'depends_on':['prd'],'decision_dependencies':[]}))
 def test_six_change_scenarios_do_not_select_bootstrap_steps(self):
  for case,docs in [('bug',[]),('field',['DATA_DICTIONARY']),('page',['UI_FLOW']),('permission',['RBAC']),('module',['PRD','API_CONTRACT']),('architecture',['TECH_SPEC'])]:
   with self.subTest(case=case):
    p=copy.deepcopy(self.plan);p['id']=case;p['scope']=case
    p['document_changes']=[{'path':x+'.md','section':'affected section','reason':case,'timing':'before-code'} for x in docs]
    s=w.change_baseline(w.registry(),self.project,p,'Approved described scope','case.json')
    effective=w.effective_registry(s,w.registry())
    self.assertEqual(w.candidates(s,effective),['cr:'+case+':contracts'])
    self.assertEqual(len(s['approvals']),1)
 def test_cli_does_not_overwrite_baseline(self):
  state=self.project/'WORKFLOW_STATE.json';state.write_text('existing baseline')
  plan=self.project/'plan.json';plan.write_text(json.dumps(self.plan))
  result=subprocess.run(['python3',str(BASE/'scripts/workflow.py'),'init-change','--plan',str(plan),'--response','approved','--state',str(state)],capture_output=True,text=True)
  self.assertNotEqual(result.returncode,0);self.assertEqual(state.read_text(),'existing baseline')
 def test_cli_init_and_inspect_do_not_need_guided_phase_authorization(self):
  state=self.project/'changes/new.json';plan=self.project/'plan.json';plan.write_text(json.dumps(self.plan))
  command=['python3',str(BASE/'scripts/workflow.py')]
  result=subprocess.run(command+['init-change','--plan',str(plan),'--response','Setuju implementasi scope ini','--state',str(state),'--project',str(self.project)],check=True,capture_output=True,text=True)
  created=json.loads(result.stdout);self.assertEqual(created['profile'],'change')
  before=state.read_bytes()
  result=subprocess.run(command+['inspect','--state',str(state)],check=True,capture_output=True,text=True)
  self.assertEqual(json.loads(result.stdout)['ready'],['cr:serial:contracts'])
  self.assertEqual(state.read_bytes(),before)
 def test_installer_preserves_change_state_and_ships_protocol(self):
  target=self.project/'target';p=target/'docs/aod/changes/serial.json'
  p.parent.mkdir(parents=True);p.write_text('active change')
  for _ in range(2):subprocess.run(['bash',str(ROOT/'install.sh'),str(target)],check=True,capture_output=True)
  self.assertEqual(p.read_text(),'active change')
  self.assertTrue((target/'.agents/skills/aod-orchestrator/references/change-workflow.md').exists())
  self.assertIn('One accepted plan',(target/'CLAUDE.md').read_text())

if __name__=='__main__':unittest.main()
