def p(g):
 w=len(g[0])
 T=next(c for c in range(w)if all(g[r][c]==g[0][c]for r in range(len(g)))and g[0][c]!=0)
 u=[Q[:T]for Q in g]
 s=[Q[T+1:][::-1]for Q in g]
 return[[(l if l!=0 else r)for l,r in zip(R,e)]
  for R,e in zip(u,s)]