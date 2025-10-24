def p(r):
 l,l=len(r),len(r[0]);p=[(o,h)for o in(-4,0,4)for h in(-4,0,4)if o|h];t=range;f=[l]*10;a=[l]*10;s=[-1]*10;j=[-1]*10
 for h in t(l):
  for n in t(l):
   o=r[h][n]
   if n<f[o]:f[o]=n
   if h<a[o]:a[o]=h
   if n>s[o]:s[o]=n
   if h>j[o]:j[o]=h
 for o in t(1,10):
  if s[o]-f[o]==2and j[o]-a[o]==2:c,e=f[o],a[o];break
 a=[[0]*l for o in r]
 for o in t(3):a[e+o][c:c+3]=r[e+o][c:c+3]
 q=[(h,o)for o in t(3)for h in t(3)if r[e+o][c+h]]
 for(f,s)in p:
  n=c+f;h=e+s;o=0
  for p in t(3):
   for j in t(3):
    i,b=n+j,h+p
    if 0<=i<l and 0<=b<l and r[b][i]:o=r[b][i];break
   if o:break
  if not o:continue
  n=c;h=e
  while 1:
   n+=f;h+=s
   if not(-3<n<l and-3<h<l):break
   for(j,p)in q:
    i,b=n+j,h+p
    if 0<=i<l and 0<=b<l:a[b][i]=o
 return a