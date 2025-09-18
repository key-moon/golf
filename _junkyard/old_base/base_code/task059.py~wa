def p(g):
 b=[]
 for i in 0,4,8:
  for j in 0,4,8:
   s=c=0
   for x in range(3):
    for y in range(3):
     a=g[i+x][j+y];s+=a;c+=a>0
   b+=[(c,s,i,j)]
 m=max(b)[0]
 for c,s,i,j in b:
  if c==m:
   for x in range(3):
    for y in range(3):
     g[i+x][j+y]=s//c
 return g
