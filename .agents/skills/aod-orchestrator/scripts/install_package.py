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
 preserved=0
 for item in manifest['files']:
  rel=Path(item)
  if rel.is_absolute() or '..' in rel.parts: raise ValueError('Invalid package path')
  src=source/rel;dst=target/rel
  if dst.is_symlink() or not dst.resolve().is_relative_to(target): raise ValueError('Unsafe target path: '+item)
  if item=='.agents/rules/aod-architecture-engineering.md' and dst.exists():
   preserved+=1
   continue
  operations.append((dst,src.read_bytes()))
 block=(source/'.agents/skills/aod-orchestrator/references/agent-block.md').read_text()
 pointer='<!-- aod:start -->\nRead AGENTS.md and use aod-orchestrator for Mulai/Lanjut/Status/Jeda/Ubah mode AOD. Route initialized-project fixes/features/modules through the scoped change profile, not guided Phase 0–5. One accepted plan authorizes affected contract patches, implementation, checks and factual documentation. Do not request repeated phase/document approvals for the same scope. Pause only for new material decisions or actions outside authorization. Follow project architecture rules and preserve baseline state.\n<!-- aod:end -->\n'
 for item in ['AGENTS.md','GEMINI.md','CLAUDE.md','.github/copilot-instructions.md','.cursor/rules/aod.mdc','.windsurfrules']:
  dst=target/item
  if dst.is_symlink() or not dst.resolve().is_relative_to(target): raise ValueError('Unsafe instruction path')
  content=dst.read_text() if dst.exists() else ''
  replacement=block if item in ['AGENTS.md','GEMINI.md'] else pointer
  if item.endswith('.mdc') and not dst.exists(): content='---\ndescription: AOD workflow\nalwaysApply: true\n---\n'
  operations.append((dst,inject(content,replacement).encode()))
 # Preflight all paths/markers/source files before the first target write.
 counts={'created':0,'updated':0,'unchanged':0}
 total=len(operations)
 print(f'  Memeriksa {total} file terkelola dan blok instruksi ...',flush=True)
 for number,(dst,data) in enumerate(operations,1):
  exists=dst.exists()
  if exists and dst.read_bytes()==data:
   counts['unchanged']+=1
  else:
   atomic(dst,data)
   counts['updated' if exists else 'created']+=1
  if number==total or number%50==0:
   print(f'  Progres: {number}/{total} file diperiksa',flush=True)
 print(f"  Hasil: {counts['created']} baru, {counts['updated']} diperbarui, {counts['unchanged']} sudah sesuai.")
 print(f'  Aturan arsitektur proyek dipertahankan: {preserved}.')

if __name__=='__main__': install(*sys.argv[1:])
