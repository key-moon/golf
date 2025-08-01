def p(val_g):
 val_r,val_c=len(val_g),len(val_g[0])
 for val_i in range(val_r):
  val_js=[val_j for val_j in range(val_c) if val_g[val_i][val_j]==2]
  if val_js[1:]:
   a,b=val_js[0],val_js[-1]
   for val_j in range(a+1,b):
    if val_g[val_i][val_j]!=2:val_g[val_i][val_j]=8
 for val_j in range(val_c):
  val_is=[val_i for val_i in range(val_r) if val_g[val_i][val_j]==2]
  if val_is[1:]:
   a,b=val_is[0],val_is[-1]
   if a>0:val_g[a-1][val_j]=8
   if b<val_r-1:val_g[b+1][val_j]=8
 return val_g
