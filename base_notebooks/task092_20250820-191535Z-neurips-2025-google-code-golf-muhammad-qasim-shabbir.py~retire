def p(g,u=range):
 H=len(g);W=len(g[0]);o=[r[:]for r in g]
 for i in u(H):
  L=C=None
  for j in u(W):
   if g[i][j]:
    if L is not None and g[i][j]==C:
     for k in u(L+1,j):o[i][k]=C
    L=j;C=g[i][j]
 for j in u(W):
  L=C=None
  for i in u(H):
   if g[i][j]:
    if L is not None and g[i][j]==C:
     for k in u(L+1,i):o[k][j]=C
    L=i;C=g[i][j]
 return o