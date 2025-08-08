def p(g,E=enumerate):
 for r,R in E(g):
  for c,C in E(R):
   if r<len(g)//2:g[r][c]=g[-(r+1)][c]
 return g