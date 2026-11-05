"""ARC fixtures exercise real CLI, read-only navigation, graph escaping and installation."""
import copy
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
CLI=ROOT/'.agents/aod/bin/arc'

class ArcTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=Path(self.tmp.name);self.refs=self.root/'docs/references'
  self.refs.mkdir(parents=True)
  self.write('docs/business/PRD.md','# Equipment\n\nRequirement REQ-001\n')
  self.write('app/equipment.py','fixture code')
  self.base=dict(schema_version=1,id='REF-FEAT-equipment-create',title='Create equipment',type='feature',module_id='equipment',feature_id='create',status='active',updated_at='2026-11-05',tags=['running hours'],sources=[{'path':'docs/business/PRD.md','fragment':'equipment','relation':'implements'}],related_refs=[],code_paths=['app/equipment.py'])
  self.doc('features/REF-FEAT-equipment-create.md',self.base,'Detail lifecycle')
  self.write('docs/references/INDEX.md','# Registry\n\n[Create](features/REF-FEAT-equipment-create.md)\n')
 def write(self,path,text):
  p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');return p
 def doc(self,path,data,body=''):
  return self.write('docs/references/'+path,'# '+data['title']+'\n\n<!-- arc:metadata:start -->\n```json\n'+json.dumps(data,ensure_ascii=False)+'\n```\n<!-- arc:metadata:end -->\n\n'+body)
 def run_arc(self,*args,code=0,cwd=None):
  result=subprocess.run(['python3',str(CLI),'--root',str(self.root),*args],capture_output=True,text=True,cwd=cwd)
  self.assertEqual(result.returncode,code,result.stderr+'\n'+result.stdout)
  return result.stdout
 def test_registered_default_and_unregistered_discovery(self):
  d=copy.deepcopy(self.base);d.update(id='REF-UI-equipment-list',title='Equipment list',type='ui')
  self.doc('ui/REF-UI-equipment-list.md',d)
  self.assertEqual(len(json.loads(self.run_arc('list','--json'))),1)
  all_=json.loads(self.run_arc('list','--all','--json'));self.assertEqual(len(all_),2)
  self.assertFalse(next(r for r in all_ if r['type']=='ui')['registered'])
  self.assertIn('unregistered_reference',self.run_arc('check'))
 def test_search_module_and_path_output(self):
  self.assertIn(self.base['id'],self.run_arc('search','running hours'))
  self.assertIn(self.base['id'],self.run_arc('search','lifecycle'))
  self.assertEqual(self.run_arc('list','--module','equipment','--path-only').strip(),'docs/references/features/REF-FEAT-equipment-create.md')
  self.assertEqual(json.loads(self.run_arc('modules','--json')),{'equipment':1})
  self.assertEqual(json.loads(self.run_arc('list','--module','other','--json')),[])
 def test_trace_explicit_sources_and_reverse_relationships(self):
  d=copy.deepcopy(self.base);d.update(id='REF-UI-equipment-form',type='ui',title='Form',sources=[],related_refs=[{'id':self.base['id'],'relation':'integrates_with'}])
  self.doc('ui/REF-UI-equipment-form.md',d)
  trace=json.loads(self.run_arc('trace',self.base['id'],'--json'))
  self.assertTrue(any(e['relation']=='implements' for e in trace['edges']))
  self.assertTrue(any(e['relation']=='integrates_with' for e in trace['edges']))
  self.assertEqual({e['provenance'] for e in trace['edges']},{'metadata'})
 def test_read_only_commands_do_not_change_project(self):
  def snap():return {p.relative_to(self.root).as_posix():p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
  before=snap()
  for args in [('list',),('modules',),('search','equipment'),('show',self.base['id']),('trace',self.base['id']),('graph',),('check',)]:self.run_arc(*args)
  self.assertEqual(before,snap())
 def test_legacy_and_legacy_root_registry_link(self):
  self.write('docs/references/ui/REF-UI-old.md','# Agent Reference Context: Old page\n\n> **Reference ID:** `REF-UI-old`\n> **Upstream Specs:**\n> - PRD: `docs/business/PRD.md#equipment`\n\n---\n')
  with (self.refs/'INDEX.md').open('a') as f:f.write('[old](docs/references/ui/REF-UI-old.md)\n')
  old=json.loads(self.run_arc('show','REF-UI-old','--json'))
  self.assertEqual(old['format'],'legacy');self.assertEqual(old['module_id'],'unknown');self.assertTrue(old['registered'])
  self.assertEqual(old['sources'][0]['relation'],'references')
  out=self.run_arc('check');self.assertIn('legacy_metadata',out);self.assertIn('legacy_registry_link',out)
 def test_missing_source_related_code_and_registered_file(self):
  d=copy.deepcopy(self.base);d['sources'][0]['path']='docs/absent.md';d['related_refs']=[{'id':'REF-UI-missing','relation':'integrates_with'}];d['code_paths']=['app/missing.py']
  self.doc('features/REF-FEAT-equipment-create.md',d)
  with (self.refs/'INDEX.md').open('a') as f:f.write('[missing](features/REF-FEAT-missing.md)\n')
  issues=json.loads(self.run_arc('check','--json',code=1));codes={x['code'] for x in issues}
  self.assertTrue({'missing_source','missing_related_reference','missing_code','missing_registered_file'}<=codes)
 def test_duplicate_id_is_error_and_graph_rejects(self):
  self.doc('features/REF-FEAT-duplicate.md',self.base)
  self.assertIn('duplicate_id',self.run_arc('check',code=1))
  self.run_arc('show',self.base['id'],code=2)
  self.run_arc('graph',code=2)
 def test_malformed_metadata_and_unsafe_paths(self):
  self.write('docs/references/features/REF-FEAT-bad.md','# Bad\n<!-- arc:metadata:start -->\n{}')
  self.assertIn('invalid_reference',self.run_arc('check',code=1))
  (self.refs/'features/REF-FEAT-bad.md').unlink()
  d=copy.deepcopy(self.base);d['sources'][0]['path']='../secret.md'
  self.doc('features/REF-FEAT-equipment-create.md',d)
  self.assertIn('escapes project',self.run_arc('check',code=1))
  self.assertEqual(json.loads(self.run_arc('list','--json')),[])
 def test_symlink_cannot_read_outside_project(self):
  with tempfile.TemporaryDirectory() as other:
   secret=Path(other)/'REF-FEAT-secret.md';secret.write_text('private')
   (self.refs/'REF-FEAT-secret.md').symlink_to(secret)
   self.assertIn('Path escapes project',self.run_arc('check',code=1))
 def test_unresolved_anchor_is_warning_not_false_verification(self):
  d=copy.deepcopy(self.base);d['sources'][0]['fragment']='nonexistent'
  self.doc('features/REF-FEAT-equipment-create.md',d)
  self.assertIn('unresolved_anchor',self.run_arc('check'))
 def test_graph_mermaid_json_and_html_export(self):
  self.assertIn('flowchart TD',self.run_arc('graph'))
  data=json.loads(self.run_arc('graph','--include-code','--json'))
  self.assertTrue(any(n['kind']=='code' for n in data['nodes']))
  out=self.root/'exports/arc.html';self.run_arc('graph','--format','html','--output',str(out))
  text=out.read_text();self.assertIn('ARC Explorer',text);self.assertNotIn('https://cdn',text)
  self.assertIn('../docs/business/PRD.md#equipment',text)
  self.run_arc('graph','--format','html','--output',str(out),code=2)
  self.run_arc('graph','--format','html','--output',str(out),'--force')
  if shutil.which('node'):
   js=re.findall(r'<script>(.*?)</script>',out.read_text(),re.S)[0]
   result=subprocess.run(['node','--check'],input=js,capture_output=True,text=True)
   self.assertEqual(result.returncode,0,result.stderr)
 def test_html_and_mermaid_escape_untrusted_labels(self):
  d=copy.deepcopy(self.base);d['title']='</script><img src=x onerror=alert(1)> "injection"'
  self.doc('features/REF-FEAT-equipment-create.md',d)
  out=self.root/'arc.html';self.run_arc('graph','--format','html','--output',str(out))
  self.assertNotIn('</script><img',out.read_text())
  self.assertIn('\\u003c/script',out.read_text())
  self.assertIn('&quot;injection&quot;',self.run_arc('graph'))
 def test_root_detection_from_subdirectory(self):
  child=self.root/'app';result=subprocess.run(['python3',str(CLI),'modules'],cwd=child,capture_output=True,text=True)
  self.assertEqual(result.returncode,0,result.stderr);self.assertIn('equipment',result.stdout)
 def test_empty_project_has_warning_without_writes(self):
  with tempfile.TemporaryDirectory() as other:
   result=subprocess.run(['python3',str(CLI),'--root',other,'check'],capture_output=True,text=True)
   self.assertEqual(result.returncode,0);self.assertIn('missing_directory',result.stdout)
   self.assertEqual(list(Path(other).iterdir()),[])
 def test_no_registry_requires_explicit_discovery(self):
  (self.refs/'INDEX.md').unlink()
  self.assertEqual(json.loads(self.run_arc('list','--json')),[])
  self.assertEqual(len(json.loads(self.run_arc('list','--all','--json'))),1)
 def test_header_identity_conflict_is_reported(self):
  p=self.refs/'features/REF-FEAT-equipment-create.md'
  p.write_text(p.read_text()+'\n> **Reference ID:** `REF-FEAT-wrong`\n')
  self.assertIn('conflicting_header_id',self.run_arc('check',code=1))
 def test_terminal_listing_escapes_control_characters(self):
  d=copy.deepcopy(self.base);d['title']='Bad\x1b[31m title'
  self.doc('features/REF-FEAT-equipment-create.md',d)
  self.assertNotIn('\x1b',self.run_arc('list'))
 def test_install_cli_executable_and_reinstall_preserves_arc(self):
  before=(self.refs/'INDEX.md').read_bytes()
  for _ in range(2):subprocess.run(['bash',str(ROOT/'install.sh'),'--yes',str(self.root)],check=True,capture_output=True)
  cli=self.root/'.agents/aod/bin/arc';self.assertTrue(os.access(cli,os.X_OK))
  result=subprocess.run([str(cli),'--root',str(self.root),'modules'],capture_output=True,text=True)
  self.assertEqual(result.returncode,0,result.stderr);self.assertIn('equipment',result.stdout)
  self.assertEqual((self.refs/'INDEX.md').read_bytes(),before)
  self.assertFalse((self.root/'.agents/aod/tests').exists());self.assertFalse((self.root/'.agents/aod/scripts').exists())

if __name__=='__main__':unittest.main()
