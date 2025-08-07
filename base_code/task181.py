def p(g):
 for r in range(3):
  for c,v in enumerate(g[r]):
   if v==8:g[r][8-c]=8
 return g
