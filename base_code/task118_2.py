def p(g):
 val_r,val_c=len(g),len(g[0])
 for val_i in range(val_r):
  val_js=[val_j for val_j in range(val_c) if g[val_i][val_j]==2]
  if val_js[1:]:
   a,b=val_js[0],val_js[-1]
   for val_j in range(a+1,b):
    if g[val_i][val_j]!=2:g[val_i][val_j]=8
 for val_j in range(val_c):
  val_is=[val_i for val_i in range(val_r) if g[val_i][val_j]==2]
  if val_is[1:]:
   a,b=val_is[0],val_is[-1]
   if a>0:g[a-1][val_j]=8
   if b<val_r-1:g[b+1][val_j]=8
 return g
