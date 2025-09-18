def p(g):
 import math
 H,W=len(g),len(g[0])
 val_pts=[(y,x,v)for y,r in enumerate(g)for x,v in enumerate(r)if v]
 val_ys=sorted({y for y,_,_ in val_pts})
 val_xs=sorted({x for _,x,_ in val_pts})
 if len(val_ys)>1:
  val_dY=val_ys[1]-val_ys[0]
  for i in range(2,len(val_ys)):val_dY=math.gcd(val_dY,val_ys[i]-val_ys[i-1])
 else:val_dY=H-1-val_ys[0]
 if len(val_xs)>1:
  val_dX=val_xs[1]-val_xs[0]
  for i in range(2,len(val_xs)):val_dX=math.gcd(val_dX,val_xs[i]-val_xs[i-1])
 else:val_dX=W-1-val_xs[0]
 val_o=[[0]*W for _ in g]
 for y,x,v in val_pts:
  for i in range(y,H,val_dY):
   for j in range(x,W,val_dX):val_o[i][j]=v
 return val_o
