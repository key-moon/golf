def p(o,r=enumerate):
 a=f=9**9;p=i=-1
 for h,j in r(o):
  for t,d in r(j):
   if d:a=min(a,h);p=max(p,h);f=min(f,t);i=max(i,t)
 u=a+p;l=f+i
 for h in range(a,p+1):
  for t in range(f,i+1):
   r=u-h;t=l-t;m=a+t-f;d=f+h-a;m=a+i-t;j=f+p-h
   r=((h,t),(h,t),(r,t),(r,t),(m,d),(m,d),(m,j),(m,j))
   e=max(o[r][m]for r,m in r)
   for r,m in r:o[r][m]=e
 return o