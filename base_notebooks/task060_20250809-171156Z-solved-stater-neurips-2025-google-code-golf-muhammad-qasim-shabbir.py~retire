def p(g):
 w=len(g[0])
 h=int((w-1)/2)
 E=enumerate
 for r,R in E(g):
  if max(R)>0:
   for x in range(h):g[r][x]=g[r][0];g[r][w-x-1]=g[r][w-1]
   g[r][h]=5
 return g