def p(x):
 if not x or not x[0]:return[o[:]for o in x]
 a=[o[:]for o in x];l,n=len(a),len(a[0]);from collections import Counter as x
 def g(b):o=x(a for o in b for a in o);return max(o,key=lambda x:o[x])
 def s(y,t):
  for o in(-1,0,1):
   for a in(-1,0,1):
    if o==0and a==0:continue
    i,m=y+o,t+a
    if 0<=i<l and 0<=m<n:yield(i,m)
 def i(b):
  o=b;u=g(o);n,k=len(o),len(o[0]);m,d=set(),[]
  for t in range(n):
   for x in range(k):
    if(t,x)in m:continue
    e=o[t][x]
    if e==u:continue
    r,l=set(),{(t,x)}
    while l:
     p=set()
     for(a,i)in l:
      if(a,i)in m:continue
      y=o[a][i]
      if y==e:r.add((a,i));m.add((a,i));[p.add((o,a))for(o,a)in s(a,i)if 0<=o<n and 0<=a<k]
     l=p-m
    if r:d.append((e,tuple(sorted(r))))
  return d
 def m(e):return min(o for(o,a)in e)
 def k(e):return min(o for(o,a)in e),min(o for(a,o)in e)
 def r(y):a,o=y;i,m=k(o);return a,tuple(sorted((o-i,a-m)for(o,a)in o))
 def c(y,t):o,a=y;i,m=t;return o,tuple(sorted((o+i,a+m)for(o,a)in a))
 f=g(a);x=i(a);e={}
 for(d,o)in x:e[o]=d
 d=[(a,o)for(o,a)in e.items()]
 if not d:return[o[:]for o in a]
 t=sorted(d,key=lambda y:(m(y[1]),k(y[1])[1]));p=m(t[0][1]);x=p
 for y in range(p+1,l):
  if any(a[y][o]!=f for o in range(n)):x=y
  elif x>=p:break
 e,u=set(),t[0][0]
 for(d,o)in t:
  if m(o)<=x:e.update(o)
  else:break
 b=min(o for(o,a)in e);q=min(o for(a,o)in e);p=tuple(sorted((o-b,a-q)for(o,a)in e));e=u,p
 def r(l):
  a=None;e,o,i=[],a,-1
  for(n,t)in l:
   r=m(t)
   if r<=x:continue
   l=max(o for(o,a)in t)
   if o is a or r>i+1:
    if o is not a:e.append((u,tuple(sorted(o))))
    o=set(t);i=l
   else:o.update(t);i=max(i,l)
  if o is not a:e.append((u,tuple(sorted(o))))
  return e
 t=r(t);y=[(0,2),(0,1),(0,0),(0,-1),(0,-2),(-1,0)];b=[]
 for(d,o)in t:t=k(o);x=c(e,t);x=[set(c(x,o)[1])for o in y];d=set(o);p=[(o,len(o&d),min(o for(o,a)in o)if o else u('inf'))for o in x];m=max(p,key=lambda k:(k[1],-k[2]));g=max(o for(a,o)in o);b.append((m[0]if m[1]>0else d,g))
 i=[o[:]for o in a]
 for(p,j)in b:
  for(y,r)in p:
   if r<=j:continue
   if 0<=y<l and 0<=r<n and i[y][r]==f:i[y][r]=1
 return i