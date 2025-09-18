def p(g):
 val_d={}
 for val_y,val_r in enumerate(g):
  for val_x,val_v in enumerate(val_r):
   if val_v:val_d.setdefault(val_v,[]).append((val_y,val_x))
 val_b=[0,0,0,0,0,0]
 for val_v,val_pts in val_d.items():
  val_v0,val_v1=min(_[0]for _ in val_pts),max(_[0]for _ in val_pts);val_h0,val_h1=min(_[1]for _ in val_pts),max(_[1]for _ in val_pts)
  val_s=(val_v1-val_v0+1)*(val_h1-val_h0+1)
  if val_s==len(val_pts)and val_s>val_b[0]:val_b=[val_s,val_v0,val_h0,val_v1,val_h1,val_v]
 val_r=[[0]*len(g[0])for _ in g]
 for val_y in range(val_b[1],val_b[3]+1):
  for val_x in range(val_b[2],val_b[4]+1):val_r[val_y][val_x]=val_b[5]
 return val_r
