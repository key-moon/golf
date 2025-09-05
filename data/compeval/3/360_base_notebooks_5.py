def p(g):
 w=len(g[0])
 X=next(c for c in range(w)if all(g[r][c]==g[0][c]for r in range(len(g)))and g[0][c]!=0)
 K=[v[:X]for v in g]
 k=[v[X+1:][::-1]for v in g]
 return[[(l if l!=0 else r)for l,r in zip(D,n)]
  for D,n in zip(K,k)]