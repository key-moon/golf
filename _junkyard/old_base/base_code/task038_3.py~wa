def p(g):
 val_n=len(g);val_s=set();val_c=0
 for val_i,val_r in enumerate(g):
  for val_j,val_v in enumerate(val_r):
   if val_v==1 and (val_i,val_j)not in val_s:
    val_t=[(val_i,val_j)];val_s.add((val_i,val_j));val_z=0
    while val_t:
     val_x,val_y=val_t.pop();val_z+=1
     for val_a,val_b in((1,0),(-1,0),(0,1),(0,-1)):
      val_p,val_q=val_x+val_a,val_y+val_b
      if 0<=val_p<val_n and 0<=val_q<len(g[0]) and g[val_p][val_q]==1 and (val_p,val_q)not in val_s:
       val_s.add((val_p,val_q));val_t.append((val_p,val_q))
    if val_z>1:val_c+=1
 return([1]*val_c+[0]*5)[:5]
