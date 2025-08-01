def p(g):
 val_n=len(g);val_m=len(g[0]);val_l=[0]*val_m
 for val_j in range(val_m):
  while val_l[val_j]<val_n and g[val_n-1-val_l[val_j]][val_j]==5:val_l[val_j]+=1
 val_x=[z for z in val_l if z];val_M=max(val_l);val_mn=min(val_x)
 val_jM=val_l.index(val_M);val_jm=val_l.index(val_mn)
 return [[1 if val_j==val_jM and val_i>=val_n-val_M else 2 if val_j==val_jm and val_i>=val_n-val_mn else 0 for val_j in range(val_m)] for val_i in range(val_n)]
