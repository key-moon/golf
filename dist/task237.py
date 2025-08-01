def p(d):
 n,m=len(d),len(d[0])
 for i in range(n):
  for j in range(m):
   if f:=d[i][j]:
    for k in range(j,m):d[i][k]=f
    for k in range(i,n):d[k][m-1]=f
 return d