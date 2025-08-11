def p(g):
 X=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if C==5:
    if c not in X:X.append(c)
    g[r][c]=X.index(c)+1
 return g
