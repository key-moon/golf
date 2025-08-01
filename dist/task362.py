def p(g):
 n=len(g);s=sum(r.count(5)for r in g)
 for k in sum(g,[]):
  if k%5:break
 h=next(i for i,r in enumerate(g)if r.count(k)==n)
 v=next(i for i in range(n)if all(r[i]==k for r in g))
 o=[[0]*n for _ in g]
 for i in range(n):o[i][v-s]=k
 o[h+s]=[k]*n
 return o