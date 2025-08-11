def p(g):
    val_a=[r[:]for r in g];val_m=len(g);val_n=len(g[0])
    val_l=min(j for i in range(val_m)for j in range(val_n)if val_a[i][j]==2)
    val_r=max(j for i in range(val_m)for j in range(val_n)if val_a[i][j]==2)
    val_s=set()
    for val_i in range(val_m):
     for val_j in range(val_n):
      if val_a[val_i][val_j]==8:
       # find which 2‐run this elbow sits against
       if any(val_a[val_i][k]==2 for k in range(val_j)):
        val_p=max(k for k in range(val_j)if val_a[val_i][k]==2); val_s.add(val_l)
        for k in range(val_p+1,val_j): g[val_i][k]=8
       else:
        val_p=min(k for k in range(val_j+1,val_n)if val_a[val_i][k]==2); val_s.add(val_r)
        for k in range(val_j+1,val_p): g[val_i][k]=8
       g[val_i][val_j]=4
    # for the 2‐run with no input‐8 we draw at its midpoint
    for val_c in (val_l,val_r):
     if val_c not in val_s:
      ys=[i for i in range(val_m)if val_a[i][val_c]==2]
      val_o=(min(ys)+max(ys))//2
      if val_c==val_l:
       for k in range(val_l+1,val_r): g[val_o][k]=8
      else:
       for k in range(val_r): g[val_o][k]=8
    return g
