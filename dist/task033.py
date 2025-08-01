def p(g):
 D=g[5][0];C=[(i%6,j%6)for i,row in enumerate(g)for j,v in enumerate(row)if v and v!=D]
 for A in(0,6,12):
  for B in(0,6,12):
   for a,b in C:
    if g[A+a][B+b]==0:g[A+a][B+b]=D
 return g