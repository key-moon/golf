def p(g,u=range):
 E=enumerate
 H,W=len(g),len(g[0])
 B=[[0]*W for _ in u(H)]
 J={v for f in g for v in f if v}
 for c in J:
  s=[i for i,f in E(g)for v in f if v==c]
  Q=[j for i,f in E(g)for j,v in E(f)if v==c]
  Y,R=min(s),max(s)+1
  e,T=min(Q),max(Q)+1
  for i in u(Y,R):
   for j in u(e,T):B[i][j]=c
 return B