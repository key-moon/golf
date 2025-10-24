B=len
A=range
def p(g):
 for _ in A(2):
  for i in A(B(g)):
   if B(a:=[j for j in A(B(g[i]))if g[i][j]%5])==2:
    j,k=a
    for t in A(i-1,i+2):*g[t],=g[t];g[t][j-1]=g[t][j+1]=g[i][k];g[t][k-1]=g[t][k+1]=g[i][j]
    for t in A(j+2,k-1):g[i][t]=min(t-j-1,k-1-t)%2*5
  *g,=zip(*g)
 return g