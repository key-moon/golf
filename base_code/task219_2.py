def p(g):
 val_h=len(g);val_w=len(g[0]);val_bs=val_h//3
 val_r=max(range(val_h),key=lambda y:sum(g[y][x]==8 for x in range(val_w)))
 val_cs=[x for x in range(val_w) if g[val_r][x]==8]
 for val_b in(1,2):
  for val_c in val_cs:
   i=val_r+val_b*val_bs
   if g[i][val_c]==0:g[i][val_c]=1
 return g
