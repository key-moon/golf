def p(g):
 val_n=len(g)
 for val_i in range(val_n):
  for val_j in range(val_n):
   val_v=g[val_i][val_j]
   if val_v>1:
    for val_i2 in range(val_i+1,val_n):
     if g[val_i2][val_j]==val_v:g[(val_i+val_i2)>>1][val_j]=val_v
    for val_j2 in range(val_j+1,val_n):
     if g[val_i][val_j2]==val_v:g[val_i][(val_j+val_j2)>>1]=val_v
 return g
