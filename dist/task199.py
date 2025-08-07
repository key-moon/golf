B=range
A=enumerate
def p(g):
 r,c=next((i,j)for(i,B)in A(g)for(j,x)in A(B)if x);v=g[r][c]
 for i in B(r+1):
  for j in B(len(g[0])):
   if j&1==c&1:g[i][j]=4
 g[r+1][c]=v;return g