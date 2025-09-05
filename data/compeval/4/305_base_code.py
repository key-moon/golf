def p(g):
 k = max(map(max, g))
 for i, r in enumerate(g):
  for j, _ in enumerate(r):
   r[j] = (i + j) % k + 1
 return g
