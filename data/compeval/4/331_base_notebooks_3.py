def p(g):
 P=[]
 E=enumerate
 for r,R in E(g):
  for c,C in E(R):
   if g[r][c]==1:P.append([r,c])
 for n in P:
  X,k=n
  if X>0:g[X-1][k]=2
  if X<9:g[X+1][k]=8
  if k>0:g[X][k-1]=7
  if k<9:g[X][k+1]=6
 return g