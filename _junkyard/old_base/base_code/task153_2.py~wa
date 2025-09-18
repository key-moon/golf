def p(g):
  val_d={};[val_d.setdefault(val_v,[]).append((val_i,val_j))for val_i,val_r in enumerate(g)for val_j,val_v in enumerate(val_r)if val_v];val_o=[[0]*3for _ in range(3)];
  for val_c in sorted(val_d,key=lambda val_c:min(val_d[val_c])):
    val_l=val_d[val_c];val_e=next(val_e for val_e in val_l if sum(abs(val_e[0]-val_p[0])+abs(val_e[1]-val_p[1])==1 for val_p in val_l)==2);
  for val_x,val_y in val_l:
    val_o[val_x-val_e[0]+1][val_y-val_e[1]+1]=val_c
  return val_o