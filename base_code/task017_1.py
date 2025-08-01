def p(g):
 n,m=len(g),len(g[0])
 for H in range(1,n+1):
  if all(not g[i][j] or g[i][j]==g[i%H][j]for i in range(n)for j in range(m)):break
 for W in range(1,m+1):
  if all(not g[i][j] or g[i][j]==g[i][j%W]for i in range(n)for j in range(m)):break
 for i in range(n):
  for j in range(m):
   if not g[i][j]:g[i][j]=g[i%H][j%W]
 return g
