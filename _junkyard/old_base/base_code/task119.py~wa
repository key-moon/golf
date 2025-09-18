def p(g):
 r=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]]
 a,b=max(((u,v)for u in r for v in r if g[u[0]][u[1]]!=g[v[0]][v[1]]),
        key=lambda x:abs(x[0][0]-x[1][0])+abs(x[0][1]-x[1][1]))
 x0,y0=x1,y1=a[0],a[1];x1,y1=b[0],b[1]
 dx,dy=abs(x1-x0),abs(y1-y0);sx=1 if x0<x1 else-1;sy=1 if y0<y1 else-1
 err=dx-dy
 while True:
  if g[x0][y0]==0:g[x0][y0]=3
  if x0==x1 and y0==y1:break
  e2=err*2
  if e2>-dy:err-=dy;x0+=sx
  if e2<dx:err+=dx;y0+=sy
 return g
