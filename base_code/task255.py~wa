def p(g):
 m=0;r,c=len(g),len(g[0]);p=[0]*c
 for i in range(r):
  d=[0]*c
  for j in range(c):
   if not g[i][j]:
    n=1
    if i*j:n=min(p[j],p[j-1],d[j-1])+1
    d[j]=n
    if n>m:m,x,y=n,i,j
  p=d
 for i in range(x-m+1,x+1):g[i][y-m+1:y+1]=[3]*m
 return g
