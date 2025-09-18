def p(g):
 for val_s in range(1,min(len(g),len(g[0]))):
  val_d={}
  for val_i in range(0,len(g)-val_s+1,val_s):
   for val_j in range(0,len(g[0])-val_s+1,val_s):
    val_b=tuple(tuple(g[r][val_j:val_j+val_s])for r in range(val_i,val_i+val_s))
    val_d[val_b]=val_d.get(val_b,0)+1
  val_vs=val_d.values()
  if len({*val_vs})>1:
   val_m=min(val_vs)
   return [list(r)for r,c in val_d.items() if c==val_m][0]
