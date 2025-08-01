def p(val_g):
 val_h,val_w=len(val_g),len(val_g[0])
 val_shapes=[]
 for val_i in range(val_h):
  for val_j in range(val_w):
   if val_g[val_i][val_j]==2:
    val_a,val_b=val_i,val_j
    val_Q=[(val_a,val_b)]
    for _ in val_Q:
     for val_dr,val_dc in((1,0),(-1,0),(0,1),(0,-1)):
      x,y=_[0]+val_dr,_[1]+val_dc
      if 0<=x<val_h and 0<=y<val_w and val_g[x][y]==3 and (x,y) not in val_Q:
       val_Q.append((x,y))
    val_O=[(x-val_a,y-val_b)for x,y in val_Q]
    val_shapes.append((val_a,val_b,val_O))
 for val_a,val_b,val_O in val_shapes:
  for val_dr,val_dc in((0,1),(0,-1),(1,0),(-1,0)):
   k=1
   while 1:
    x,y=val_a+k*val_dr,val_b+k*val_dc
    if not(0<=x<val_h and 0<=y<val_w):break
    for od,oc in val_O:
     i,j=x+od,y+oc
     if not(0<=i<val_h and 0<=j<val_w) or val_g[i][j]!=0:break
    else:
     for od,oc in val_O:
      val_g[x+od][y+oc]=2 if(od,oc)==(0,0)else 3
     k+=1;continue
    break
 return val_g
