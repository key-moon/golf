def p(g):
 for val_i in range(len(g)):
  for val_j in range(len(g[0])):
   if g[val_i][val_j]==5:
    val_r=val_i
    while val_r+1<len(g) and g[val_r+1][val_j]==5: val_r+=1
    val_c=val_j
    while val_c+1<len(g[0]) and g[val_i][val_c+1]==5: val_c+=1
    for val_y in range(val_i,val_r+1):
     for val_x in range(val_j,val_c+1):
      if g[val_y][val_x]==5:
       g[val_y][val_x]=1 if (val_y in(val_i,val_r) and val_x in(val_j,val_c)) else \
                         4 if (val_y in(val_i,val_r) or val_x in(val_j,val_c)) else 2
 return g
