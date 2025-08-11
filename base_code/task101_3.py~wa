def p(g):
 val_h,val_w=len(g),len(g[0])
 # find a 1 to seed the anchor flood‐fill
 for val_i,val_row in enumerate(g):
  if 1 in val_row:
   val_r0,val_c0=val_i,val_row.index(1);break
 # flood fill all +1 cells to get the full anchor
 val_C={(val_r0,val_c0)};val_Q=[(val_r0,val_c0)]
 for val_r,val_c in val_Q:
  for val_dr,val_dc in((1,0),(-1,0),(0,1),(0,-1)):
   val_nr,val_nc=val_r+val_dr,val_c+val_dc
   if 0<=val_nr<val_h and 0<=val_nc<val_w and g[val_nr][val_nc]>0 and(val_nr,val_nc)not in val_C:
    val_C.add((val_nr,val_nc));val_Q.append((val_nr,val_nc))
 # record relative offsets of 1s and 2s in the anchor
 val_O=[(vr-val_r0,vc-val_c0)for vr,vc in val_Cif g[vr][vc]==1]
 val_T=[(vr-val_r0,vc-val_c0)for vr,vc in val_Cif g[vr][vc]==2]
 # for every other 2‐cell, try to align each anchor‐2 onto it
 for val_r in range(val_h):
  for val_c in range(val_w):
   if g[val_r][val_c]==2and(val_r,val_c)not in val_C:
    for val_dr0,val_dc0 in val_T:
     val_sr,val_sc=val_r-val_dr0,val_c-val_dc0
     if all(0<=val_sr+dr<val_h and 0<=val_sc+dc<val_w and g[val_sr+dr][val_sc+dc]==2for dr,dc in val_T):
      for dr,dc in val_O:
       rr,cc=val_sr+dr,val_sc+dc
       if g[rr][cc]==0:g[rr][cc]=1
      break
 return g
