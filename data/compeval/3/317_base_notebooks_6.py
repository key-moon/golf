def p(X,k=range):
 n=len(X)
 g=[[0 for _ in k(n)]for _ in k(n)]
 for i in k(n):
  for j in k(n):
   if X[i][j]==5:
    for x in k(max(0,i-1),min(n,i+2)):
     for y in k(max(0,j-1),min(n,j+2)):g[x][y]=1
 return g