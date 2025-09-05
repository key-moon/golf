def p(g,u=range):
 E=enumerate
 Z=[[C for i,C in E(R)]for R in g]
 T,X=[],[]
 for r in u(len(g)):
  for c in u(len(g[0])):
   try:
    if g[r-1][c]==5 and g[r][c]==8:Z[r][c]=5
   except:pass
   try:
    if g[r+1][c]==5 and g[r][c]==8:Z[r][c]=5
   except:pass
 for i in u(len(Z)):
  if 5 in Z[i]:X.append(g[i])
 for R in X:
  for i in u(len(R)):
     if R[i]==5:T.append(i)
 X=[R[min(T):max(T)+1]for R in X]
 return X