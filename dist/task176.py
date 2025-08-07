B=range
A=enumerate
def p(g):
 for(i,r)in A(g):
  u=[-1]
  for(j,v)in A(r):
   if v==2:u+=[j]
  u+=[len(r)]
  for k in B(len(u)-1):
   if k%3==2*(i<1):
    for j in B(u[k]+1,u[k+1]):r[j]=4
 return g