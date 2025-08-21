def p(E,v=range):
 n=len(E)
 D=[[0 for _ in v(n)]for _ in v(n)]
 for i in v(n):
  for j in v(n):
   if E[i][j]==5:
    for x in v(max(0,i-1),min(n,i+2)):
     for y in v(max(0,j-1),min(n,j+2)):D[x][y]=1
 return D