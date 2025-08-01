def p(g):
 r,c=len(g),len(g[0]);s=[]
 for i in range(r):
  for j in(0,c-1):
   if g[i][j]==1:s.append((i,j))
 for j in range(c):
  for i in(0,r-1):
   if g[i][j]==1:s.append((i,j))
 while s:
  i,j=s.pop()
  if g[i][j]==1:
   g[i][j]=-1
   for di,dj in(1,0),(-1,0),(0,1),(0,-1):
    x,y=i+di,j+dj
    if 0<=x<r and 0<=y<c and g[x][y]==1:s.append((x,y))
 for i in range(r):
  for j in range(c):
   g[i][j]=1 if g[i][j]==-1 else 8 if g[i][j]==1 else g[i][j]
 return g