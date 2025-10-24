def p(p,u=enumerate):
 e=range;a=len(p);a=len(p[0]);i=lambda r,i:r==i or r*i<1;d=next((r for r in e(1,a)if all(i(a,e)for n in p for(a,e)in zip(n,n[r:]))),a);m=next((r for r in e(1,a)if all(i(a,e)for(r,n)in zip(p,p[r:])for(a,e)in zip(r,n))),a);o={}
 for(e,r)in u(p):
  for(n,a)in u(r):
   if a:o[e%m,n%d]=a
 for(e,r)in u(p):
  for(n,a)in u(r):
   if not a:r[n]=o[e%m,n%d]
 return p