def p(g):
 for val_r in g:
  try:val_j,val_v=next((i,v)for i,v in enumerate(val_r)if v)
  except:continue
  for val_k in range(len(val_r)-val_j):val_r[val_j+val_k]=[val_v,5][val_k&1]
 return g
