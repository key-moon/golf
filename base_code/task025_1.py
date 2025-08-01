def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:d.setdefault(v,[]).append((i,j))
 s={}
 for c,a in d.items():
  if len(a)>1:
   i0,j0=a[0]
   if all(i==i0 for i,j in a):s[c]=('h',i0)
   else:s[c]=('v',j0)
 for c,(o,k) in s.items():
  for i,j in d[c]:
   if o=='v'and j!=k:
    dlt=(j>k)-(j<k);g[i][k+dlt]=c;g[i][j]=0
   if o=='h'and i!=k:
    dlt=(i>k)-(i<k);g[k+dlt][j]=c;g[i][j]=0
 return g