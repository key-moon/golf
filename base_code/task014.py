def p(g):
 d={}
 for i,r in enumerate(g):
  for x in r:
   if x and x not in d:d[x]=i
 k=max(d,key=d.get)
 p=[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==k]
 a=min(i for i,j in p);b=max(i for i,j in p);c=min(j for i,j in p);e=max(j for i,j in p)
 return[[k if g[i][j]==k else 0 for j in range(c,e+1)]for i in range(a,b+1)]
