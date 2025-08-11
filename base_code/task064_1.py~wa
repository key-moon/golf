def p(g):
 val_m={}
 for val_i,val_r in enumerate(g):
  for val_j,val_v in enumerate(val_r):
   val_t=val_m.get(val_v)
   if val_t:
    val_t[0]=min(val_t[0],val_i); val_t[1]=max(val_t[1],val_i)
    val_t[2]=min(val_t[2],val_j); val_t[3]=max(val_t[3],val_j)
    val_t[4]+=1
   else:
    val_m[val_v]=[val_i,val_i,val_j,val_j,1]
 val_b=max(val_m,key=lambda c:val_m[c][4])
 val_B=max((c for c in val_m if c!=val_b),key=lambda c:val_m[c][4])
 val_x1,val_x2,val_y1,val_y2,_=val_m[val_B]
 for val_d,val_t in val_m.items():
  if val_d!=val_b and val_d!=val_B:
   val_i,val_j=val_t[0],val_t[2]
   if val_i<val_x1 or val_i>val_x2:
    for val_k in range(min(val_i,val_x1),max(val_i,val_x2)+1): g[val_k][val_j]=val_d
   else:
    for val_k in range(min(val_j,val_y1),max(val_j,val_y2)+1): g[val_i][val_k]=val_d
 return g
