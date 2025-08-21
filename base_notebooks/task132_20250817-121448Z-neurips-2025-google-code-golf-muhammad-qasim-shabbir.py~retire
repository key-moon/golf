def p(g,F=range):
 E=enumerate
 H,W=len(g),len(g[0])
 a=[[0]*W for _ in F(H)]
 L={v for s in g for v in s if v}
 for c in L:
  m=[i for i,s in E(g)for v in s if v==c]
  S=[j for i,s in E(g)for j,v in E(s)if v==c]
  N,o=min(m),max(m)+1
  D,A=min(S),max(S)+1
  for i in F(N,o):
   for j in F(D,A):a[i][j]=c
 return a