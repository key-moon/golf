def p(r):
 o=None;F=range;a=lambda c:[list(e)for e in zip(*c)];z=r;o=0
 if not any(all(e==8for e in e)for e in r):z,o=a(r),1
 i,c=len(z),len(z[0]);f=[e[:]for e in z];d=[e for e in F(i)if all(e==8for e in z[e])]
 for n in F(i):
  for p in F(c):
   if z[n][p]!=2:continue
   for e in(max([e for e in d if e<n],default=o),min([e for e in d if e>n],default=o)):
    if e is o:continue
    for r in(e-1,e,e+1):
     if 0<=r<i:
      for m in(p-1,p,p+1):
       if 0<=m<c:f[r][m]=2if r==e and m==p else 8
    u=1-2*(e<n)
    for r in F(n,e-u,u):f[r][p]=2
 return a(f)if o else f