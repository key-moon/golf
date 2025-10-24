def g(i,a,u,e,n,h):
 for r in range(u,n+1):
  for e in range(a,e+1):i[r][e]=h
def t(i,a,u,e,n):g(i,a,u,e,n,4);g(i,a+1,u+1,e-1,n-1,2);i[u][a]=i[u][e]=i[n][a]=i[n][e]=1
def p(i):
 f,e=len(i),len(i[0])
 for h in range(f*e):
  a,n=h%e,h//e
  if i[n][a]==5:
   u,r=a,n
   while u<e-1and i[r][u+1]==5:u+=1
   while r<f-1and i[r+1][u]==5:r+=1
   t(i,a,n,u,r)
 return i