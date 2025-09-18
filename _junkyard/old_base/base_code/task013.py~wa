def p(g):
 l=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 (i,k,A),(x,y,B)=l
 if i*x:
  h=x-i
  for I,r in enumerate(g):
   for j in range(len(r)):r[j]=A if (I-i)%(h*2)<h else B
 else:
  h=y-k
  for r in g:
   for j in range(len(r)):r[j]=A if (j-k)%(h*2)<h else B
 return g
