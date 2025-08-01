def parse_range_str(range_str: str):
  s = set()
  for part in range_str.strip().split(","):
    if "-" in part:
      start, end = map(int, part.split("-"))
      s.update(range(start, end + 1))
    else:
      s.add(int(part))
  return sorted(s)
