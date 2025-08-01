def p(g):
 for c,v in enumerate(g[-1]):
  if v==2:
   try:
    r=next(i for i,row in enumerate(g)if row[c]==5)
   except StopIteration:
    for s in g:s[c]=2
   else:
    for s in g[:r+2]:s[c+1]=2
    for s in g[r+1:]:s[c]=2
 return g