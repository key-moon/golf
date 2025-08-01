import re
import string

# string.punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
syms = r"=<>!?^|&%()\[\]{},;:*/+-"

def strip(code: str):
  matches = re.findall(r'val_[\w_]+', code)

  vals = list(string.ascii_uppercase[::-1])
  for replace in matches:
    val_name = vals.pop()
    if val_name in code:
      assert len(vals) != 0, "auto variable resolution failed"
      val_name = vals.pop()
    code = code.replace(replace, val_name)

  lines = [l for l in code.strip().splitlines() if not l.strip().startswith("#") and l.strip()]
  if len(lines) == 1: return lines[0]
  res = ""
  basic_indent = min([1] + [len(l) - len(l.lstrip(' ')) for l in lines if l.startswith(" ")])
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

    # 今が if や for、前が if や for、前とindentレベルが違う→一行にまとめない
    if ":" in stripped or ":" in res.split("\n")[-1] or indent != prev_indent:
      res += "\n" + " " * indent + stripped
    else:
      if res and res[-1] != ":": res += ";"
      res += stripped
    prev_indent = indent
  
  return res.strip()
