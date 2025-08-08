def p(g):
 for r in g:
  for c in{*r}-{0}:
   a=r.index(c);e=len(r)-r[::-1].index(c)
   for i in range(a,e):
    if ~r[i]:r[i]=c
 return g