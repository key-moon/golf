def p(g):
 o=[r[:]for r in g];R,C=len(g),len(g[0]);G={(r,c)for r in range(R)for c in range(C)if g[r][c]==3};U=set()
 for m in[3,2,1]:
  for r in range(R):
   for c in range(C):
    for f in[0,1]:
     c1,c2,c0,c3=(c+m,c,c-m,c+2*m)if f else(c,c+m,c+2*m,c-m);E=set()
     for d in range(m):
      for e in range(m):
       if 0<=r+d<R and 0<=c1+e<C:E.add((r+d,c1+e))
       if 0<=r+d+m<R and 0<=c2+e<C:E.add((r+d+m,c2+e))
     if len(E)==2*m*m and E<=G and not E&U:
      U|=E
      for d in range(m):
       for e in range(m):
        if 0<=r+d-m<R and 0<=c0+e<C:o[r+d-m][c0+e]=8
        if 0<=r+d+2*m<R and 0<=c3+e<C:o[r+d+2*m][c3+e]=8
 return o
