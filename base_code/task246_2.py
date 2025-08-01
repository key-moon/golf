def p(val_g):
 val_p=sorted((val_i,val_j)for val_i,val_row in enumerate(val_g)
              for val_j,val_v in enumerate(val_row)if val_v in(2,3))
 (val_rs,val_cs),(val_rt,val_ct)=val_p
 for val_j in range(min(val_cs,val_ct),max(val_cs,val_ct)+1):
  val_g[val_rs][val_j]or val_g[val_rs].__setitem__(val_j,8)
 for val_i in range(min(val_rs,val_rt),max(val_rs,val_rt)+1):
  val_g[val_i][val_ct]or val_g[val_i].__setitem__(val_ct,8)
 return val_g
