def p(i,t=enumerate):
 r=range;f=len(i);f=len(i[0]);z=lambda n,f:n==f or n*f<1;x=next((n for n in r(1,f)if all(z(d,p)for f in i for(d,p)in zip(f,f[n:]))),f);a=next((n for n in r(1,f)if all(z(d,p)for(n,f)in zip(i,i[n:])for(d,p)in zip(n,f))),f);u={}
 for(p,n)in t(i):
  for(f,d)in t(n):
   if d:u[p%a,f%x]=d
 for(p,n)in t(i):
  for(f,d)in t(n):
   if not d:n[f]=u[p%a,f%x]
 return i