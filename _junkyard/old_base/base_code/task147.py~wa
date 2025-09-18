def p(g):
 m,n=len(g),len(g[0])
 for i in range(m):
  for j in range(n):
   if g[i][j]==3:
    s=[(i,j)];g[i][j]=0
    for x,y in s:
     for a,b in(1,0),(-1,0),(0,1),(0,-1):
      u=x+a;v=y+b
      if 0<=u<m and 0<=v<n and g[u][v]==3:s.append((u,v));g[u][v]=0
    for x,y in s:g[x][y]=8 if len(s)>2 else 3
 return g