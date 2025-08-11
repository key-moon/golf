def p(g):
 val_h,val_w=len(g),len(g[0])
 val_b=[(0,c)for c in range(val_w)]+[(r,val_w-1)for r in range(1,val_h)]+[(val_h-1,c)for c in range(val_w-2,-1,-1)]+[(r,0)for r in range(val_h-2,0,-1)]
 val_a=[(r,c,g[r][c])for r,c in val_b if g[r][c]]
 for val_c1,val_c2 in zip(val_a,val_a[1:]+val_a[:1]):
  val_x1,val_y1,val_v1=val_c1;val_x2,val_y2,val_v2=val_c2;val_L=abs(val_x1-val_x2)+abs(val_y1-val_y2)
  for val_i in range(val_h):
   for val_j in range(val_w):
    val_d=abs(val_i-val_x1)+abs(val_j-val_y1)
    if val_d<=val_L and val_d%2==0:g[val_i][val_j]=val_v1
    else:
     val_d=abs(val_i-val_x2)+abs(val_j-val_y2)
     if val_d<=val_L and val_d%2==0:g[val_i][val_j]=val_v2
 return g
