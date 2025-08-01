def p(g):
 n=len(g)
 for i,a in enumerate(g):
  for j,v in enumerate(a):
   if v==3:a[j]=g[(0,-1)[i>=n-1-i]][j]
 return g