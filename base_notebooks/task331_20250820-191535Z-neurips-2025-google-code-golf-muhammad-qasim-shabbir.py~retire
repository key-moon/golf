def p(g):
 P=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]==1:P.append([r,c])
 for T in P:
  u,Q=T
  if u>0:g[u-1][Q]=2
  if u<9:g[u+1][Q]=8
  if Q>0:g[u][Q-1]=7
  if Q<9:g[u][Q+1]=6
 return g