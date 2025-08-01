def p(g):
 m,n=len(g),len(g[0])
 val_zs=[(i,j) for i in range(m) for j in range(n) if g[i][j]==5]
 val_r0,val_r1=min(i for i,j in val_zs),max(i for i,j in val_zs)
 val_c0,val_c1=min(j for i,j in val_zs),max(j for i,j in val_zs)
 R=[[0]*n for _ in range(m)]
 # copy original 5‐band
 for i in range(val_r0,val_r1+1):
  for j in range(val_c0,val_c1+1): R[i][j]=5
 hor = (val_r1-val_r0>val_c1-val_c0)
 # for every non‐0/non‐5 cell, shoot one 5 to the nearest band boundary
 for i in range(m):
  for j in range(n):
   v=g[i][j]
   if v and v!=5:
    if hor:
     if i<val_r0: R[val_r0-1][j]=5
     if i>val_r1: R[val_r1+1][j]=5
    else:
     if j<val_c0: R[i][val_c0-1]=5
     if j>val_c1: R[i][val_c1+1]=5
 return R
