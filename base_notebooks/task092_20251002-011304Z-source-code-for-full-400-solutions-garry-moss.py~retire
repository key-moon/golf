def p(d,n=len,o=range):
 l=None;t,l=n(d),n(d[0]);f=[m[:]for m in d]
 for m in o(t):
  s=q=l
  for p in o(l):
   if d[m][p]:
    if s is not l and d[m][p]==q:
     for n in o(s+1,p):f[m][n]=q
    s=p;q=d[m][p]
 for p in o(l):
  s=q=l
  for m in o(t):
   if d[m][p]:
    if s is not l and d[m][p]==q:
     for n in o(s+1,m):f[n][p]=q
    s=m;q=d[m][p]
 return f