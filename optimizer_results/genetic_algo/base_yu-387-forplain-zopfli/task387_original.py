A=range
def p(g):
 u=[s[:]for s in g]
 for _ in A(2):
  for i in A(len(g)):
   if a:=[j for j in A(len(g[i]))if g[i][j]]:
    j,k=a
    for t in A(j-1,j+2):u[i-1][t]=u[i+1][t]=g[i][k]
    for t in A(k-1,k+2):u[i-1][t]=u[i+1][t]=g[i][j]
    for t in A(j+2,k-1):u[i][t]=min(t-j-1,k-1-t)%2*5
  *g,=zip(*g);*u,=map(list,zip(*u))
 return u