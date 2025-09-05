def p(g):
 F=[]
 for r in g:
  r=r[:]
  s={x for x in r if x!=0}
  for c in s:
   N=[j for j,x in enumerate(r)if x==c]
   l,m=min(N),max(N)
   for j in range(l,m+1):
    if r[j]==0:r[j]=c
  F.append(r)
 return F