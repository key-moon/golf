def p(g):
 b=max({x:sum(r.count(x)for r in g)for x in sum(g,[])}.items(),key=lambda x:x[1])[0];v=[[0]*15for _ in range(5)];c=[]
 for i in range(5):
  for j in range(15):
   if not v[i][j]and g[i][j]!=b:
    s=[(i,j)];o=[]
    while s:
     x,y=s.pop()
     if 5>x>=0<=y<15and not v[x][y]and g[x][y]!=b:v[x][y]=1;o+=[(x,y)];s+=[(x+dx,y+dy)for dx,dy in[(0,1),(0,-1),(1,0),(-1,0)]]
    if o:c.append({(g[r][c],(r,c))for r,c in o})
 f=c[0];mr,mc=min(p[0]for _,p in f),min(p[1]for _,p in f);n={(v,(p[0]-mr,p[1]-mc))for v,p in f};w=max(p[1]for _,p in n)+1;p=next((d for d in range(1,w)if {(v,(x,y-d))for v,(x,y)in n if y-d>=0}.issubset(n)),w)
 for v,(x,y)in f:
  t=p
  while y+t<15:g[x][y+t]=v;t+=p
 return g