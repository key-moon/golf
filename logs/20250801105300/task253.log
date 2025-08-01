def p(g):
 m={}
 for y,r in enumerate(g):
  for x,z in enumerate(r):
   if z:m.setdefault(z,[]).append((y,x))
 o=[[0]*4 for _ in[0]*4]
 for c,l in m.items():
  u=min(y for y,x in l);v=min(x for y,x in l)
  t=sum(y for y,x in l);w=sum(x for y,x in l)
  i=t-1-3*u;j=w-1-3*v
  for y,x in l:o[i*2+y-u][j*2+x-v]=c
 return o