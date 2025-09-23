def p(u):
 e,t,*o={(p,m):v for p,u in enumerate(u)for m,v in enumerate(u)if v},[]
 def p(u):
  if u in e:r[u]=e.pop(u);p((u[0]-1,u[1]));p((u[0]+1,u[1]));p((u[0],u[1]-1));p((u[0],u[1]+1))
 while e:o+=[r:={}];p(min(e))
 for r in o+o:
  i,={*o[0].values()}&{*o[1].values()};g,={*r.values()}-{i};p,m=min(e:=[u for u in r if r[u]==i]);i=max(e)[0]+1-p;t+=[(u[0]-p,u[1]-m)for u in r if(r[u]==g)==i]
  for r,v in t:
   for e in range(i*i):u[p+r*i+e//i][m+v*i+e%i]=g
 return u