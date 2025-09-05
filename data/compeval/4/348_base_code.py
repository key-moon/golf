def p(g):
 w=len(g[0])
 for x in range(w):
  b=-1
  for y,r in enumerate(g):
   if r[x]==7:b=y
  if b<0:continue
  for y in range(b,-1,-1):
   for d in range(b-y+1):
    for k in(x+d,x-d):
     if 0<=k<w:g[y][k]=7+(d&1)
 return g
