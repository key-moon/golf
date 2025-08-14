#!/usr/bin/env python3
import sys
import os
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

if len(sys.argv) <= 1:
  print(f"usage: ./{sys.argv[0]} <taskid-or-path>")
  exit(1)

_exec=exec
__builtins__.exec=lambda c,*a:(print(c.decode(),end="") if isinstance(c,bytes) else _exec(c,*a))

if os.path.exists(sys.argv[1]):
  sys.path.insert(0, os.path.dirname(sys.argv[1]))
  module_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
  __import__(module_name)
else:
  __import__(f"dist.task{int(sys.argv[1]):03}")
