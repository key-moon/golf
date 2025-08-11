def p(g):
 val_a={v for r in g for v in r if v}
 for val_c in val_a:
  val_ps=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==val_c]
  val_i0=min(i for i,j in val_ps);val_i1=max(i for i,j in val_ps)
  val_j0=min(j for i,j in val_ps);val_j1=max(j for i,j in val_ps)
  for val_i in range(val_i0,val_i1+1):
   g[val_i][val_j0:val_j1+1]=[val_c]*(val_j1-val_j0+1)
 return g
