def p(g):
 q=range;r=[x[:]for x in g];n,m=len(g),len(g[0])
 for i in q(1,n,4):
  for j in q(1,m,4):
   v=g[i][j]+5
   for x in q(3):
    for y in q(3):r[i-1+x][j-1+y]=v
 return r