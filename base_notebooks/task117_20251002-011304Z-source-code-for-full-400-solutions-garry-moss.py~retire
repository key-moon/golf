def p(I):
 f=False;p=None;s=True;o,t=len(I),len(I[0])
 def a(f):s=[B for s in f for B in s];return max(set(s),key=s.count)
 def b(f):return tuple(tuple(s)for s in zip(*f[::-1]))
 def c(f):return f[::-1]
 def d(f):return tuple(tuple(s[::-1])for s in f)
 def B(k):s=[s for(s,B)in k];B=[s for(B,s)in k];return min(s),min(B),max(s),max(B)
 def K(k):s,C,p,t=B(k);return s+(p-s)//2,C+(t-C)//2
 def x(f,o,l,d,a):return tuple(tuple(f[s][l:a+1])for s in range(o,d+1))
 def e(f,t):
  s=[list(s)for s in f]
  for(p,(B,C))in t:
   if 0<=B<len(s)and 0<=C<len(s[0]):s[B][C]=p
  return tuple(tuple(s)for s in s)
 def Q(t,di,d):return{(s,(B+di,C+d))for(s,(B,C))in t}
 def t(f,x=s,s=s):
  B=s;C=a(f)if B else p;t,k=len(f),len(f[0])
  if x:
   j=sorted({f[s][p]for s in range(t)for p in range(k)if not B or f[s][p]!=C});I=[]
   for z in j:
    if B and z==C:continue
    s=[(s,B)for s in range(t)for B in range(k)if f[s][B]==z]
    if s:I.append({(z,(s,B))for(s,B)in s})
   return I
  else:
   s=[(s,p)for s in range(t)for p in range(k)if not B or f[s][p]!=C]
   if B:s=[(s,B)for(s,B)in s if f[s][B]!=C]
   if not s:return[]
   return[{(f[s][B],(s,B))for(s,B)in s}]
 def L(f,t):k=[(s,B)for(C,(s,B))in t];s,C,p,t=B(k);return x(f,s,C,p,t),(s,C,p,t)
 def r(t,f):s,B=L(f,t);return s==b(s)
 o=t(I,x=s,s=s);q=sorted(o,key=lambda o:B([s for(B,s)in o]));z=p
 for C in q:
  if r(C,I):z=C;break
 if z is p:return I
 j=K([s for(B,s)in z]);u=t(I,x=f,s=s)
 if not u:return I
 s=sorted(u,key=lambda o:B([s for(B,s)in o]))[0];s,h=L(I,s);M=c(s);T=t(M,x=f,s=s)
 if not T:return I
 k=sorted(T,key=lambda o:B([s for(B,s)in o]))[0];l=t(M,x=s,s=s);u=p
 for C in sorted(l,key=lambda o:B([s for(B,s)in o])):
  if r(C,M):u=C;break
 if u is p:return I
 b=K([s for(B,s)in u]);s,b=j[0]-b[0],j[1]-b[1];k=e(I,Q(k,s,b));s=t(k,x=f,s=s)
 if not s:return k
 o=sorted(s,key=lambda o:B([s for(B,s)in o]))[0];p,h=L(k,o);s=d(p);u=t(s,x=f,s=s)
 if not u:return k
 q=sorted(u,key=lambda o:B([s for(B,s)in o]))[0];i=t(s,x=s,s=s)
 if not i:return k
 a=next(iter(z))[0];u=p
 for C in sorted(i,key=lambda o:B([s for(B,s)in o])):
  if next(iter(C))[0]==a:u=C;break
 if u is p:return k
 t=K([s for(B,s)in u]);s,t=j[0]-t[0],j[1]-t[1];return e(k,Q(q,s,t))