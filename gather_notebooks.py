from hashlib import sha256
import json
import os
import sys
import zipfile
import subprocess

from checker import check
from utils import get_task
import re

def safe_check(path: str, i: int):
  FORBID_EVENTS = {
      "import", "module.__getattr__", "importlib.import_module",
      "open", "os.open", "os.openat",
      "subprocess.Popen", "os.system", "os.fork", "os.forkpty",
      "os.exec", "os.execve", "os.execv", "os.execveat", "posix_spawn",
      "socket.__new__", "socket.connect", "socket.bind", "socket.listen",
      "socket.send", "socket.recv",
      "code.__new__", "ctypes.dlopen", "builtins.__import__",
  }
  ALLOWLIST_MODNAMES = {"math","collections","itertools","functools","re","tmp.tmp","tmp"}
  def audit_hook(event, args):
    if event == "import":
      modname = args[0] if args else None
      if modname not in ALLOWLIST_MODNAMES:
        raise PermissionError(f"audit: blocked import: {modname!r}")
    elif event == "open":
      if not args[0].endswith(path) or args[1] != "r":
        raise PermissionError(f"audit: blocked open: {args[0]}")
    elif event in FORBID_EVENTS:
        raise PermissionError(f"audit: blocked event: {event} ({args})")
  task = get_task(i)
  sys.addaudithook(audit_hook)
  return check(path, task=task, knockout=1).correct == 1

if __name__ == "__main__":
  checked_hash = json.load(open("notebooks_check_cache.json", "r"))

  tmp_dir = "tmp"
  os.makedirs(tmp_dir, exist_ok=True)
  for root, _, files in os.walk("notebooks"):
    for file in files:
      if file != "submission.zip":
        continue
      zip_path = os.path.join(root, file)
      with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for name in zip_ref.namelist():
          task_match = re.match(r"task(\w{3})\.py$", name)
          if not task_match:
            print(f"Invalid file name in {zip_path}: {name}")
            continue
          task_number = int(task_match.group(1))
          extracted_path = os.path.join(tmp_dir, "tmp.py")
          with open(extracted_path, "wb") as f:
            f.write(zip_ref.read(name))
          with open(extracted_path, "r") as f:
            code = f.read()
            if "import os" in code or "import sys" in code:
              print(f"Cheating in {zip_path}: {name}")
              continue
          digest = f"{task_number:03}|{sha256(code.encode()).hexdigest()}"
          if digest not in checked_hash:
            verdict = False
            try:
              result = subprocess.run(
                [sys.executable, "-c", f"from gather_notebooks import safe_check; print(safe_check({extracted_path!r},{task_number}))"],
                capture_output=True, text=True, check=True
              )
              verdict = result.stdout.strip() == "True"
              if verdict:
                print(f"Valid solution in {zip_path}: {name}")
              else:
                print(f"Incorrect solution in {zip_path}: {name}")
            except subprocess.CalledProcessError as e:
              print(f"Error while checking {zip_path}: {name}\n{e.stderr}")
            checked_hash[digest] = verdict
            json.dump(checked_hash, open("notebooks_check_cache.json", "w"))
          if checked_hash[digest]:
            open(f"base_notebooks/task{task_number:03}_{root.split('/')[-1]}.py", "wb").write(zip_ref.read(name))
