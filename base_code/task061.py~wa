def p(g):
    val_h=len(g)//3;val_w=len(g[0])//3
    for val_bi in range(3):
     for val_bj in range(3):
      if all(g[val_bi*val_h+val_a][val_bj*val_w+val_b]
             for val_a in range(val_h) for val_b in range(val_w)):
         val_r0,val_c0=val_bi*val_h,val_bj*val_w
    for val_i in range(len(g)):
     for val_j in range(len(g[0])):
      if g[val_i][val_j]==0:
         g[val_i][val_j]=g[val_r0+val_i%val_h][val_c0+val_j%val_w]
    return g
