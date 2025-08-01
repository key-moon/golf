def strip(code: str):
  lines = [l for l in code.strip().splitlines() if not l.strip().startswith("#")]
  if len(lines) == 1: return lines[0]
  res = ""
  basic_indent = len(lines[1]) - len(lines[1].lstrip(' '))
  for l in lines:
    stripped = l.strip()
    indent = len(l) - len(stripped)
    if l.find("#"):
      l = l.split("#")[0]
    res += " " * (indent // max(basic_indent, 1)) + stripped
    res += "\n"
  return res.strip()
