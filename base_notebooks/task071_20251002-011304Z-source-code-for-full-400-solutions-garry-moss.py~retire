def p(n):
 from collections import defaultdict as a
 def p(l):
  if not l:return False
  l,a=zip(*l);return len(l)==(max(l)-min(l)+1)*(max(a)-min(a)+1)
 d,f=len(n),len(n[0]);l=a(list)
 for a in range(d):
  for c in range(f):
   if n[a][c]:l[n[a][c]].append((a,c))
 if not l:return[[0]*f for l in range(d)]
 o=max([l for(l,a)in l.items()if p(a)],key=lambda a:len(l[a]),default=None);t=max([a for a in l if a!=o and not p(l[a])]or[l for l in l if l!=o],key=lambda a:len(l[a]));a,e=l[t],set(l[t]);x=set(l[o])if o else set();x=max(range(2*f-1),key=lambda o:sum(1for(a,c)in a if 0<=(l:=o-c)<f and((a,l)in e or(a,l)in x)),default=min(l for(a,l)in a)+max(l for(a,l)in a));n=[[0]*f for l in range(d)]
 for(a,c)in a:n[a][c]=t
 if o:
  for(a,c)in l[o]:
   if 0<=(m:=x-c)<f and(a,m)in e:n[a][c]=t
 return n