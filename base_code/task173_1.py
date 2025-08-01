def p(g):
 val_cnt={}
 for val_r in g:
  for val_v in val_r:
   if val_v: val_cnt[val_v]=val_cnt.get(val_v,0)+1
 val_c=min(val_cnt,key=lambda val_z:val_cnt[val_z])
 for val_Y,val_r in enumerate(g):
  for val_X,val_v in enumerate(val_r):
   if val_v==val_c: break
  else: continue
  break
 val_comp={(val_Y,val_X)}; val_s=[(val_Y,val_X)]
 H,W=len(g),len(g[0])
 while val_s:
  val_y,val_x=val_s.pop()
  for val_dy,val_dx in((1,0),(-1,0),(0,1),(0,-1)):
   val_y2,val_x2=val_y+val_dy,val_x+val_dx
   if 0<=val_y2<H and 0<=val_x2<W and g[val_y2][val_x2] and (val_y2,val_x2) not in val_comp:
    val_comp.add((val_y2,val_x2)); val_s.append((val_y2,val_x2))
 val_P=[(val_y-val_Y,val_x-val_X,g[val_y][val_x]) for val_y,val_x in val_comp]
 for val_y in range(H):
  for val_x in range(W):
   if all(0<=val_y+val_dy<H and 0<=val_x+val_dx<W and g[val_y+val_dy][val_x+val_dx] in (0,val_c2) for val_dy,val_dx,val_c2 in val_P):
    for val_dy,val_dx,val_c2 in val_P: g[val_y+val_dy][val_x+val_dx]=val_c2
 return g
