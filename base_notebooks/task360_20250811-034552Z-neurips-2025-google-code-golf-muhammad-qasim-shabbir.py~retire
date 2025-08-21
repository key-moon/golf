def p(g):
 w=len(g[0])
 o=next(c for c in range(w)if all(g[r][c]==g[0][c]for r in range(len(g)))and g[0][c]!=0)
 v=[L[:o]for L in g]
 E=[L[o+1:][::-1]for L in g]
 return[[(l if l!=0 else r)for l,r in zip(D,b)]
  for D,b in zip(v,E)]