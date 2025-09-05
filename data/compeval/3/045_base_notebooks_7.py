def p(g):
 res=[]
 for r in g:
  r=r[:]
  s={x for x in r if x!=0}
  for c in s:
   idx=[j for j,x in enumerate(r) if x==c]
   l,rgt=min(idx),max(idx)
   for j in range(l,rgt+1):
    if r[j]==0: r[j]=c
  res.append(r)
 return res
