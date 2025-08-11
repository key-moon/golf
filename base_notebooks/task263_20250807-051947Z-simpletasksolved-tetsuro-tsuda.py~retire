def p(g):
 R=range
 b=[[[g[i+r*3][j+c*3]for j in R(3)]for i in R(3)]for r in R(len(g)//3)for c in R(len(g[0])//3)]
 for x in b:
  if[tuple(tuple(y[i][j]==0 for j in R(3))for i in R(3))for y in b].count(tuple(tuple(x[i][j]==0 for j in R(3))for i in R(3)))==1:return x