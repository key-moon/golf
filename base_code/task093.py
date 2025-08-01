def p(g):
 m,n=len(g),len(g[0]);a=m;b=-1;c=n;d=-1
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==5:
    if i<a:a=i
    if i>b:b=i
    if j<c:c=j
    if j>d:d=j
 f=[[0]*n for _ in g]
 for i in range(a,b+1):f[i][c:d+1]=[5]*(d-c+1)
 if b-a>d-c:
  for i,r in enumerate(g):
   for j,v in enumerate(r):
    if v%5:
     if j<c:f[i][c-1]=5
     if j>d:f[i][d+1]=5
 else:
  for i,r in enumerate(g):
   for j,v in enumerate(r):
    if v%5:
     if i<a:f[a-1][j]=5
     if i>b:f[b+1][j]=5
 return f
