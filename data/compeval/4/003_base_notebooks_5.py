def p(g):
  return [[c*2 for c in r] for r in g + (g[:3] if g[1] == g[4] else g[2:5])]
