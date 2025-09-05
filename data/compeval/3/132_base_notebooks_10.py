def p(g,k=range):
 E=enumerate
 H,W=len(g),len(g[0])
 b=[[0]*W for _ in k(H)]
 s={v for m in g for v in m if v}
 for c in s:
  K=[i for i,m in E(g)for v in m if v==c]
  A=[j for i,m in E(g)for j,v in E(m)if v==c]
  D,n=min(K),max(K)+1
  B,X=min(A),max(A)+1
  for i in k(D,n):
   for j in k(B,X):b[i][j]=c
 return b