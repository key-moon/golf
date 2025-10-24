def p(h,f=range):
 d=None;e=False;m,t=len(h),len(h[0]);from collections import Counter as b;d=b(y for n in h for y in n);n=min(d,key=d.get);i=[(y,p)for y in f(m)for p in f(t)if h[y][p]==n]
 if not i:return[n[:]for n in h]
 d=min(n for(n,y)in i);c=min(n for(y,n)in i);l=max(n for(n,y)in i);u=max(n for(y,n)in i);j=l-d+1;k=u-c+1;o=max(1,j-2);i=max(1,k-2)
 def d(a,s):
  for y in f(s,s+k):
   if h[a][y]!=n or h[a+j-1][y]!=n:return e
  for p in f(a,a+j):
   if h[p][s]!=n or h[p][s+k-1]!=n:return e
  return True
 a=d
 for y in f(m-(o+2)+1):
  for p in f(t-(i+2)+1):
   x=True
   for c in f(y+1,y+o+1):
    l=h[c]
    for u in f(p+1,p+i+1):
     if l[u]!=0:x=e;break
    if not x:break
   if x:
    if a is d or d(*a)and not d(y,p):a=y,p
 if a is d:return[n[:]for n in h]
 y,p=a;j=o+2;k=i+2;t=[n[:]for n in h]
 for u in f(p,p+k):t[y][u]=n;t[y+j-1][u]=n
 for c in f(y,y+j):t[c][p]=n;t[c][p+k-1]=n
 return t