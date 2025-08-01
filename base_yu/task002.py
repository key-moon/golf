def p(g):
 h,w=len(g),len(g[0])
 for r in range(w):
  for d in range(h):
   for l in range(r):
    for u in range(d):
     if set(g[d][l:r]+g[u-1][l:r]+[g[i][l] for i in range(u,d)]+[g[i][r-1] for i in range(u,d)])=={1}:
      for i in range(u,d):
       g[i][l:r]=[4]*(r-l)
 return g
