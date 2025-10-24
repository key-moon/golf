def p(o,u=enumerate,x=range):
 f=[f[:]for f in o];n=len(f);m=len(f[0]);z=[c for f in f for(c,g)in u(f)if g==2]
 if not z:return f
 r=min(z);t=max(z);z=[f for(f,c)in u(f)if 2in c];l=min(z);e=max(z);z=[f for(f,c)in u(f)if all(c[f]==2for f in x(r,t+1))];c=bool(z)
 if c:
  l=min(z);e=max(z)
  for g in x(l+1,e):
   z=[c for c in x(r+1,t)if f[g][c]==5]
   if not z:continue
   for c in z:f[g][c]=0
   c=g-l;u=e-g
   if c<=u:
    j=l-c
    if 0<=j<n:
     for c in z:f[j][c]=5
   else:
    j=e+u
    if 0<=j<n:
     for c in z:f[j][c]=5
 else:
  for g in x(l,e+1):
   z=[c for c in x(r+1,t)if f[g][c]==5]
   if not z:continue
   for c in z:
    j=c-r;d=t-c
    if j<=d:z=r-j
    else:z=t+d
    if 0<=z<m:f[g][z]=5
    f[g][c]=0
 return f