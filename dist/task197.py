def p(g):
 b=next(r for r in g if 0 not in r)
 c=[]
 for x in b:
  if x not in c:
   c+=[x]
 for r in g:
  s=[]
  for x in r:
   if x and x not in s:
    s+=[x]
  if s and 0 in r:
   for i,x in enumerate(b):
    r[i]=s[c.index(x)]
 return g