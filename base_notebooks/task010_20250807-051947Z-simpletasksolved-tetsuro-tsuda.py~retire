def p(g):
 h=[(sum(r[c]==5for r in g),c)for c in range(len(g[0]))if any(r[c]==5for r in g)]
 h.sort(reverse=True)
 r=[r[:]for r in g]
 for k,(n,c)in enumerate(h):
  for i in range(len(g)):
   if g[i][c]==5:r[i][c]=k+1
 return r
