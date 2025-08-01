import re
import string

# string.punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
syms = r"=<>!?^|&%()\[\]{},;:*/+-"

def strip(code: str):
  lines = [l for l in code.strip().splitlines() if not l.strip().startswith("#")]
  if len(lines) == 1: return lines[0]
  res = ""
  basic_indent = min([len(l) - len(l.lstrip(' ')) for l in lines if l.startswith(" ")])
  prev_indent = 0
  for l in lines:
    stripped = l.strip()
    if len(stripped) == 0:
      continue
    indent = (len(l) - len(stripped)) // max(basic_indent, 1)
    if stripped.find("#"):
      stripped = stripped.split("#")[0]

    stripped = re.sub(rf"(\w) *([{syms}])", r"\1\2", stripped)
    stripped = re.sub(rf"([{syms}]) *(\w)", r"\1\2", stripped)
    stripped = re.sub(rf"([{syms}]) *([{syms}])", r"\1\2", stripped)

    # 今が if や for、前が if や for、前とindentレベルが違う→まとめない
    if ":" in stripped or ":" in res.split("\n")[-1] or indent != prev_indent:
      res += "\n" + " " * indent + stripped
    else:
      if res[-1] != ":": res += ";"
      res += stripped
    prev_indent = indent

  return res.strip()
