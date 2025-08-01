def p(g):
 for val_r in g:
  if 2 in val_r:
   val_a=val_r.index(2);val_b=len(val_r)-val_r[::-1].index(2)-1
   for val_j in range(val_a+1,val_b):
    if val_r[val_j]!=2:val_r[val_j]=8
 return g
