def p(o,d=range):
 if not o or not o[0]:return[list(f)for f in o]
 f=tuple(tuple(f)for f in o);h,b=len(f),len(f[0]);p=lambda u:(min(f for(f,q)in u),min(f for(q,f)in u),max(f for(f,q)in u),max(f for(q,f)in u))if u else(0,0,0,0);i=lambda u:{(f-p(u)[0],q-p(u)[1])for(f,q)in u}if u else set();u=tuple(tuple(f[::-1])for f in f);from collections import Counter as f;j=max(f(sum(u,())).items(),key=lambda a:a[1])[0];f={};[f.setdefault(u[q][s],set()).add((q,s))for q in d(h)for s in d(b)if u[q][s]!=j]
 if not f:return[list(f)for f in f]
 s=max(f,key=lambda h:len(f[h]));h=i(f[s]);q=None
 for(r,o)in f.items():
  if r==s or len(o)==len(f[s]):continue
  o=i(o);l={(2*f+s,2*q+o)for(f,q)in o for s in(0,1)for o in(0,1)}
  if l and h:g,g,m,m=[f for(f,q)in l],[f for(q,f)in l],[f for(f,q)in h],[f for(q,f)in h];a=max(sum((s+f,o+q)in h for(s,o)in l)for f in d(min(m)-max(g),max(m)-min(g)+1)for q in d(min(m)-max(g),max(m)-min(g)+1))
  else:a=0
  b=a-2*len(o),len(o),p(o)[3],r;q=b if q is None or b>q else q
 m=q[3]if q else(lambda f:max(f,key=lambda h:len(f[h]))if f else s)([f for f in f if f!=s]);i,k,f,b=p(f[m]);p=[list(u[f][k:b+1])for f in d(i,f+1)];[[f.__setitem__(q,j)for q in d(len(f))if f[q]!=m]for f in p];return[list(f[::-1])for f in p]