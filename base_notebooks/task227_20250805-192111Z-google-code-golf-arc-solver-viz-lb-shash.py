def p(g,R=range(4)):
 for i in R:
  for j in R:g[i][j]+=g[i+4][j]
 g=[[2 if C==0 else 1 for C in R]for R in g];g=[[0 if C!=2 else 2 for C in R]for R in g]
 return g[:4]