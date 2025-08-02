def p(g):
 k=1
 for _ in range(4):
  if g[0].count(8)>k:
   d,k=0,99
   for s in g[1:]:
    d+=s[0]-s[-1]>>1
    if d<0:
     s[:d]=g[0][-d:]
    else:
     s[d:]=g[0]
  *g,=map(list,zip(*g[::-1]))
 return g