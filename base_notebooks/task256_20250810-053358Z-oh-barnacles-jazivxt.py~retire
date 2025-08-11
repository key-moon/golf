def p(g):
 c,x=0,0
 h,w=len(g),len(g[c])
 for r in range(h):
  if sum(g[r])//2>0:
   x,c=int(r),sum(g[r])//2
 for r in range(h):
  z=x-r+c
  if r!=x and z>0:
   if r<x:g[r]=[3]*z + [0]*(w-z)
   if r>x:g[r]=[1]*z + [0]*(w-z)
 return g
