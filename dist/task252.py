A=range
def p(g):
 n,m=len(g),len(g[0])
 for i in A(n):
  for j in A(m):
   if g[i][j]and(i*j<1or not g[i-1][j-1]):
    k=0;x=i;y=j
    while x<n and y<m and g[x][y]:
     if k&1:g[x][y]=4
     k+=1;x+=1;y+=1
 return g