def p(g):
 val_xl=min(j for j in range(len(g[0]))if any(g[i][j]==2 for i in range(len(g))))
 val_xr=max(j for j in range(len(g[0]))if any(g[i][j]==2 for i in range(len(g))))
 val_yl=min(i for i in range(len(g))    if g[i][val_xl]==2)
 val_yr=min(i for i in range(len(g))    if g[i][val_xr]==2)
 val_s=val_yr-val_yl
 val_z=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==8]
 for val_y,val_x in val_z:
  g[val_y][val_x]=4
  for val_j in range(val_xl,val_x):
   if g[val_y][val_j]==0:g[val_y][val_j]=8
  val_y2=val_y+val_s
  for val_j in range(val_xl,val_xr):
   if g[val_y2][val_j]==0:g[val_y2][val_j]=8
 return g
