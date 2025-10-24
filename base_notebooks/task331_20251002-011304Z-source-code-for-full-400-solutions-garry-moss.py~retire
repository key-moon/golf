def p(q,p=enumerate):
 l=[]
 for(e,x)in p(q):
  for(k,n)in p(x):
   if q[e][k]==1:l+=[[e,k]]
 for p in l:
  h,e=p
  if h>0:q[h-1][e]=2
  if h<9:q[h+1][e]=8
  if e>0:q[h][e-1]=7
  if e<9:q[h][e+1]=6
 return q