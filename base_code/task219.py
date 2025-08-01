def p(g):
 m=max(r.count(8)for r in g)
 ps=[i for i,r in enumerate(g)if r.count(8)==m]
 for y,r in enumerate(g):
  if any(v==8 for v in r):
   p=ps[y%2]if len(ps)>1 else ps[0]
   if y>p:
    for x,v in enumerate(r):
     if v==0 and g[p][x]==8:r[x]=1
 return g