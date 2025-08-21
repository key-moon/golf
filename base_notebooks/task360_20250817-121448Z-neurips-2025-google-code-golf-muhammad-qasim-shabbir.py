def p(g):
 w=len(g[0])
 N=next(c for c in range(w)if all(g[r][c]==g[0][c]for r in range(len(g)))and g[0][c]!=0)
 m=[F[:N]for F in g]
 s=[F[N+1:][::-1]for F in g]
 return[[(l if l!=0 else r)for l,r in zip(i,A)]
  for i,A in zip(m,s)]