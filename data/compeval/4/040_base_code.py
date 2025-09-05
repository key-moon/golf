def p(g):
 n=len(g);b=n-1;a=len(set(g[0]))==1
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==3:
    r[j]=(
     g[0][j] if i<b-i else g[-1][j]
    ) if a else (
     r[0]   if j<b-j else r[-1]
    )
 return g
