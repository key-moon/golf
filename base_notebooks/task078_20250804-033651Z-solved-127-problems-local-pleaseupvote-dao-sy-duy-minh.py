def p(g):
 d={i:0 for i in range(len(g[0]))}
 X=[[1 if C==1 else 0 for C in R] for R in g]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if C==2:d[c]+=1
 for r,R in E(X):
  for c,C in E(R):
   if C==0 and d[c]>0:
    X[r][c]=2
    d[c]-=1
 return X
