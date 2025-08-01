def p(g):
 val_h,val_w=len(g),len(g[0]);val_b=[0]*5
 for val_l in range(val_w):
  for val_r in range(val_l,val_w):
   val_run=0
   for val_i,val_row in enumerate(g+[[]]):
    if val_i<val_h and all(val_x==0 for val_x in val_row[val_l:val_r+1]):val_run+=1;continue
    if (val_a:=val_run*(val_r-val_l+1))>val_b[0]:val_b=[val_a,val_i-val_run,val_l,val_run,val_r-val_l+1]
    val_run=0
 for val_i in range(val_b[3]):g[val_b[1]+val_i][val_b[2]:val_b[2]+val_b[4]]=[6]*val_b[4]
 return g
