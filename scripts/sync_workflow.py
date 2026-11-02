"""Generate the shared workflow map; --check reports drift without writes."""
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'.agents/skills/aod-orchestrator/references/workflow.json').read_text())
lines=['| Phase | Steps / executing skills |','| --- | --- |']
for p in r['phases']:
 units=[s['skill'] or s['id'] for s in r['steps'] if s['phase']==p['id']]
 lines.append('| '+p['id']+' — '+p['name']+' | '+', '.join('`'+s+'`' for s in units)+' |')
text='\n'.join(lines)+'\n'
for name in ['README.md','AGENTS.md','GEMINI.md','.agents/skills/aod-orchestrator/references/agent-block.md']:
 p=ROOT/name;s=p.read_text();start='<!-- aod:map:start -->';end='<!-- aod:map:end -->'
 if start not in s: raise SystemExit('Missing map markers: '+name)
 a,b=s.split(start);old,c=b.split(end);new=a+start+'\n'+text+end+c
 if '--check' in sys.argv:
  if new!=s: raise SystemExit('Workflow map drift: '+name)
 else: p.write_text(new)
