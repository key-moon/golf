import re
import string

# string.punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
syms = r"=<>!?^|&%()\[\]{},;:*/+-"

def strip(code: str):
  lines = [l for l in code.strip().splitlines() if not l.strip().startswith("#")]
  if len(lines) == 1: return lines[0]
  res = ""
  basic_indent = len(lines[1]) - len(lines[1].lstrip(' '))
  for l in lines:
    stripped = l.strip()
    if len(stripped) == 0:
      continue
    indent = len(l) - len(stripped)
    if stripped.find("#"):
      stripped = stripped.split("#")[0]

    stripped = re.sub(rf"(\w) *([{syms}])", r"\1\2", stripped)
    stripped = re.sub(rf"([{syms}]) *(\w)", r"\1\2", stripped)
    stripped = re.sub(rf"([{syms}]) *([{syms}])", r"\1\2", stripped)

    res += " " * (indent // max(basic_indent, 1)) + stripped
    res += "\n"

  return res.strip()
