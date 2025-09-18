def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:d.setdefault(v,[]).append((i,j))
 for v,p in d.items():
  (a0,a1),(b0,b1)=p
  for i in range(min(a0,b0),max(a0,b0)+1):
   for j in range(min(a1,b1),max(a1,b1)+1):
    if g[i][j]==0 and (i==a0 or i==b0 or j==a1 or j==b1):g[i][j]=v
 return g
