def p(g):
 m={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:m[v]=min(m.get(v,len(g)),i)
 d=m[1];n=[[0]*len(r)for r in g]
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:n[i-m[v]+d][j]=v
 return n
