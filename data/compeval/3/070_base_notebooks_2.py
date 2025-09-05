def p(g):
 q=range
 r=[o[:]for o in g]
 p=[(i,j)for i in q(len(g))for j in q(len(g[0]))if g[i][j]==8]
 if p:
  t,b=min(i for i,j in p),max(i for i,j in p)
  l,s=min(j for i,j in p),max(j for i,j in p)
  for i in q(t,b+1):
   for j in q(l,s+1):
    if g[i][j]==1:r[i][j]=3
 return r
