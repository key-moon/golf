def p(g,R=range):
 A=len(g)
 for i in R(A):
  for(x,y)in zip(R(1,A,2),R(i+1,A,2)):
   if g[0][i]:g[x][y]=4
   if g[i][0]:g[y][x]=4
 return g