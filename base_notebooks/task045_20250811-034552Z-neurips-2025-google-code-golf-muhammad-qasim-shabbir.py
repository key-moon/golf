def p(g):
 v=[]
 for r in g:
  r=r[:]
  s={x for x in r if x!=0}
  for c in s:
   D=[j for j,x in enumerate(r)if x==c]
   l,E=min(D),max(D)
   for j in range(l,E+1):
    if r[j]==0:r[j]=c
  v.append(r)
 return v