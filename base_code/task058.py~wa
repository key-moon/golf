def p(g):
 n=len(g);d=[(0,1),(1,0),(0,-1),(-1,0)];i=x=y=0
 while 1:
  g[x][y]=3
  a,b=d[i];u,v=x+a,y+b
  if u<0or u>=n or v<0or v>=n or g[u][v]:
   i=(i+1)%4;a,b=d[i];u,v=x+a,y+b
   if u<0or u>=n or v<0or v>=n or g[u][v]:break
  x,y=u,v
 return g