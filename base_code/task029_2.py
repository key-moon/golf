def p(g):
 val_d=[]
 for val_i,val_r in enumerate(g):
  val_m=0;val_s=0;val_l=1
  for val_j in range(1,len(val_r)):
   if val_r[val_j]==val_r[val_j-1]:val_l+=1
   else:
    if val_l>val_m:val_m,val_s=val_l,val_j-val_l
    val_l=1
  if val_l>val_m:val_m,val_s=val_l,len(val_r)-val_l
  if val_m>1:val_d.append((val_i,val_s,val_m))
 val_L=max(t[2]for t in val_d)
 a,b=[t for t in val_d if t[2]==val_L]
 y1,x1,_=a; y2,x2,_=b
 return [row[x1+1:x2] for row in g[y1+1:y2]]
