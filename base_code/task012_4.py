def p(g):
 val_r=[[0]*len(g[0])for _ in g]
 for val_i in range(2,len(g)-2):
  for val_j in range(2,len(g[0])-2):
   val_C=g[val_i][val_j];val_A=g[val_i-1][val_j]
   if val_C*val_A*g[val_i+1][val_j]*g[val_i][val_j-1]*g[val_i][val_j+1]:
    for val_di in range(-2,3):
     for val_dj in range(-2,3):
      val_r[val_i+val_di][val_j+val_dj]=val_A if not(val_di*val_dj)and abs(val_di)+abs(val_dj)>0 else val_C
 return val_r
