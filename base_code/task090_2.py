def p(g):
 val_r,val_c=len(g),len(g[0]);val_best=0
 for val_i in range(val_r):
  for val_j in range(val_i,val_r):
   val_h=val_j-val_i+1;val_cur=0
   val_ok=[all(not g[r][c] for r in range(val_i,val_j+1))for c in range(val_c)]
   for val_col in range(val_c+1):
    if val_col<val_c and val_ok[val_col]:val_cur+=1
    else:
     if val_cur*val_h>val_best:
      val_best,val_i1,val_j1,val_w,val_s=val_cur*val_h,val_i,val_j,val_cur,val_col-val_cur
     val_cur=0
 for r in range(val_i1,val_j1+1):
  for c in range(val_s,val_s+val_w):
   g[r][c]=6
 return g
