def p(g):
 r=len(g)-1;v=next(z for z in g[r] if z and z not in g[r-1]);c=[i for i,z in enumerate(g[r]) if z==v];x,y=c[0],c[-1];w=len(g[0])
 for k in range(1,r):
  rr=r-k-1;i=x-k
  if i>=0:g[rr][i]=v
  j=y+k
  if j<w:g[rr][j]=v
 return g
