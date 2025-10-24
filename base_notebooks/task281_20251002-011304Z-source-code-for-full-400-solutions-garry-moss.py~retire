def p(n):
 u=sum(n,[]);f=len(n[0]);r=[f for(f,r)in enumerate(u)if r];a,p=r[0]//f,r[-1]//f;e=min(r%f for r in r);o=max(r%f for r in r);r,d=sorted({*u}-{0,8},key=u.count);s=[d]+[r]*(o-e-1)+[d]
 for r in range(a,p+1):n[r][e:o+1]=(s,[d]*len(s))[r in(a,p)]
 return n