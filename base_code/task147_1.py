def p(val_g):
 val_h,val_w=len(val_g),len(val_g[0])
 for val_i in range(val_h):
  for val_j in range(val_w):
   if val_g[val_i][val_j]==3 and((val_i and val_g[val_i-1][val_j]==3)or(val_i<val_h-1 and val_g[val_i+1][val_j]==3)or(val_j and val_g[val_i][val_j-1]==3)or(val_j<val_w-1 and val_g[val_i][val_j+1]==3)):val_g[val_i][val_j]=8
 return val_g
