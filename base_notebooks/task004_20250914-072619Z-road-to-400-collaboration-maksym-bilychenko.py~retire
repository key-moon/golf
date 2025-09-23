def p(g,p=enumerate):
 a=[[0]*len(g[0])for _ in g]
 for q in{*sum(g,[])}-{0}:
  f=[(y,x)for y,r in p(g)for x,v in p(r)if v==q];k,l=map(max,zip(*f))
  for y,x in f:a[y][x+(y<k)*(x<l)]=q
 return a