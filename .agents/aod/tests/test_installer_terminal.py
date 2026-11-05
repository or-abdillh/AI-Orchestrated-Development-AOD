"""Exercise the actual installer through a controlling pseudo-terminal."""
import errno
import os
from pathlib import Path
import pty
import select
import signal
import subprocess
import tempfile
import time
import unittest

ROOT=Path(__file__).resolve().parents[3]


def terminal_install(target, answers):
 pid,fd=pty.fork()
 if pid==0:
  os.environ['NO_COLOR']='1'
  os.execv('/bin/bash',['bash',str(ROOT/'install.sh'),'--interactive',str(target)])
 output=bytearray();sent=False;deadline=time.monotonic()+15
 try:
  while time.monotonic()<deadline:
   readable,_,_=select.select([fd],[],[],0.2)
   if not readable: continue
   try: data=os.read(fd,65536)
   except OSError as exc:
    if exc.errno==errno.EIO: break
    raise
   if not data: break
   output.extend(data)
   if not sent and b'Pilihan [1-4]:' in output:
    os.write(fd,answers.encode());sent=True
  else:
   os.kill(pid,signal.SIGKILL)
   raise AssertionError('Installer terminal test timed out')
 finally:
  os.close(fd)
  _,status=os.waitpid(pid,0)
 return os.waitstatus_to_exitcode(status),output.decode(errors='replace')


class TerminalInstallerTests(unittest.TestCase):
 def test_banner_and_noninteractive_output(self):
  with tempfile.TemporaryDirectory() as tmp:
   result=subprocess.run(['bash',str(ROOT/'install.sh'),'--yes','--no-color',tmp],capture_output=True,text=True,check=True)
   self.assertIn('___    ____  ____',result.stdout)
   self.assertIn('AI-Orchestrated Development',result.stdout)
   self.assertIn('[5/5] Instalasi selesai',result.stdout)
   self.assertIn('Progres:',result.stdout)
   self.assertIn('Hasil:',result.stdout)
   self.assertNotIn('\x1b[',result.stdout)
   self.assertNotIn('Pilihan [1-4]:',result.stdout)
 def test_cancel_leaves_project_untouched(self):
  with tempfile.TemporaryDirectory() as tmp:
   code,output=terminal_install(tmp,'4\n')
   self.assertEqual(code,0,output)
   self.assertIn('dibatalkan',output)
   self.assertFalse((Path(tmp)/'.agents').exists())
 def test_empty_answer_does_not_install(self):
  with tempfile.TemporaryDirectory() as tmp:
   code,output=terminal_install(tmp,'\n4\n')
   self.assertEqual(code,0,output)
   self.assertIn('Jawaban kosong tidak memulai instalasi',output)
   self.assertFalse((Path(tmp)/'.agents').exists())
 def test_preview_change_target_and_confirm(self):
  with tempfile.TemporaryDirectory() as tmp:
   old=Path(tmp)/'old';new=Path(tmp)/'project with spaces'
   code,output=terminal_install(old,'3\n2\n'+str(new)+'\n1\n')
   self.assertEqual(code,0,output)
   self.assertIn('.agents/aod-package.json',output)
   self.assertTrue((new/'AGENTS.md').exists())
   self.assertFalse(old.exists())
   self.assertIn('[5/5] Instalasi selesai',output)
 def test_invalid_option_and_help(self):
  for args,expected in [(['--help'],0),(['--unknown'],1),(['--yes','--interactive'],1)]:
   result=subprocess.run(['bash',str(ROOT/'install.sh'),*args],capture_output=True,text=True)
   self.assertEqual(result.returncode,expected)

if __name__=='__main__':unittest.main()
