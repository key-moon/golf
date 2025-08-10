def p(g):
 r,c=len(g),len(g[0])
 for i in range(r-1):
  for j in range(c-1):
   if g[i][j]==g[i][j+1]==g[i+1][j]==g[i+1][j+1]==5:
    if i>0 and j>0:g[i-1][j-1]=1
    if i>0 and j+2<c:g[i-1][j+2]=2
    if i+2<r and j>0:g[i+2][j-1]=3
    if i+2<r and j+2<c:g[i+2][j+2]=4
 return g
