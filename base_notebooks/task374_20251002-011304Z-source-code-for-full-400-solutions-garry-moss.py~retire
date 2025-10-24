def p(m):
 s=len(m);s=len(m[0]);q=[]
 for o in range(s):
  for p in range(s):
   if m[o][p]==5:
    l=[(o,p)];m[o][p]=0;e=[]
    while l:
     p,n=l.pop();e+=[(p,n)]
     for p,n in((p+1,n),(p-1,n),(p,n+1),(p,n-1)):
      if 0<=p<s and 0<=n<s and m[p][n]==5:m[p][n]=0;l+=[(p,n)]
    q+=e,
 for e,l in zip(sorted(q,key=len),(2,4,1)):
  for p,n in e:m[p][n]=l
 return m