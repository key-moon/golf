def p(m):
 n=3;v=[]
 for c in zip(*m):
  for x in c:
   if x:v+=[x];break
 v+=[0]*(n*n-len(v))
 return[v[i*n:i*n+n][::1-2*(i%2)]for i in range(n)]
