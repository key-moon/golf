def p(g):
 val_c=next(filter(None,g[-1]));val_p=g[-1].index(val_c)
 for val_j in range(val_p,10,2):
  for val_i in range(10):g[val_i][val_j]=val_c
 for val_k,val_j in enumerate(range(val_p+1,10,2)):g[(val_k&1)*9][val_j]=5
 return g
