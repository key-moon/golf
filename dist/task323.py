def p(g):
 h=len(g)
 for y0,r in enumerate(g):
  if 8 in r:x0=r.index(8);break
 for y,r in enumerate(g):
  if y==y0:continue
  d=abs(y0-y);s=1if y<y0 else-1;p=x0+s*d
  if d&1:
   x=p-s
   if 0<=x<h:r[x]=5
  else:
   for x in(range(p-2,p+1)if y<y0 else range(p,p+3)):
    if 0<=x<h:r[x]=5
 return g