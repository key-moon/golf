def p(g):
 for val_i in range(len(g)):
  for val_j in range(len(g[0])):
   if not g[val_i][val_j]:
    for val_k in range(1,len(g)):
     if val_i+val_k<len(g) and val_j+val_k<len(g[0]) and g[val_i+val_k][val_j+val_k]:
      g[val_i][val_j]=g[val_i+val_k][val_j+val_k];break
     if val_i>=val_k and val_j>=val_k and g[val_i-val_k][val_j-val_k]:
      g[val_i][val_j]=g[val_i-val_k][val_j-val_k];break
 return g
