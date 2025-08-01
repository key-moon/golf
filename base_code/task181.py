def p(val_g):
 for r in range(3):
  for c,v in enumerate(val_g[r]):
   if v==8:val_g[r][8-c]=8
 return val_g
