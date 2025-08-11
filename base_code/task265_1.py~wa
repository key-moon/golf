def p(g):
 for val_i in range(len(g)-1):
  for val_j in range(len(g[0])-1):
   if not g[val_i][val_j] and not g[val_i][val_j+1] and not g[val_i+1][val_j] and not g[val_i+1][val_j+1]:
    g[val_i][val_j]=g[val_i][val_j+1]=g[val_i+1][val_j]=g[val_i+1][val_j+1]=2
 return g
