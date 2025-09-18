def p(g):
 val_h=len(g)
 val_w=len(g[0])
 val_c0=(val_h-1)/2;val_c1=(val_w-1)/2
 val_d={}
 for i in range(val_h):
  for j in range(val_w):
   if g[i][j]:val_d.setdefault(g[i][j],[]).append((i,j))
 for k,val_v in val_d.items():
  xs=[x for x,_ in val_v];ys=[y for _,y in val_v]
  x0,x1=min(xs),max(xs);y0,y1=min(ys),max(ys)
  cx,cy=(x0+x1)//2,(y0+y1)//2
  if g[cx][cy]==k:
   for i,j in val_v:
    di=i-val_c0;dj=j-val_c1
    for a,b in((-dj,di),(-di,-dj),(dj,-di)):
      g[int(val_c0+a)][int(val_c1+b)]=k
 return g
