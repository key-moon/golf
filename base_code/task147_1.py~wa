def p(g):
 val_h,val_w=len(g),len(g[0])
 for val_i in range(val_h):
  for val_j in range(val_w):
   if g[val_i][val_j]==3 and((val_i and g[val_i-1][val_j]==3)or(val_i<val_h-1 and g[val_i+1][val_j]==3)or(val_j and g[val_i][val_j-1]==3)or(val_j<val_w-1 and g[val_i][val_j+1]==3)):g[val_i][val_j]=8
 return g
