def p(g):
 R=range
 r=[x[:]for x in g]
 n=len(g)
 for i in R(n):
  x=sum(1for j in R(len(g[0]))if g[i][j]==2)
  if x:
   c=x-1
   for k in R(i+1,n):
    if c<1:break
    for j in R(c):r[k][j]=1
    c-=1
   c=x+1
   for k in R(i-1,-1,-1):
    for j in R(c):r[k][j]=3
    c+=1
 return r