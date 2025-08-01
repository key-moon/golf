def p(g):
 AD=g[5][0];AC=[(i%6,j%6)for i,row in enumerate(g)for j,v in enumerate(row)if v and v!=AD]
 for AA in(0,6,12):
  for AB in(0,6,12):
   for a,b in AC:
    if g[AA+a][AB+b]==0:g[AA+a][AB+b]=AD
 return g