def p(g):
 val_n=len(g);val_o=[[0]*val_n for _ in g]
 for val_i in range(2,val_n-2):
  for val_j in range(2,val_n-2):
   val_c=g[val_i][val_j]
   if val_c and g[val_i-1][val_j]==g[val_i+1][val_j]==g[val_i][val_j-1]==g[val_i][val_j+1]!=val_c:
    val_k=g[val_i-1][val_j]
    for val_dx in range(-2,3):
     for val_dy in range(-2,3):
      val_s=abs(val_dx)+abs(val_dy)
      if val_s<3 or val_s==4:
       val_o[val_i+val_dx][val_j+val_dy]=val_c if val_s>2 else val_k
 return val_o
