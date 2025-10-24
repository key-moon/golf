def p(h):
 p=h;c,c=len(p),len(p[0])
 def F(l,U):return{(p,t)for(p,v)in enumerate(l)for(t,o)in enumerate(v)if o==U}
 def d(I):p=I;v=min(p for(p,v)in p);t=min(p for(v,p)in p);return v,t
 def l(I):
  p=I
  if not p:return 0,0,-1,-1
  v=min(p for(p,v)in p);t=max(p for(p,v)in p);o=min(p for(v,p)in p);f=max(p for(v,p)in p);return v,o,t,f
 def a(l):return tuple(tuple(p)for p in zip(*l[::-1]))
 def M(l):return tuple(tuple(p[::-1])for p in l[::-1])
 def r(l):return tuple(tuple(p[::-1])for p in zip(*l[::-1]))[::-1]
 def B(I):
  p=I
  if not p:return set()
  v,t=d(p);return{(p-v,o-t)for(p,o)in p}
 def x(I):
  p=I
  if not p:return 0,0
  v,t,o,f=l(p);return o-v+1,f-t+1
 def U(l,U,I):
  p=[list(p)for p in l]
  for(v,t)in I:
   if 0<=v<c and 0<=t<c:p[v][t]=U
  return tuple(tuple(p)for p in p)
 v=F(p,1);h=F(p,4)
 if not v:return p
 z=min(p for(p,v)in v);G=max(p for(p,v)in v);t=min(p for(v,p)in v);e=max(p for(v,p)in v);u=z,t;t=tuple(tuple(p[v][t:e+1])for v in range(z,G+1));o=[t,a(t),M(t),r(t)]
 def z(l):return tuple(tuple(p[::-1])for p in l)
 o+=[z(p)for p in o];z=set()
 for J in o:
  o={(p,t)for(p,v)in enumerate(J)for(t,o)in enumerate(v)if o==4};f={(p,t)for(p,v)in enumerate(J)for(t,o)in enumerate(v)if o==1};y={(p+u[0],v+u[1])for(p,v)in o};G=h;t=d(o)if o else(0,0);e=d(f)if f else(0,0);q=e[0]-t[0];N=e[1]-t[1];K=B(o);H=B(f);X,k=x(K);e=c-X+1;L=c-k+1
  if e<0 or L<0:continue
  for f in range(e):
   for o in range(L):
    e={(p+f,v+o)for(p,v)in K};w={(p,v)for(p,v)in G if f<=p<f+X and o<=v<o+k}
    if w==e:P={(p+f+q,v+o+N)for(p,v)in H};z.update(P)
 i=U(p,1,z);return i
