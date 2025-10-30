C=any
B=len
A=range
def p(g):
 for _ in A(8):
  for i in A(B(g)-1):
   for j in A(B(g)-1):
    if 3<B({g[i][j],g[i+1][j],g[i][j+1],g[i+1][j+1]}):u=[(i,j)];u=[(a,b)for a in A(B(g))for b in A(B(g))if g[a][b]==g[i][j]>0if C((y-a)*(y-a)+(x-b)*(x-b)<3for(y,x)in u)];u=[(a,b)for a in A(B(g))for b in A(B(g))if g[a][b]==g[i][j]>0if C((y-a)*(y-a)+(x-b)*(x-b)<3for(y,x)in u)];u=[(a,b)for a in A(B(g))for b in A(B(g))if g[a][b]==g[i][j]>0if C((y-a)*(y-a)+(x-b)*(x-b)<3for(y,x)in u)];u=[(a,b)for a in A(B(g))for b in A(B(g))if g[a][b]==g[i][j]>0if C((y-a)*(y-a)+(x-b)*(x-b)<3for(y,x)in u)];g=[[g[a][b]|((a,2*j+1-b)in u)*g[i][j+1]|((2*i+1-a,b)in u)*g[i+1][j]for b in A(B(g))]for a in A(B(g))]
  g[::-1]=zip(*g)
 return g