def p(r,k=range):
 i,g=len(r),len(r[0]);u=[k[:]for k in r];l,f=[k for k in k(i)if all(k==8for k in r[k])];d,e=[n for n in k(g)if all(r[k][n]==8for k in k(i))]
 for n in k(i):
  for t in k(g):
   if not u[n][t]:
    if n<l and d<t<e:u[n][t]=2
    elif l<n<f and t<d:u[n][t]=4
    elif l<n<f and d<t<e:u[n][t]=6
    elif l<n<f and t>e:u[n][t]=3
    elif n>f and d<t<e:u[n][t]=1
 return u