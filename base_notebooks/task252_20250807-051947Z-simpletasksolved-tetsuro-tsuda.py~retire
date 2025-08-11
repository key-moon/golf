def p(g):
 r=[x[:]for x in g]
 n,m=len(g),len(g[0])
 for j in range(m):
  if g[0][j]:
   i,j=1,j+1
   while i<n and j<m:
    r[i][j]=4
    i+=2
    j+=2
 for i in range(1,n):
  if g[i][0]:
   i,j=i+1,1
   while i<n and j<m:
    r[i][j]=4
    i+=2
    j+=2
 return r