def p(g):
 h=len(g)
 for i in range(h):
  g[i][i]=0
  g[i][h-i-1]=0
 return g