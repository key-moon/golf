def p(p):
 y=len(p);y=len(p[0]);t=[]
 for a in range(y):
  for d in range(y):
   if p[a][d]==5:
    i=[(a,d)];p[a][d]=0;g=[]
    while i:
     d,n=i.pop();g+=[(d,n)]
     for d,n in((d+1,n),(d-1,n),(d,n+1),(d,n-1)):
      if 0<=d<y and 0<=n<y and p[d][n]==5:p[d][n]=0;i+=[(d,n)]
    t+=g,
 for g,l in zip(sorted(t,key=len),(2,4,1)):
  for d,n in g:p[d][n]=l
 return p