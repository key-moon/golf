def p(g):
 for val_i in range(len(g)-2):
  for val_j in range(len(g[0])-2):
   if not any(g[val_i+val_a][val_j+val_b]
              for val_a in(0,1,2) for val_b in(0,1,2)):
    for val_a in(0,1,2):
     for val_b in(0,1,2):g[val_i+val_a][val_j+val_b]=1
    return g
