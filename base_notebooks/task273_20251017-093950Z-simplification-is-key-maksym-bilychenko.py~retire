def p(a):
 d={}
 for i,r in enumerate(a):
  if 4 in r:
   x=r.index(4);y=r.index(4,x+1)
   for t in a[d.setdefault((x,y),i)+1:i]:t[x+1:y]=[2]*~(x-y)
 return a