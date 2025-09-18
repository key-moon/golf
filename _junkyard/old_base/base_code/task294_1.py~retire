def p(g):
 val_m,val_n=len(g),len(g[0])
 for val_i in range(val_m):
  for val_j in range(val_n):
   if g[val_i][val_j]==5 and (val_i==0 or g[val_i-1][val_j]!=5) and (val_j==0 or g[val_i][val_j-1]!=5):
    val_h=1
    while val_i+val_h<val_m and g[val_i+val_h][val_j]==5: val_h+=1
    val_w=1
    while val_j+val_w<val_n and g[val_i][val_j+val_w]==5: val_w+=1
    for val_r in range(val_i+1, val_i+val_h-1):
     for val_c in range(val_j+1, val_j+val_w-1):
      if g[val_r][val_c]==5: g[val_r][val_c]=2
 return g
