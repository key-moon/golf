def p(g):
 val_m=max(map(max,g));val_n=len(g)
 for val_i in range(val_n):
  for val_j in range(val_n):
   if g[val_i][val_j]==val_m:g[val_i][val_j]=g[val_j][val_i]
 return g
