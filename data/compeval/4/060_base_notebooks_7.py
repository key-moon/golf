def p(g):
 q=range
 r=[row[:]for row in g]
 for i in q(5):
  if g[i][0]:
   for j in q(5):r[i][j]=g[i][0]
   r[i][5]=5
  if g[i][10]:
   for j in q(6,11):r[i][j]=g[i][10]
 return r