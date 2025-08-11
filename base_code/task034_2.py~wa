def p(g):
 val_n=len(g)
 for val_i in range(val_n):
  for val_j in range(val_n):
   if g[val_i][val_j]==2:
    val_vs=[(k,l)for k,l in((1,0),(-1,0),(0,1),(0,-1))
           if 0<=val_i+k<val_n and 0<=val_j+l<val_n and g[val_i+k][val_j+l]>2]
    val_v1,val_v2=val_vs
    val_d=(-val_v1[0]-val_v2[0],-val_v1[1]-val_v2[1])
    val_c=g[val_i+val_v1[0]][val_j+val_v1[1]]
    val_t=0
    while 1:
     for a,b in (val_v1,val_v2,(val_v1[0]+val_v2[0],val_v1[1]+val_v2[1])):
      x=val_i+a+val_t*val_d[0];y=val_j+b+val_t*val_d[1]
      if x<0 or x>=val_n or y<0 or y>=val_n:return g
      g[x][y]=val_c
     val_t+=1
