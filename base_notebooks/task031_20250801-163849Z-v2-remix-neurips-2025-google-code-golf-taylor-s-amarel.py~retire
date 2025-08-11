def p(g):
 c=[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x]
 if c:
  y0=min(i for i,j in c);y1=max(i for i,j in c)
  x0=min(j for i,j in c);x1=max(j for i,j in c)
  return[g[i][x0:x1+1]for i in range(y0,y1+1)]
 return g