def p(g):
 val_n=len(g)
 for val_i in range(val_n):
  for val_j in range(val_n):
   if g[val_i][val_j]!=5:
    # find block origin by integer‐dividing by 4 (3 cells + 1 separator)
    g[val_i][val_j]=g[val_i//4*4][val_j//4*4]
 return g
