def p(g):
 h,w,R=len(g),len(g[0]),range;q=[(i,j)for i in(0,h-1)for j in R(w)if g[i][j]<1]+[(i,j)for i in R(h)for j in(0,w-1)if g[i][j]<1]
 while q:
  i,j=q.pop()
  if g[i][j]<1:g[i][j]=3;q+=[(x,y)for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if 0<=x<h and 0<=y<w and g[x][y]<1]
 for i in R(h):
  for j in R(w):
   if g[i][j]<1:g[i][j]=2
 return g
