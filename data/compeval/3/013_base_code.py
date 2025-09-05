def p(g):
 val_h,val_w=len(g),len(g[0]);val_p=[(y,x,g[y][x])for y in range(val_h)for x in range(val_w)if g[y][x]]
 (y1,x1,v1),(y2,x2,v2)=val_p
 val_o=val_w>val_h
 val_L=(sorted([(x1,v1),(x2,v2)])if val_o else sorted([(y1,v1),(y2,v2)]))
 val_s,val_v=val_L[0];val_t,val_u=val_L[1];val_d=val_t-val_s;val_k=0
 while val_s+val_k*val_d<(val_w if val_o else val_h):
  val_c=val_s+val_k*val_d;val_f=val_v if val_k%2<1 else val_u
  for _ in range(val_h*val_o+val_w*(1-val_o)):
   g[val_o*_+(1-val_o)*val_c][val_o*val_c+(1-val_o)*_]=val_f
  val_k+=1
 return g
