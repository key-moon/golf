def p(g):
 r=[o[:]for o in g]
 n,m=len(g),len(g[0])
 for j in range(m):
  if g[0][j]:
   for i in range(n):
    if i%2==0:r[i][j]=g[0][j]
    else:
     if j>0:r[i][j-1]=g[0][j]
     if j<m-1:r[i][j+1]=g[0][j]
 return r