#!/usr/bin/env python3
import sys
import os
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

if len(sys.argv) <= 1:
  print(f"usage: ./{sys.argv[0]} <taskid-or-path>")
  exit(1)

import zlib
zlib.decompress=lambda *argc: (sys.stdout.buffer.write(argc[0]),"")[1]

if os.path.exists(sys.argv[1]):
  sys.path.insert(0, os.path.dirname(sys.argv[1]))
  module_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
  __import__(module_name)
else:
  __import__(f"dist.task{int(sys.argv[1]):03}")
