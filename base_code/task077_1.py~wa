def p(g):
 val_o=[val_r[:]for val_r in g];val_h,val_w=len(val_o),len(val_o[0])
 for val_y in range(val_h):
  for val_x in range(val_w):
   if val_o[val_y][val_x]==2:
    for val_dx,val_dy in((1,0),(-1,0),(0,1),(0,-1)):
     val_i,val_j=val_x+val_dx,val_y+val_dy
     if 0<=val_i<val_w and 0<=val_j<val_h:
      val_c=val_o[val_j][val_i]
      if val_c and val_c-2:
       while 0<=val_i<val_w and 0<=val_j<val_h and val_o[val_j][val_i]==val_c:
        g[val_j][val_i]=4
        val_i+=val_dx;val_j+=val_dy
 return g
