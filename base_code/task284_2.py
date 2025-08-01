def p(g):
  val_p=[(i,j,g[i][j])for i in range(len(g))for j in range(len(g[0]))if g[i][j]];(val_r,val_c,val_v),(val_R,val_C,val_V)=val_p;val_dr=(val_R>val_r)-(val_R<val_r);val_dc=(val_C>val_c)-(val_C<val_c);val_k=(abs(val_R-val_r)+abs(val_C-val_c))//2;val_er,val_ec=val_r+val_dr*val_k,val_c+val_dc*val_k;val_Er,val_Ec=val_R-val_dr*val_k,val_C-val_dc*val_k
  for val_t in range(val_k+1):
    g[val_r+val_dr*val_t][val_c+val_dc*val_t]=val_v;g[val_R-val_dr*val_t][val_C-val_dc*val_t]=val_V
  val_px,val_py=(0,1)if val_dr else(1,0)
  for val_i in range(-2,3):g[val_er+val_px*val_i][val_ec+val_py*val_i]=val_v;g[val_Er+val_px*val_i][val_Ec+val_py*val_i]=val_V
  return g
