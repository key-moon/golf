def p(g):
 h,w=len(g),len(g[0])
 c=min(x for r in g for x in r if x not in (0,2,8))
 i,j=next((i,j)for i in range(h)for j in range(w)if g[i][j]==c)
 s=[(i,j)]
 while s:
  i,j=s.pop()
  for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
   x,y=i+di,j+dj
   if 0<=x<h and 0<=y<w and g[x][y]==0:
    g[x][y]=c;s.append((x,y))
 return g
