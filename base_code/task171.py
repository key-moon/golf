def p(g):
  g[0]=g[-1]=[8]*len(g[0])
  for r in g[1:-1]:r[0]=r[-1]=8
  return g