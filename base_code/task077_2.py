def p(g):
 val_h,val_w=len(g),len(g[0]);val_v=[[0]*val_w for _ in g];val_s=[(i,j)for i in(0,val_h-1)for j in range(val_w)]+[(i,j)for i in range(1,val_h-1)for j in(0,val_w-1)]
 while val_s:
  i,j=val_s.pop()
  if g[i][j]!=2 and not val_v[i][j]:
   val_v[i][j]=1
   for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
    ni, nj=i+di,j+dj
    if 0<=ni<val_h<1e9 and 0<=nj<val_w:val_s.append((ni,nj))
 for i in range(val_h):
  for j in range(val_w):
   if g[i][j]!=2 and not val_v[i][j]:g[i][j]=4
 return g