def p(g):
 n=len(g)
 for i in range(n):
  for j in range(n):
   if g[i][j]==5:
    s=[(i,j)];g[i][j]=0
    for x,y in s:
     for d in 1,-1:
      if 0<=x+d<n and g[x+d][y]==5:s+=[(x+d,y)];g[x+d][y]=0
      if 0<=y+d<n and g[x][y+d]==5:s+=[(x,y+d)];g[x][y+d]=0
    l=5-len(s)
    for x,y in s:g[x][y]=l
 return g