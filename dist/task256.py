def p(g):
 for a,r in enumerate(g):
  if 2 in r:break
 t=r.count(2)
 for i in range(a):
  for j in range(t+a-i):g[i][j]=3
 for k in range(1,t):
  for j in range(t-k):g[a+k][j]=1
 return g