def p(val_g):
 for val_i in range(len(val_g)):
  for val_j in range(len(val_g[0])):
   if not val_g[val_i][val_j]:
    for val_k in range(1,len(val_g)):
     if val_i+val_k<len(val_g) and val_j+val_k<len(val_g[0]) and val_g[val_i+val_k][val_j+val_k]:
      val_g[val_i][val_j]=val_g[val_i+val_k][val_j+val_k];break
     if val_i>=val_k and val_j>=val_k and val_g[val_i-val_k][val_j-val_k]:
      val_g[val_i][val_j]=val_g[val_i-val_k][val_j-val_k];break
 return val_g
