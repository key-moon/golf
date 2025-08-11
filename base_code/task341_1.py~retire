def p(g):
 s={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:
    t=s.setdefault(v,[i,i,j,j])
    t[0]=min(t[0],i);t[1]=max(t[1],i);t[2]=min(t[2],j);t[3]=max(t[3],j)
 a,b=s.values()
 f=lambda a,b,c,d:range(b+1,c)if b<c else range(d+1,a)if d<a else range(max(a,c)+1,min(b,d))
 for i in f(*a[:2],*b[:2]):
  for j in f(*a[2:],*b[2:]):g[i][j]=8
 return g
