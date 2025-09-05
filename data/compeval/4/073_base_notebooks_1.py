def p(g):
 X=[[5 if C==5 else 0 for C in R]for R in g]
 for r in range(len(g)):
  for c in range(len(g[r])):
   C=g[r][c]
   if C>0and C!=5:X[len(g)-1][c]=C
 return X