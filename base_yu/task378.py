def p(g):
 n=len(g)
 u=[s[:] for s in g]
 for i in range(1,n-1):
  for j in range(1,n-1):
   s=[g[i+k%3-1][j+k//3-1]for k in range(9)]
   if len({*s[1::2]})<len({*s}) == 3:
    u[i][j] = 9
 return u
