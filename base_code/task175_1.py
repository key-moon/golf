def p(g):
 val_n,val_m=len(g),len(g[0])
 for val_i in range(val_n):
  for val_j in range(val_m):
   if g[val_i][val_j]==0:
    g[val_i][val_j]=g[val_i][val_j-1] or g[val_i][val_j+1] or g[val_i-1][val_j] or g[val_i+1][val_j]
 return g
