A=range
def p(g):
 for(a,r)in enumerate(g):
  if 2 in r:break
 t=r.count(2)
 for i in A(a):
  for j in A(t+a-i):g[i][j]=3
 for k in A(1,t):
  for j in A(t-k):g[a+k][j]=1
 return g