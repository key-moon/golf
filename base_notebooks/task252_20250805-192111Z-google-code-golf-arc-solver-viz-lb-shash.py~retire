def p(g,R=range):
 N=len(g)
 for i in R(N):
  for x,y in zip(R(1,N,2),R(i+1,N,2)):
   if g[0][i]:g[x][y]=4
   if g[i][0]:g[y][x]=4
 return g