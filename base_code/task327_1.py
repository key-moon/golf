def p(val_g):
    val_n=len(val_g)
    val_o=[[0]*(val_n*2)for _ in range(val_n*2)]
    for val_i in range(val_n):
      for val_j in range(val_n):
        for val_k in range(val_n*2-max(val_i,val_j)):
          val_o[val_i+val_k][val_j+val_k]=val_g[val_i][val_j]
    return val_o
