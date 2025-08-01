def p(g):
 for i,r in enumerate(g):
  if 3 in r:a=i;b=r.index(3)
  if 4 in r:c=i;d=r.index(4)
 g[a][b]=0;g[a+(c>a)-(c<a)][b+(d>b)-(d<b)]=3
 return g