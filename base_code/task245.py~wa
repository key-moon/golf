def p(g):
 a=len(g);b=0;e=len(g[0]);f=0
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==3:
    a=min(a,i);b=max(b,i);e=min(e,j);f=max(f,j)
 S=[r[e:f+1]for r in g[a:b+1]]
 T=zip(*S[::-1])
 for i in range(a,b+1):
  for j in range(e,f+1):
   if g[i][j]^3:g[i][j]=T[i-a][j-e]
 return g
