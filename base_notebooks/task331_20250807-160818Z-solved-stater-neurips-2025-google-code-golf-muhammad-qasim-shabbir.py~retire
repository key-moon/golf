def p(g):
 P=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]==1:P.append([r,c])
 for b in P:
  u,j=b
  if u>0:g[u-1][j]=2
  if u<9:g[u+1][j]=8
  if j>0:g[u][j-1]=7
  if j<9:g[u][j+1]=6
 return g