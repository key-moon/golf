def p(g):
 a=g[0][0]
 b=next(x for r in g for x in r if x and x!=a)
 A=[(i,j)for i,R in enumerate(g)for j,v in enumerate(R)if v==a]
 B=[(i,j)for i,R in enumerate(g)for j,v in enumerate(R)if v==b]
 ar=[i for i,_ in A];ac=[j for _,j in A]
 br=[i for i,_ in B];bc=[j for _,j in B]
 r1,r2=min(ar)+1,max(ar)
 c1,c2=min(ac)-1,max(bc)
 r3=max(br)
 for i in range(r1,r3): 
  if 0==g[i][c1]:g[i][c1]=3
 for j in range(min(bc)+1,c2): 
  if 0==g[r2][j]:g[r2][j]=3
 return g