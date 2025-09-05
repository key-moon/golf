def p(g):
 for i,r in enumerate(g):
  u=[-1]
  for j,v in enumerate(r):
   if v==2:u+=[j]
  u+=[len(r)]
  for k in range(len(u)-1):
   if k%3==2*(i<1):
    for j in range(u[k]+1,u[k+1]):r[j]=4
 return g
