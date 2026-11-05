"""Focused structural checks for package JSON, links and Markdown fences."""
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parents[3]
manifest=json.loads((root/'.agents/aod-package.json').read_text())
if len(manifest['files'])!=len(set(manifest['files'])): raise SystemExit('Duplicate manifest path')
for name in manifest['files']:
 if name.startswith(('scripts/', 'tests/', 'test/', '.agents/aod/')) and name != '.agents/aod/bin/arc':
  raise SystemExit('Maintainer/root tooling must not be installed: '+name)
 p=root/name
 if not p.is_file(): raise SystemExit('Missing package file: '+name)
 if p.suffix=='.json': json.loads(p.read_text())
for p in [root/'README.md',root/'AGENTS.md',root/'GEMINI.md',*root.glob('.agents/skills/aod-*/**/*.md')]:
 text=p.read_text()
 if len(re.findall(r'^```',text,re.M))%2: raise SystemExit('Unclosed Markdown fence: '+str(p))
 if p.parent.name=='references' and 'aod-orchestrator' in p.parts or p.name=='SKILL.md' and p.parent.name=='aod-orchestrator':
  for link in re.findall(r'\]\(([^)]+)\)',text):
   if not link.startswith(('http:','https:','#')) and not (p.parent/link).exists(): raise SystemExit('Broken local link: '+link)
print('Package JSON, manifest, orchestrator links and Markdown fences valid')
