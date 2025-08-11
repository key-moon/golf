def p(g):
 w=len(g[0])
 X=next(c for c in range(w)if all(g[r][c]==g[0][c]for r in range(len(g)))and g[0][c]!=0)
 b=[y[:X]for y in g]
 v=[y[X+1:][::-1]for y in g]
 return[[(l if l!=0 else r)for l,r in zip(j,u)]
  for j,u in zip(b,v)]