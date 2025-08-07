def p(g):
 val_h,val_w=len(g),len(g[0]);val_vs=list({val_v for val_r in g for val_v in val_r if val_v});val_ds={}
 for val_v in val_vs:
  val_n=val_s=0
  for val_i,val_r in enumerate(g):
   for val_j,val_x in enumerate(val_r):
    if val_x==val_v:
     val_d=2*val_i-(val_h-1);val_e=2*val_j-(val_w-1);val_s+=val_d*val_d+val_e*val_e;val_n+=1
  val_ds[val_v]=val_s/val_n
 val_rep=max(val_vs,key=lambda val_v:val_ds[val_v]);val_r2=[val_r[:]for val_r in g]
 for val_i,val_r in enumerate(g):
  for val_j,val_x in enumerate(val_r):
   if val_x==val_rep:
    for val_ii in(val_i,val_h-1-val_i):
     for val_jj in(val_j,val_w-1-val_j):
      val_r2[val_ii][val_jj]=val_rep
 return val_r2
