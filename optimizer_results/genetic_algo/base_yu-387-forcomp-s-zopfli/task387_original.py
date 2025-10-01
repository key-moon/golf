def p(g):
 u=[s[:]for s in g]
 for _ in range(2):
  for i in range(len(g)):
   if a:=[j for j in range(len(g[i]))if g[i][j]]:
    j,k=a
    for t in range(j-1,j+2):u[i-1][t]=u[i+1][t]=g[i][k]
    for t in range(k-1,k+2):u[i-1][t]=u[i+1][t]=g[i][j]
    for t in range(j+2,k-1):u[i][t]=min(t-j-1,k-1-t)%2*5
  *g,=zip(*g);*u,=map(list,zip(*u))
 return u