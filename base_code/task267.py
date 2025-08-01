def p(g):
 c=g[-1][0];s=min(x for r in g for x in r if x)
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==s:g[i][j]=c
 g[-1][0]=0;return g
