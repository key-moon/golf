def p(g):
 m=len(g[0])//2
 X=[[0 for i in R] for R in g]
 for r in range(len(g)):
  X[r][m]=g[r][m]
 return X
