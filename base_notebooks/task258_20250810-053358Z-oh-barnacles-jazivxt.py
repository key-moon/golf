def p(g):
 for r in range(len(g)):
  for c in range(len(g[0])-2):
   if g[r][c]==1 and g[r][c+2]==1:g[r][c+1]=2
 return g
