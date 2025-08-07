def p(g):
 val_h=len(g)
 val_w=len(g[0])
 val_seen=[[0]*val_w for _ in range(val_h)]
 val_best=[]
 for val_i in range(val_h):
  for val_j in range(val_w):
   if g[val_i][val_j]==2 and not val_seen[val_i][val_j]:
    val_cl=[(val_i,val_j)];val_seen[val_i][val_j]=1;val_Q=[(val_i,val_j)]
    while val_Q:
     val_x,val_y=val_Q.pop()
     for val_dx,val_dy in((1,0),(-1,0),(0,1),(0,-1)):
      val_nx,val_ny=val_x+val_dx,val_y+val_dy
      if 0<=val_nx<val_h and 0<=val_ny<val_w and g[val_nx][val_ny]==2 and not val_seen[val_nx][val_ny]:
       val_seen[val_nx][val_ny]=1;val_Q.append((val_nx,val_ny));val_cl.append((val_nx,val_ny))
    if len(val_cl)>len(val_best):val_best=val_cl
 val_S=max(i for i,row in enumerate(g) if 1 in row)
 val_rs=max(i for i,_ in val_best)
 val_dr=val_S+1-val_rs
 for val_i,val_j in val_best:g[val_i][val_j]=0
 for val_i,val_j in val_best:
  if g[val_i+val_dr][val_j]==0:g[val_i+val_dr][val_j]=2
 return g
