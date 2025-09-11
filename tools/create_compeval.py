from tqdm import tqdm
from compress import get_embed_str
from deflate_optimizer.optimizer import optimize_deflate_stream
from utils import get_code_paths, openable_uri, viz_deflate_url
import strip
import os

PURE_PATH = ["base_yu", "base_keymoon", "base_kq5y", "base_zatsu"]
for i in tqdm(range(1, 401)):
  for path in get_code_paths("base_*", i, include_retire=True):
    if "arc" in path: continue
    code = open(path, "rb").read()
    if b"zlib" in code: continue
    stripped = strip.strip_for_zlib(code).encode()
    base_name = path.split("/")[0]
    if base_name in PURE_PATH:
      if 200 <= len(stripped) <= 600:
        dataset_level = 1
      else:
        dataset_level = 2
    else:
      if 200 <= len(stripped) <= 600:
        dataset_level = 3
      else:
        dataset_level = 4

    # write this code into every target level >= dataset_level
    for target_level in range(1, 5):
      if dataset_level <= target_level:
        out_dir = f"data/compeval/{target_level}"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{i:03}_{base_name}.py")
        ind = 1
        while os.path.exists(out_path):
          out_path = os.path.join(out_dir, f"{i:03}_{base_name}_{ind}.py")
          ind += 1
        with open(out_path, "wb") as out_f:
          out_f.write(stripped)
