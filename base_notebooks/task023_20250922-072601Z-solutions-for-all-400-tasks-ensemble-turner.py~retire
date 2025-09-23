def z(s,t,a):
 if not s:return t
 for i,(p,s,a)in enumerate(a):
  a=set(f(p,s,a))
  if a&s and not a&set(sum([f(z,y,s)for z,y,s in t],[])):
   if k:=z(s-a,t+[(p,s,a)],a[i+1:]):return k
def p(t):
 from itertools import combinations as b;u,z=len(t),len(t[0]);f=lambda p,s,i:[(p,s),(p,s+1),(p+1,s),(p+1,s+1)]if i<1 else[(p,s),(p+1,s),(p+2,s)]if i<2 else[(p,s),(p,s+1),(p,s+2)];a=[(p,s,i)for i in range(3)for p in range(u-(1,2,0)[i])for s in range(z-(1,0,2)[i])if all(0<=a<u and 0<=s<z and t[a][s]==5 for a,s in f(p,s,i))];y={(p,s)for p in range(u)for s in range(z)if t[p][s]==5};p=lambda t:len(a:=sum([f(p,s,i)for p,s,i in t],[]))==len(set(a))and set(a)==y;i=next((c for s in range(1,min(len(a)+1,10))for c in b(a,s)if p(c)),None)
 if not i:
  i=z(y,[],a)or[]
 if not i:c,i=set(),[];[(i.append((p,s,i)),c.update(a))for p,s,i in sorted(a,key=lambda a:(a[2],a[0],a[1]))if not(a:=set(f(p,s,i)))&c]
 [t[a].__setitem__(s,8 if i<1 else 2)for p,s,i in i for a,s in f(p,s,i)if 0<=a<u and 0<=s<z];return t