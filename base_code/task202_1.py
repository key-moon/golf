def p(g):
 val_i=0
 while val_i<len(g):
  val_bg=next(v for v in g[val_i] if v)
  val_j=val_i
  while val_j<len(g)and next(v for v in g[val_j] if v)==val_bg:val_j+=1
  val_C={y for r in g[val_i:val_j]for y,z in enumerate(r)if z<1}
  for r in g[val_i:val_j]:
   for y in val_C:r[y]=0
  val_i=val_j
 return g
