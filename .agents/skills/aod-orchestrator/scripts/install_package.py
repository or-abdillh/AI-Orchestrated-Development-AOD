"""Install only manifest-owned package files and marked AOD instruction blocks."""
import json
import os
from pathlib import Path
import sys
import tempfile


def atomic(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 name=None
 try:
  with tempfile.NamedTemporaryFile(dir=path.parent,delete=False) as f:
   name=f.name;f.write(data);f.flush();os.fsync(f.fileno())
  os.replace(name,path);name=None
 finally:
  if name: os.unlink(name)


def inject(content,block):
 start='<!-- aod:start -->';end='<!-- aod:end -->'
 if content.count(start)!=content.count(end) or content.count(start)>1:
  raise ValueError('Malformed or duplicate AOD markers')
 if start in content:
  a=content.index(start);b=content.index(end)
  if b<a: raise ValueError('Reversed AOD markers')
  return content[:a]+block.rstrip()+content[b+len(end):]
 return content+('\n\n' if content else '')+block.rstrip()+'\n'


def install(source,target):
 source=Path(source).resolve();target=Path(target).resolve()
 manifest=json.loads((source/'.agents/aod-package.json').read_text())
 operations=[]
 for item in manifest['files']:
  rel=Path(item)
  if rel.is_absolute() or '..' in rel.parts: raise ValueError('Invalid package path')
  src=source/rel;dst=target/rel
  if dst.is_symlink() or not dst.resolve().is_relative_to(target): raise ValueError('Unsafe target path: '+item)
  if item=='.agents/rules/aod-architecture-engineering.md' and dst.exists(): continue
  operations.append((dst,src.read_bytes()))
 block=(source/'.agents/skills/aod-orchestrator/references/agent-block.md').read_text()
 pointer='<!-- aod:start -->\nRead AGENTS.md and use aod-orchestrator for Mulai/Lanjut/Status/Jeda/Ubah mode AOD. Execute specialists and return control. Follow scoped approvals, registry dependencies, checkpoint protocol and project architecture rules.\n<!-- aod:end -->\n'
 for item in ['AGENTS.md','GEMINI.md','CLAUDE.md','.github/copilot-instructions.md','.cursor/rules/aod.mdc','.windsurfrules']:
  dst=target/item
  if dst.is_symlink() or not dst.resolve().is_relative_to(target): raise ValueError('Unsafe instruction path')
  content=dst.read_text() if dst.exists() else ''
  replacement=block if item in ['AGENTS.md','GEMINI.md'] else pointer
  if item.endswith('.mdc') and not dst.exists(): content='---\ndescription: AOD workflow\nalwaysApply: true\n---\n'
  operations.append((dst,inject(content,replacement).encode()))
 # Preflight all paths/markers/source files before the first target write.
 for dst,data in operations: atomic(dst,data)
 print('AOD package updated; project artifacts and architecture rules preserved.')

if __name__=='__main__': install(*sys.argv[1:])
