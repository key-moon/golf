def p(g):
 T=[]
 for r in g:
  r=r[:]
  s={x for x in r if x!=0}
  for c in s:
   u=[j for j,x in enumerate(r)if x==c]
   l,R=min(u),max(u)
   for j in range(l,R+1):
    if r[j]==0:r[j]=c
  T.append(r)
 return T