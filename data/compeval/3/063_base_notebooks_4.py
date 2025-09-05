def p(g):
 q=range
 n=len(g)
 r=[o[:]for o in g]
 for j in range(n):
  if g[1][j]==0 and g[n-2][j]==0 and sum(g[i][j]for i in q(1,n-1))==0:
   for i in q(1,n-1):r[i][j]=3
 for i in range(n):
  if g[i][1]==0 and g[i][n-2]==0 and sum(g[i][j]for j in q(1,n-1))==0:
   for j in q(1,n-1):
    if r[i][j]==0:r[i][j]=3
 return r
