def p(g):
 v=set();n=len(g);m=len(g[0])
 for i in range(n):
  for j in range(m):
   if g[i][j] and (i,j) not in v:
    c=[(i,j)];f=[(i,j)];v.add((i,j))
    while f:
     x,y=f.pop()
     for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
      u,b=x+dx,y+dy
      if 0<=u<n and 0<=b<m and g[u][b] and (u,b) not in v:
       v.add((u,b));f+=[(u,b)];c+=[(u,b)]
    a,b=zip(*c);W,H=max(a)-min(a)+1,max(b)-min(b)+1
    if W>1 and H>1 and len(c)==2*(W+H)-4:
     for x,y in c:g[x][y]=3
 return g
