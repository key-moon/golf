def p(g):
 val_o=[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==1]
 val_y0,val_x0=map(min,zip(*val_o));val_y1,val_x1=map(max,zip(*val_o))
 val_u=[(i-val_y0,j-val_x0)for i,j in val_o]
 val_v=[(i-val_y0,j-val_x0)for i in range(val_y0,val_y1+1)for j in range(val_x0,val_x1+1)if g[i][j]==4]
 val_h,val_w=val_y1-val_y0+1,val_x1-val_x0+1
 for val_a in range(len(g)-val_h+1):
  for val_b in range(len(g[0])-val_w+1):
   if all(g[val_a+di][val_b+dj]==4 for di,dj in val_v):
    for di,dj in val_u:g[val_a+di][val_b+dj]=1
 return g
