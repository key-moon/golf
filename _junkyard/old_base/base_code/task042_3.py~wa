def p(g):
 m,n=len(g),len(g[0])
 h=list(map(list,zip(*g[::-1])))
 h2=list(map(list,zip(*g)))[::-1]
 for i in range(m):
  for j in range(n):
   if not g[i][j] and h[i][j]==3 and h2[i][j]==3:
    g[i][j]=8
 return g
