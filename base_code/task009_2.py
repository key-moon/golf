def p(g):
 val_b=next(r[0]for r in g if r.count(r[0])==len(r)and r[0])
 for val_i,val_r in enumerate(g):
  for val_c in{*val_r}-{0,val_b}:
   val_m=[val_j for val_j,val_v in enumerate(val_r)if val_v==val_c];val_x,val_y=min(val_m),max(val_m)
   for val_j in range(val_x,val_y+1):val_r[val_j]=val_c
 return g
