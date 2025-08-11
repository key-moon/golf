def p(g):
 val_h,val_w=len(g),len(g[0])
 val_o=[[0]*val_w for _ in g]
 val_v=[[0]*val_w for _ in g]
 for val_i in range(val_h):
  for val_j in range(val_w):
   if g[val_i][val_j]==2 and not val_v[val_i][val_j]:
    val_f=[(val_i,val_j)];val_v[val_i][val_j]=1
    for val_a,val_b in val_f:
     for val_dx,val_dy in((1,0),(-1,0),(0,1),(0,-1)):
      val_x,val_y=val_a+val_dx,val_b+val_dy
      if 0<=val_x<val_h and 0<=val_y<val_w and g[val_x][val_y]==2 and not val_v[val_x][val_y]:
       val_v[val_x][val_y]=1;val_f.append((val_x,val_y))
    val_rs=[val_p[0]for val_p in val_f];val_cs=[val_p[1]for val_p in val_f]
    val_mn,val_mx,val_minc,val_maxc=min(val_rs),max(val_rs),min(val_cs),max(val_cs)
    if val_mx-val_mn>1 and val_maxc-val_minc>1 and all(g[val_mn][val_k]==2 for val_k in range(val_minc,val_maxc+1)) and all(g[val_mx][val_k]==2 for val_k in range(val_minc,val_maxc+1)) and all(g[val_k][val_minc]==2 for val_k in range(val_mn,val_mx+1)) and all(g[val_k][val_maxc]==2 for val_k in range(val_mn,val_mx+1)):
     for val_x in range(val_mn+1,val_mx):
      for val_y in range(val_minc+1,val_maxc):
       val_o[val_x][val_y]=3
 return val_o
