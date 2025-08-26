def p(g):
 val_s=g[5][0]
 val_r=[(i%6,j%6)for i,row in enumerate(g)for j,v in enumerate(row)if v and v!=val_s]
 for val_i in(0,6,12):
  for val_j in(0,6,12):
   for a,b in val_r:
    if g[val_i+a][val_j+b]==0: g[val_i+a][val_j+b]=val_s
 return g
