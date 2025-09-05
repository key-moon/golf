def p(g):
 r=[x[:]for x in g]
 n,m=len(g),len(g[0])
 for i in range(n):
  for j in range(m):
   if g[i][j]:
    v=g[i][j]
    for d in[(-1,-1),(-1,1),(1,1),(1,-1)]:
     x,y=i+d[0],j+d[1]
     while 0<=x<n and 0<=y<m:
      r[x][y]=v
      x+=d[0]
      y+=d[1]
 return r