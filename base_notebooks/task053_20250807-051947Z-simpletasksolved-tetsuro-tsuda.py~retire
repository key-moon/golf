def p(g):
 h, w = len(g), len(g[0])
 res = [[0]*w for _ in range(h)]
 for i in range(h):
  for j in range(w):
   src_i, src_j = (i - -2) % h, (j - -3) % w
   res[i][j] = g[src_i][src_j]
 return res
