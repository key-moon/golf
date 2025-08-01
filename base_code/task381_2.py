def p(g):
 for val_l in g:
  val_e=None;val_j=0
  while val_j<len(val_l):
   if val_l[val_j]==2:
    if val_e:
     for val_c in range(val_e+1,val_j):val_l[val_c]=9
    while val_j+1<len(val_l)and val_l[val_j+1]==2:val_j+=1
    val_e=val_j
   val_j+=1
 return g
