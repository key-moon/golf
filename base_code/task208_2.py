def p(g):
 val_a=sum(g,[])
 val_b=max(set(val_a),key=val_a.count)
 for val_c in set(val_a)-{val_b}:
  val_t=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==val_c]
  if(val_h:=max(i for i,j in val_t)-min(i for i,j in val_t)+1)*(val_w:=max(j for i,j in val_t)-min(j for i,j in val_t)+1)>len(val_t):
   val_r0,val_c0=min(i for i,j in val_t),min(j for i,j in val_t);break
 val_bs=[(i,j)for i in range(val_h)for j in range(val_w)if i*(i-val_h+1)*j*(j-val_w+1)==0]
 for val_i in range(len(g)-val_h+1):
  for val_j in range(len(g[0])-val_w+1):
   if val_i==val_r0 and val_j==val_c0: continue
   if all(g[val_i+i][val_j+j]==val_b for i in range(1,val_h-1) for j in range(1,val_w-1)) and all(g[val_i+i][val_j+j]!=val_c for i,j in val_bs):
    for i,j in val_bs: g[val_i+i][val_j+j]=val_c
    return g
 return g
