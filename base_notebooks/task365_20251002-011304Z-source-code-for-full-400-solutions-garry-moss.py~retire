def p(a):
 n,n=len(a),len(a[0]);i=-1
 for d in range(n):
  for t in range(n):
   if a[d][t]and(d<1or a[d-1][t]<1)and(t<1or a[d][t-1]<1):
    f=o=1
    while t+f<n and a[d][t+f]:f+=1
    while d+o<n and a[d+o][t]:o+=1
    u=[d[t:t+f]for d in a[d:d+o]];f=sum(d.count(2)for d in u)
    if f>i:i=f;l=u
 return l