def p(g):
 t=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==2]
 a=min(i for i,j in t);b=min(j for i,j in t);h=max(i for i,j in t)-a+1
 A=[[0]*h for _ in range(h)]
 for i,j in t:A[i-a][j-b]=2
 k=next(v for r in g for v in r if v*(v-2))
 T=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==k]
 c=min(i for i,j in T);d=min(j for i,j in T);s=(h-2)//(max(i for i,j in T)-c+1)
 for i,j in T:
  for x in range(s):
   for y in range(s):A[1+(i-c)*s+x][1+(j-d)*s+y]=k
 return A
