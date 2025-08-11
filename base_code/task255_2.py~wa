def p(g):
 val_h,val_w=len(g),len(g[0])
 val_s=[(i,j)for i in(0,val_h-1)for j in range(val_w)if g[i][j]==0]+[(i,j)for i in range(val_h)for j in(0,val_w-1)if g[i][j]==0]
 while val_s:
  y,x=val_s.pop()
  if g[y][x]==0:
   g[y][x]=-1
   if y:val_s+=[(y-1,x)]
   if y<val_h-1:val_s+=[(y+1,x)]
   if x:val_s+=[(y,x-1)]
   if x<val_w-1:val_s+=[(y,x+1)]
 for y in range(val_h):
  for x in range(val_w):
   if g[y][x]==0:g[y][x]=3
   elif g[y][x]<0:g[y][x]=0
 return g
