def p(g):
  val_h=len(g);val_w=len(g[0])
  for val_p in range(1,val_h+1):
    if val_h%val_p:continue
    for val_q in range(1,val_w+1):
      if val_w%val_q:continue
      if all(g[val_i][val_j]==g[val_i%val_p][val_j%val_q]for val_i in range(val_h)for val_j in range(val_w)):return[val_r[:val_q]for val_r in g[:val_p]]
