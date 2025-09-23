import json
import os
import hashlib

checked_hash = json.load(open(".cache/notebooks_check_cache.json", "r"))

def get_sha256_hex(filepath):
  with open(filepath, "rb") as f:
    return hashlib.sha256(f.read()).hexdigest()

notebook_dir = "base_notebooks"
seen_contents = set()

for fname in os.listdir(notebook_dir):
  if fname.startswith("task") and "_" in fname:
    task_id = fname[4:fname.index("_")]
    fpath = os.path.join(notebook_dir, fname)
    content_hash = get_sha256_hex(fpath)
    key = f"{task_id}|{content_hash}"
    if key in seen_contents:
      os.remove(fpath)
      continue
    seen_contents.add(key)
    checked_hash[key] = True

with open(".cache/notebooks_check_cache.json", "w") as f:
  json.dump(checked_hash, f)
