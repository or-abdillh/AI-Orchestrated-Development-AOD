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

def plan_digest(plan):
 return hashlib.sha256(json.dumps(plan,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def change_baseline(r, project, plan, response, path):
 """Initialize only after actual scoped execution authorization; never infer sign-off."""
 if not isinstance(response,str) or not response.strip(): raise ValueError('Explicit execution authorization required')
 if not isinstance(plan,dict) or not all(plan.get(k) for k in ('id','scope','implementation','verification')):
  raise ValueError('Change plan needs id, scope, implementation and verification')
 if not isinstance(plan.get('document_changes'),list): raise ValueError('Declare affected document sections, including an empty list when none')
 if not isinstance(plan['implementation'],list) or not isinstance(plan['verification'],list): raise ValueError('Plan work must be lists')
 if any(not isinstance(x,str) or not x.strip() for x in plan['implementation']+plan['verification']): raise ValueError('Plan work must contain nonempty descriptions')
 for item in plan['document_changes']:
  if not isinstance(item,dict) or not all(item.get(k) for k in ('path','section','reason','timing')) or item['timing'] not in {'before-code','after-verification'}:
   raise ValueError('Document changes require path, section, reason and timing')
 if not isinstance(plan['id'],str) or not plan['id'] or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' for c in plan['id']):
  raise ValueError('Use a stable alphanumeric change ID')
 s=baseline(r,project,plan['scope'],path)
 s.update(profile='change',workflow_id='change:'+plan['id'],active_phase='change',mode='change-sequential',change_plan=copy.deepcopy(plan))
 s['dynamic_steps']=[]
 previous=[]
 for stage in ('contracts','implementation','verification','documentation'):
  key='cr:'+plan['id']+':'+stage
  definition=dict(id=key,phase='change',skill=None,purpose=stage,outputs=[],depends_on=previous[:],decision_dependencies=[],applicability='required',review_required=False)
  s['dynamic_steps'].append(definition)
  s['steps'][key]=dict(status='Pending',artifacts=[],sources={},evidence=[],approved=False,reason=None)
  previous=[key]
 s['authorization']=dict(start=True,scope=plan['scope'],plan_digest=plan_digest(plan),step_ids=[x['id'] for x in s['dynamic_steps']],response=response)
 s['approvals'].append(dict(kind='execution-plan',response=response,scope=plan['scope'],digest=plan_digest(plan),at=now()))
 s['next_action']='Update essential contract sections, then implement approved scope without phase gates'
 return s

def change_authorized(state):
 a=state['authorization']
 return bool(a.get('start') and a.get('response') and a.get('scope')==state['scope'] and a.get('plan_digest')==plan_digest(state.get('change_plan',{})))

def validate(state, r):
 required={'schema_version','registry_version','workflow_id','scope','project_path','checkpoint_path','revision','updated_at','active_phase','active_step','mode','authorization','approvals','decisions','blockers','pending_decisions','next_action','paused','failures','steps'}
 if not required <= state.keys() or state['schema_version'] != 1: raise ValueError('Unsupported or invalid checkpoint; preserve original and recover a copy')
 if state['registry_version'] != r['version']: raise ValueError('Registry migration required; preserve original')
 if state.get('profile','guided') not in {'guided','change'}: raise ValueError('Invalid workflow profile')
 if state['mode'] not in {'step','phase-parallel','phase-sequential','change-sequential','change-parallel'}: raise ValueError('Invalid mode')
 if state.get('profile')=='change' and not change_authorized(state): raise ValueError('Changed or unauthorized execution plan; preserve history and resolve changed scope')
 if state.get('profile')=='change':
  expected=['cr:'+state['change_plan']['id']+':'+stage for stage in ('contracts','implementation','verification','documentation')]
  if state['authorization'].get('step_ids')!=expected or [d['id'] for d in state.get('dynamic_steps',[])]!=expected: raise ValueError('Change pipeline scope mismatch')
  for index,d in enumerate(state['dynamic_steps']):
   if d['depends_on']!=expected[index-1:index] or d['phase']!='change' or d['review_required']: raise ValueError('Invalid change pipeline dependencies')
 if state.get('profile','guided')=='guided' and state['mode'].startswith('change-'): raise ValueError('Change mode requires change profile')
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
 definitions={s['id']:s for s in effective_registry(state,registry())['steps']}
 if state.get('profile')=='change':
  ancestors=set(step['depends_on'])
  pending=list(ancestors)
  while pending:
   for dep in definitions[pending.pop()]['depends_on']:
    if dep not in ancestors: ancestors.add(dep); pending.append(dep)
  if any(any(fingerprint(Path(state['project_path'])/p)!=digest for p,digest in state['steps'][k]['sources'].items()) for k in ancestors): return False
 return all(state['steps'][d]['status']=='Completed' and (not definitions[d]['review_required'] or state['steps'][d].get('approved')) for d in step['depends_on']) and all(state['decisions'].get(d, {}).get('approved') for d in step['decision_dependencies'])

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
 # Propagate decision scope; independent units remain executable.
 while True:
  extra={s['id'] for s in r['steps'] if set(s['depends_on']) & blocked}
  if extra <= blocked: break
  blocked |= extra
 if state['mode']=='step' and state['authorization'].get('unit_consumed'): return []
 if state.get('profile')=='change':
  if not change_authorized(state): return []
  stale={k for k,u in state['steps'].items() if any(fingerprint(Path(state['project_path'])/p)!=digest for p,digest in u['sources'].items())}
  allowed=set(state['authorization'].get('step_ids',[]))
  return [s['id'] for s in r['steps'] if s['id'] in allowed and s['phase']=='change' and s['id'] not in blocked|stale and state['steps'][s['id']]['status'] in {'Pending','Ready'} and ready(state,s)]
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
  if state.get('profile')=='change' and state['steps'][key]['status']!='Needs Revalidation': state['steps'][key]['status_before_source_review']=state['steps'][key]['status']
  if state.get('profile')!='change': state['steps'][key]['approved']=False
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
   u['status']='Needs Revalidation'
   if state.get('profile')!='change': u['approved']=False
 return affected

def resolve_source_change(state, unit_id, classification, evidence, r):
 """Human/agent supplies a documented impact assessment, not just a refreshed hash."""
 if state.get('profile')!='change' or classification not in {'editorial','contract'} or not evidence:
  raise ValueError('Scoped change impact assessment and evidence required')
 unit=state['steps'][unit_id]
 changes={p:(old,fingerprint(Path(state['project_path'])/p)) for p,old in unit['sources'].items() if fingerprint(Path(state['project_path'])/p)!=old}
 if not changes: return set()
 if classification=='editorial' and any(new is None for old,new in changes.values()): raise ValueError('Missing source is not an editorial change')
 state.setdefault('source_reviews',[]).append(dict(unit=unit_id,classification=classification,evidence=evidence,changes=changes,at=now()))
 if classification=='contract':
  affected=invalidate(state,r,{unit_id})
 else:
  affected=set()
 for p,(old,new) in changes.items(): unit['sources'][p]=new
 # Restoration is explicit and evidence-based; preserve approvals/history.
 if classification=='editorial' and unit['status']=='Needs Revalidation':
  unit['status']=unit.pop('status_before_source_review','Needs Revalidation')
 return affected

def close_phase(state,r):
 if state.get('profile')=='change':
  selected=set(state['authorization'].get('step_ids',[]))
  return change_authorized(state) and bool(selected) and not state['blockers'] and not state['pending_decisions'] and all(state['steps'][k]['status']=='Completed' and state['steps'][k]['evidence'] for k in selected) and not any(any(fingerprint(Path(state['project_path'])/p)!=digest for p,digest in state['steps'][k]['sources'].items()) for k in selected)
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
 parser.add_argument('action',choices=['validate-registry','inspect','save','init-change'])
 parser.add_argument('--plan',help='Scoped change plan JSON')
 parser.add_argument('--response',help='Actual developer execution authorization, not a fabricated response')
 parser.add_argument('--project',default='.')
 parser.add_argument('--state',default='docs/aod/WORKFLOW_STATE.json')
 parser.add_argument('--candidate',help='Validated proposed state JSON; save only')
 parser.add_argument('--expected-revision',type=int,default=-1)
 args=parser.parse_args(); r=registry()
 if args.action=='validate-registry': print('Registry valid'); return
 if args.action=='init-change':
  if not args.plan: parser.error('--plan required')
  if Path(args.state).exists(): parser.error('Preserve existing workflow; choose a separate change checkpoint path')
  state=change_baseline(r,args.project,json.loads(Path(args.plan).read_text()),args.response,args.state)
  print(json.dumps(save(args.state,state,effective_registry(state,r),-1),indent=2)); return
 state=json.loads(Path(args.candidate if args.action=='save' else args.state).read_text())
 r=effective_registry(state,r)
 validate(state,r)
 if args.action=='save': state=save(args.state,state,r,args.expected_revision)
 else:
  changed=reconcile(state)
  affected=changed if state.get('profile')=='change' else invalidate(state,r,changed)
  print(json.dumps({'needs_revalidation':sorted(affected),'ready':candidates(state,r),'phase_exit':close_phase(state,r)},indent=2)); return
 print(json.dumps(state,indent=2))

if __name__=='__main__': main()
