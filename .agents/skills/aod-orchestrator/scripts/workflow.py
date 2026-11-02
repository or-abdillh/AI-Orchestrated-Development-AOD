"""Deterministic workflow checks; approval evidence is supplied by the developer/agent."""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone

REGISTRY = Path(__file__).resolve().parents[1] / 'references/workflow.json'
STATUSES = {'Pending', 'Ready', 'In Progress', 'Awaiting Review', 'Completed', 'Blocked', 'Needs Revalidation', 'Skipped', 'Failed'}
TRANSITIONS = {
 'Pending': {'Ready', 'Blocked', 'Skipped'}, 'Ready': {'In Progress', 'Blocked', 'Skipped'},
 'In Progress': {'Awaiting Review', 'Completed', 'Blocked', 'Failed'},
 'Awaiting Review': {'Completed', 'In Progress', 'Blocked', 'Needs Revalidation'},
 'Completed': {'Needs Revalidation'}, 'Skipped': {'Needs Revalidation'},
 'Blocked': {'Ready', 'Skipped'}, 'Failed': {'Ready', 'Blocked'},
 'Needs Revalidation': {'Ready', 'Awaiting Review', 'Blocked', 'Completed', 'Skipped'}}

def now():
 return datetime.now(timezone.utc).isoformat()

def fingerprint(path):
 p = Path(path)
 return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None

def registry(path=REGISTRY):
 r = json.loads(Path(path).read_text())
 ids = [s['id'] for s in r['steps']]
 if len(ids) != len(set(ids)):
  raise ValueError('Duplicate step ID')
 nodes = {s['id']: s for s in r['steps']}
 def visit(key, stack):
  if key in stack: raise ValueError('Dependency cycle')
  if key not in nodes: raise ValueError('Missing dependency: '+key)
  for dep in nodes[key]['depends_on']: visit(dep, stack | {key})
 for s in r['steps']:
  visit(s['id'], set())
  if s['skill'] and not (REGISTRY.parents[2] / s['skill'] / 'SKILL.md').is_file():
   raise ValueError('Missing skill: '+s['skill'])
 return r

def baseline(r, project, scope, path):
 return dict(schema_version=1, registry_version=r['version'], workflow_id='aod', scope=scope,
 project_path=str(Path(project).resolve()), checkpoint_path=path, revision=0, updated_at=now(),
 active_phase='0', active_step=None, mode='step', authorization={}, approvals=[], decisions={},
 blockers=[], pending_decisions=[], next_action='Confirm overview and phase mode', paused=False,
 failures=[], steps={s['id']: dict(status='Pending', artifacts=[], sources={}, evidence=[],
 approved=False, reason=None) for s in r['steps']})

def validate(state, r):
 required={'schema_version','registry_version','workflow_id','scope','project_path','checkpoint_path','revision','updated_at','active_phase','active_step','mode','authorization','approvals','decisions','blockers','pending_decisions','next_action','paused','failures','steps'}
 if not required <= state.keys() or state['schema_version'] != 1: raise ValueError('Unsupported or invalid checkpoint; preserve original and recover a copy')
 if state['registry_version'] != r['version']: raise ValueError('Registry migration required; preserve original')
 if state['mode'] not in {'step','phase-parallel','phase-sequential'}: raise ValueError('Invalid mode')
 if not isinstance(state['revision'], int) or state['revision'] < 0: raise ValueError('Invalid revision')
 if not {s['id'] for s in r['steps']} <= state['steps'].keys(): raise ValueError('Missing registry steps')
 schema=json.loads((REGISTRY.parent/'checkpoint.schema.json').read_text())
 types={'string':str,'object':dict,'array':list,'boolean':bool,'integer':int,'null':type(None)}
 for key,rule in schema['properties'].items():
  if key not in state: continue
  if 'type' in rule:
   names=rule['type'] if isinstance(rule['type'],list) else [rule['type']]
   if not any(type(state[key]) is types[t] for t in names): raise ValueError('Invalid field type: '+key)
 for key, unit in state['steps'].items():
  if not {'status','artifacts','sources','evidence','approved','reason'} <= unit.keys(): raise ValueError('Invalid step fields')
  if unit['status'] not in STATUSES: raise ValueError('Invalid status: '+key)
  if unit['status']=='Skipped' and not unit.get('reason'): raise ValueError('Skip requires reason')
  if unit['status']=='Completed' and not unit.get('evidence'): raise ValueError('Completion requires evidence')
  definition=next((s for s in r['steps'] if s['id']==key),None)
  if not definition: raise ValueError('Unknown step: '+key)
  if unit['status']=='Completed' and definition['review_required'] and not unit.get('approved'): raise ValueError('Completion requires scoped approval')
 return state

def ready(state, step):
 return all(state['steps'][d]['status']=='Completed' and state['steps'][d].get('approved') for d in step['depends_on']) and all(state['decisions'].get(d, {}).get('approved') for d in step['decision_dependencies'])

def effective_registry(state, r):
 result=copy.deepcopy(r)
 result['steps'].extend(state.get('dynamic_steps', []))
 for override in state.get('baseline_overrides', []):
  unit=next((s for s in result['steps'] if s['id']==override['step_id']),None)
  if not unit or unit['phase'] in {'0','5','service'} or unit['id'] in {'adapter','implementation','plan','prompts','dod'}:
   raise ValueError('Invalid baseline override target')
  if override.get('scope')!='as-is' or not override.get('evidence') or not override.get('authorization'):
   raise ValueError('Baseline override requires scoped evidence and authorization')
  unit['depends_on']=override['depends_on']

 nodes={s['id']:s for s in result['steps']}
 if len(nodes)!=len(result['steps']): raise ValueError('Duplicate dynamic ID')
 def visit(key, trail):
  if key not in nodes or key in trail: raise ValueError('Invalid dynamic dependency graph')
  for dep in nodes[key]['depends_on']: visit(dep,trail|{key})
 for key in nodes: visit(key,set())
 return result


def candidates(state, r):
 if state['paused'] or not state['authorization'].get('start'): return []
 blocked=set()
 for decision in state['pending_decisions']:
  if not isinstance(decision,dict) or 'blocks' not in decision: return []
  blocked.update(decision['blocks'])
 if state['mode']=='step' and state['authorization'].get('unit_consumed'): return []
 if state['authorization'].get('phase') != state['active_phase']: return []
 return [s['id'] for s in r['steps'] if s['phase']==state['active_phase'] and s['applicability'] not in {'on-request','dynamic'} and s['id'] not in blocked and state['steps'][s['id']]['status'] in {'Pending','Ready'} and ready(state,s)]

def continue_step(state):
 """Call only after explicit lanjut; does not approve open decisions."""
 state['authorization']['unit_consumed']=False


def transition(state, step, target):
 u=state['steps'][step['id']]
 if target not in TRANSITIONS[u['status']]: raise ValueError('Illegal transition')
 if target in {'Ready','In Progress','Completed'} and not ready(state,step): raise ValueError('Dependencies not ready')
 if target=='In Progress' and step['id'] not in candidates(state, {'steps':[step]}): raise ValueError('Execution not authorized')
 if target=='Completed' and (not u['evidence'] or (step['review_required'] and not u['approved'])): raise ValueError('Evidence and scoped review required')
 if target=='Skipped' and not u.get('reason'): raise ValueError('Skip reason required')
 u['status']=target
 if target=='In Progress' and state['mode']=='step': state['authorization']['unit_consumed']=True

def reconcile(state):
 changed=set()
 for key,u in state['steps'].items():
  if any(fingerprint(Path(state['project_path'])/p)!=digest for p,digest in u['sources'].items()): changed.add(key)
 # Each unit records actual consumed files, including code/test evidence.
 for key in changed:
  state['steps'][key]['approved']=False
  if state['steps'][key]['status'] not in {'Pending','Skipped'}: state['steps'][key]['status']='Needs Revalidation'
 return changed

def invalidate(state, r, changed_ids):
 affected=set(changed_ids)
 while True:
  extra={s['id'] for s in r['steps'] if set(s['depends_on']) & affected}
  if extra <= affected: break
  affected |= extra
 for key in affected:
  u=state['steps'][key]
  if u['status'] not in {'Pending','Skipped'}:
   u['status']='Needs Revalidation'; u['approved']=False
 return affected

def close_phase(state,r):
 units=[s for s in r['steps'] if s['phase']==state['active_phase'] and s['applicability']!='on-request']
 return not state['blockers'] and not state['pending_decisions'] and all(state['steps'][s['id']]['status'] in {'Completed','Skipped'} and (not s['review_required'] or state['steps'][s['id']]['approved'] or state['steps'][s['id']]['status']=='Skipped') for s in units)

def save(path,state,r,expected_revision):
 validate(state,r)
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
 lock=p.with_suffix(p.suffix+'.lock')
 fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
 tmp=None
 try:
  os.write(fd,json.dumps({'pid':os.getpid(),'at':now()}).encode()); os.fsync(fd)
  current=json.loads(p.read_text()) if p.exists() else None
  if current: validate(current,effective_registry(current,registry()))
  if (current['revision'] if current else -1)!=expected_revision: raise ValueError('Concurrent update; reload checkpoint')
  out=copy.deepcopy(state); out['revision']=expected_revision+1; out['updated_at']=now()
  with tempfile.NamedTemporaryFile(mode='w',dir=p.parent,delete=False) as f:
   tmp=f.name; json.dump(out,f,indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())
  os.replace(tmp,p); tmp=None
  return out
 finally:
  os.close(fd)
  if tmp: os.unlink(tmp)
  lock.unlink()

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('action',choices=['validate-registry','inspect','save'])
 parser.add_argument('--state',default='docs/aod/WORKFLOW_STATE.json')
 parser.add_argument('--candidate',help='Validated proposed state JSON; save only')
 parser.add_argument('--expected-revision',type=int,default=-1)
 args=parser.parse_args(); r=registry()
 if args.action=='validate-registry': print('Registry valid'); return
 state=json.loads(Path(args.candidate if args.action=='save' else args.state).read_text())
 r=effective_registry(state,r)
 validate(state,r)
 if args.action=='save': state=save(args.state,state,r,args.expected_revision)
 else:
  affected=invalidate(state,r,reconcile(state))
  print(json.dumps({'needs_revalidation':sorted(affected),'ready':candidates(state,r),'phase_exit':close_phase(state,r)},indent=2)); return
 print(json.dumps(state,indent=2))

if __name__=='__main__': main()
