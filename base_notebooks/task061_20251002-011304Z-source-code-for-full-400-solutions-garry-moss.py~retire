def p(m,t=enumerate):
 f=range;e=len(m);e=len(m[0]);x=lambda u,f:u==f or u*f<1;d=next((u for u in f(1,e)if all(x(n,e)for f in m for(n,e)in zip(f,f[u:]))),e);a=next((u for u in f(1,e)if all(x(n,e)for(u,f)in zip(m,m[u:])for(n,e)in zip(u,f))),e);b={}
 for(e,u)in t(m):
  for(f,n)in t(u):
   if n:b[e%a,f%d]=n
 for(e,u)in t(m):
  for(f,n)in t(u):
   if not n:u[f]=b[e%a,f%d]
 return m