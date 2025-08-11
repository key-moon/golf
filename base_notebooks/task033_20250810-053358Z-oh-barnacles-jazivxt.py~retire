def p(g):
 q=range
 r=[o[:]for o in g]
 x=g[5][0]
 b=[[g[i+1][j+1]for j in q(3)]for i in q(3)]
 for p in[(0,6),(0,12),(6,0),(6,6),(6,12),(12,0),(12,6),(12,12)]:
  for i in q(3):
   for j in q(3):
    y,z=p[0]+i+1,p[1]+j+1
    r[y][z]=g[y][z]if b[i][j]==g[y][z]else(x if b[i][j]else 0)
 return r
