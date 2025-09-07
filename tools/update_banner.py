from public_data import apply_banner_update, build_banner_lines_for_task
import os

from utils import get_code_paths

base_dir = os.path.join(os.path.dirname(__file__), '..', 'base')
for task_id in range(1, 401):
  for base_path in get_code_paths("base_*", task_id):
    with open(base_path, 'r', encoding='utf-8') as f:
      content = f.read()
    banner_lines = build_banner_lines_for_task(task_id)
    content, updated = apply_banner_update(content, banner_lines)
    if updated:
      with open(base_path, 'w', encoding='utf-8') as f:
        f.write(content)
