def p(g,R=range,E=enumerate):
 H=len(g);W=len(g[0]);a=[[0]*W for _ in R(H)];r={v for G in g for v in G if v}
 for c in r:
  I=[i for i,G in E(g)for v in G if v==c];L=[j for i,G in E(g)for j,v in E(G)if v==c];C,D=min(I),max(I)+1;b,V=min(L),max(L)+1
  for i in R(C,D):
   for j in R(b,V):a[i][j]=c
 return a