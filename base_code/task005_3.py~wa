def p(g):
 h=len(g);w=len(g[0])
 # find all nonzero connected components by BFS
 seen=[[False]*w for _ in g];comps=[]
 for y in range(h):
  for x in range(w):
   if g[y][x] and not seen[y][x]:
    col=g[y][x]
    q=[(y,x)];seen[y][x]=1;cc=[]
    for yy,xx in q:
     cc.append((yy,xx))
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      y2, x2=yy+dy, xx+dx
      if 0<=y2<h and 0<=x2<w and not seen[y2][x2] and g[y2][x2]==col:
       seen[y2][x2]=1; q.append((y2,x2))
    comps.append((col,cc))
 # overlay one mask at every cell of the other, for any pair on same rows
 for i,(c1,cells1) in enumerate(comps):
  for j,(c2,cells2) in enumerate(comps):
   if i>=j or c1==c2: continue
   ys1=[y for y,x in cells1]; ys2=[y for y,x in cells2]
   if max(ys1)<min(ys2) or max(ys2)<min(ys1): continue
   # bounding boxes
   r1=min(y for y,x in cells1);c1min=min(x for y,x in cells1)
   r2=min(y for y,x in cells2);c2min=min(x for y,x in cells2)
   H2=max(y for y,x in cells2)-r2+1;W2=max(x for y,x in cells2)-c2min+1
   H1=max(y for y,x in cells1)-r1+1;W1=max(x for y,x in cells1)-c1min+1
   # tile mask2 at each cell1
   for (y1,x1) in cells1:
    dy=y1-r1;dx=x1-c1min
    for (y2,x2) in cells2:
     g[r2+(y2-r2)+dy*H2][c2min+(x2-c2min)+dx*W2]=g[y2][x2]
   # tile mask1 at each cell2
   for (y2,x2) in cells2:
    dy=y2-r2;dx=x2-c2min
    for (y1,x1) in cells1:
     g[r1+(y1-r1)+dy*H1][c1min+(x1-c1min)+dx*W1]=g[y1][x1]
 return g
