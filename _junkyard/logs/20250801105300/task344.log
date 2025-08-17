def p(g):
 m,n=len(g),len(g[0])
 for i in range(m):
  for j in range(n):
   if g[i][j]==3:
    for a,b in((1,0),(0,1),(-1,0),(0,-1)):
     if 0<=i+a<m and 0<=j+b<n and g[i+a][j+b]==2:
      g[i][j]=8;g[i+a][j+b]=0
 return g