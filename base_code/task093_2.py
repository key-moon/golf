def p(val_g):
 val_r=[i for i,row in enumerate(val_g) if 5 in row];val_r0,val_r1=val_r[0],val_r[-1]
 val_c=[j for j in range(len(val_g[0])) if any(val_g[i][j]==5 for i in val_r)];val_c0,val_c1=val_c[0],val_c[-1]
 val_h=[[0]*len(val_g[0]) for _ in val_g]
 for val_i in range(val_r0,val_r1+1):
  for val_j in range(val_c0,val_c1+1):val_h[val_i][val_j]=5
 for val_i in range(len(val_g)):
  for val_j,val_x in enumerate(val_g[val_i]):
   if val_x and val_x-5:
    if val_i<val_r0: val_h[val_r0-1][val_j]=5
    elif val_i>val_r1: val_h[val_r1+1][val_j]=5
    elif val_j<val_c0: val_h[val_i][val_c0-1]=5
 else
 return val_h
