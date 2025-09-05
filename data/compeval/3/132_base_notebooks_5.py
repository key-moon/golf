def p(g,u=range):
 E=enumerate
 H,W=len(g),len(g[0])
 z=[[0]*W for _ in u(H)]
 t={v for J in g for v in J if v}
 for c in t:
  G=[i for i,J in E(g)for v in J if v==c]
  b=[j for i,J in E(g)for j,v in E(J)if v==c]
  k,o=min(G),max(G)+1
  X,y=min(b),max(b)+1
  for i in u(k,o):
   for j in u(X,y):z[i][j]=c
 return z