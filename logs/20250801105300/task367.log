def p(g):
 m,n=len(g),len(g[0])
 s=[(0,j)for j in range(n)if g[0][j]==0]+[(m-1,j)for j in range(n)if g[m-1][j]==0]+[(i,0)for i in range(1,m-1)if g[i][0]==0]+[(i,n-1)for i in range(1,m-1)if g[i][n-1]==0]
 while s:
  i,j=s.pop()
  if g[i][j]==0:
   g[i][j]=6
   if i: s.append((i-1,j))
   if i<m-1: s.append((i+1,j))
   if j: s.append((i,j-1))
   if j<n-1: s.append((i,j+1))
 for i in range(m):
  for j in range(n):
   if g[i][j]==0: g[i][j]=4
   elif g[i][j]==6: g[i][j]=0
 return g