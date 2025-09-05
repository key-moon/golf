def p(g,D=range):
 E=enumerate
 H,W=len(g),len(g[0])
 L=[[0]*W for _ in D(H)]
 A={v for J in g for v in J if v}
 for c in A:
  b=[i for i,J in E(g)for v in J if v==c]
  F=[j for i,J in E(g)for j,v in E(J)if v==c]
  e,z=min(b),max(b)+1
  U,o=min(F),max(F)+1
  for i in D(e,z):
   for j in D(U,o):L[i][j]=c
 return L