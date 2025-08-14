import string

import zopfli
import zopfli.zlib
import strip
from utils import get_code_paths, openable_uri, viz_deflate_url
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

strippers = {
  "sep_space": strip.get_stripper(
    prefer_sep=" ",
    remove_literal_statements=True,
    remove_asserts=True,
    remove_debug=True,
    preserve_locals=list("_" + string.ascii_lowercase),
    rename_globals=False,
    hoist_literals=False,
  ),
  "sep_tab": strip.get_stripper(
    prefer_sep="\t",
    remove_literal_statements=True,
    remove_asserts=True,
    remove_debug=True,
    preserve_locals=list("_" + string.ascii_lowercase),
    rename_globals=False,
    hoist_literals=False,
  )
}

TARGET = "sep_tab"

for i in range(1, 401):
  for base_path in get_code_paths("base_*", i):
    code = open(base_path, "rb").read()
    if 2000 <= len(code): continue
    result = {name: zopfli.zlib.compress(stripper(code), numiterations=150)[2:-4] for name, stripper in strippers.items()}
    sorted_result = sorted(result.items(), key=lambda x: len(x[1]))

    best_stripper, best_comp = sorted_result[0]
    best_score = len(best_comp)
    if len(code) <= best_score + 65: continue

    my_score = len(result[TARGET])
    print(f"{base_path}:")
    viz_str = " / ".join([openable_uri(f"{name}({len(code)})", viz_deflate_url(code)) for name, code in sorted_result])
    if best_stripper == TARGET:
      next_score = len(sorted_result[1][1])
      print(f"✅ ({my_score - next_score}): {viz_str}")
    else:
      diff = my_score - best_score
      print(f"{"❌" if diff != 0 else "➖"} (+{diff}): {viz_str}")

