def p(l):
 i,i=len(l),len(l[0]);r=lambda f:next((p,e)for p in range(i-1)for e in range(i-1)if l[p][e]==l[p+1][e+1]==f);p,e=r(1)
 while p>=1and e>=1:p,e=p-1,e-1;l[p][e]=1
 p,e=r(2)
 while p<i-1and e<i-1:p,e=p+1,e+1;l[p][e]=2
 return l