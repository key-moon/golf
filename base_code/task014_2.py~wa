def p(g):
 val_cs={}
 for val_r in g:
  for val_v in val_r:
   if val_v:val_cs[val_v]=val_cs.get(val_v,0)+1
 val_c=min(val_cs,key=val_cs.get)
 val_r0,len0,len1=len(g),len(g),0;val_c0,val_r1=len(g[0]),0
 for val_i,val_r in enumerate(g):
  for val_j,val_v in enumerate(val_r):
   if val_v==val_c:
    val_r0=min(val_r0,val_i);val_r1=max(val_r1,val_i)
    val_c0=min(val_c0,val_j);val_c1=max(val_c1,val_j)
 return [val_r[val_c0:val_c1+1]for val_r in g[val_r0:val_r1+1]]
