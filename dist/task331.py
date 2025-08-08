A=range
def p(g):
 n=len(g)
 for i in A(n):
  for j in A(n):
   if g[i][j]==1:
    if i:g[i-1][j]=2
    if j:g[i][j-1]=7
    if i+1<n:g[i+1][j]=8
    if j+1<n:g[i][j+1]=6
 return g