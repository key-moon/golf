def p(val_g):
 m,n=len(val_g),len(val_g[0])
 h=list(map(list,zip(*val_g[::-1])))
 h2=list(map(list,zip(*val_g)))[::-1]
 for i in range(m):
  for j in range(n):
   if not val_g[i][j] and h[i][j]==3 and h2[i][j]==3:
    val_g[i][j]=8
 return val_g
