def p(g):
 val_n=len(g);val_m=max(max(val_r)for val_r in g);val_o=[[0]*val_n*val_n for _ in range(val_n*val_n)]
 for val_i,val_r in enumerate(g):
  for val_j,val_v in enumerate(val_r):
   if val_v==val_m==2:
    for val_di,val_rr in enumerate(g):
     for val_dj,val_c in enumerate(val_rr):val_o[val_i*val_n+val_di][val_j*val_n+val_dj]=val_c
 return val_o
