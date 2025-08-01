def p(val_g):
 val_a=[x for r in val_g for x in r];val_b=max(val_a,key=val_a.count);val_c=[(1,0),(0,1),(-1,0),(0,-1)]
 def val_d(val_x):
  val_e={(i,j)for i in range(len(val_g))for j in range(len(val_g[0]))if val_g[i][j]==val_x};val_f=[]
  while val_e:
   val_h={val_e.pop()};val_i=[]
   while val_h:
    val_j=val_h.pop();val_i.append(val_j)
    for val_l in val_c:
     val_k=(val_j[0]+val_l[0],val_j[1]+val_l[1])
     if val_k in val_e:val_e.remove(val_k);val_h.add(val_k)
   val_f.append(val_i)
  return val_f
 for val_m in val_d(val_b):
  val_n=[i for i,_ in val_m];val_o=[j for _,j in val_m]
  val_r0,val_r1=min(val_n),max(val_n);val_c0,val_c1=min(val_o),max(val_o)
  val_p=[(i,j)for i in range(val_r0,val_r1+1)for j in range(val_c0,val_c1+1)if val_g[i][j]==0]
  if not val_p:continue
  val_s0,val_s1=min(i for i,_ in val_p),min(j for _,j in val_p)
  val_sh=sorted((i-val_s0,j-val_s1)for i,j in val_p)
  for val_t in set(val_a)-{0,val_b}:
   for val_u in val_d(val_t):
    val_m0,val_n0=min(i for i,_ in val_u),min(j for _,j in val_u)
    if sorted((i-val_m0,j-val_n0)for i,j in val_u)==val_sh:
     for i,j in val_u:val_g[i][j]=0
     for i,j in val_p:val_g[i][j]=val_t
 return val_g
