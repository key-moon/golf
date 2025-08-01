def p(g):
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==8:x1,y1=x,y
   if v==2:x2,y2=x,y
 sy=(y2>y1)-(y2<y1)
 for y in range(y1+sy,y2+sy,sy):g[y][x1]=4
 sx=(x2>x1)-(x2<x1)
 for x in range(x1+sx,x2,sx):g[y2][x]=4
 return g