def p(g):
 q=range
 r=[o[:]for o in g]
 a=[[g[i][j]for j in q(3)]for i in q(3)]
 for i in q(9):
  for j in q(4,13):
   if g[i][j]==1:
    for e in q(-1,2):
     for f in q(-1,2):
      if 0<=i+e<9 and 4<=j+f<13:
       r[i+e][j+f]=a[e+1][f+1]
 return r
