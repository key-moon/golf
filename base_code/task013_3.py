def p(g):
 val_h,val_w=len(g),len(g[0]);val_P=[(i,j,g[i][j])for i in range(val_h)for j in range(val_w)if g[i][j]];val_r0,val_c0,val_v0=val_P[0];val_r1,val_c1,val_v1=val_P[1];val_dx,val_dy=abs(val_c1-val_c0),abs(val_r1-val_r0);val_f=val_dx==0 or val_dx>val_dy
 if val_f:g=list(map(list,zip(*g)));val_r0,val_c0,val_r1,val_c1=val_c0,val_r0,val_c1,val_r1;val_h,val_w=val_w,val_h;val_dx=val_dy
 val_res=[[0]*val_w for _ in range(val_h)];val_t=[val_v0,val_v1]
 for val_k,val_x in enumerate(range(val_c0,val_w,val_dx)):
  for val_y in range(val_h):val_res[val_y][val_x]=val_t[val_k&1]
 return list(map(list,zip(*val_res)))if val_f else val_res
