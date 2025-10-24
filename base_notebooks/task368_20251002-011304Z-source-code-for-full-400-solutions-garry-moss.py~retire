def p(a,b=range):
 i=len(a);j=1;l,o=0,0;d=[0,5];q,g=0,0
 for p in b(i):
  for t in b(i):
   if a[p][t]not in d and j:
    j=0;q,g=p,t;h=p;n=t
    while h<i and a[h][t]not in d:h+=1
    while n<i and a[p][n]not in d:n+=1
    l=h-p;o=n-t
 for p in b(i-l+1):
  for t in b(i-o+1):
   if a[p][t]==5:
    for k in b(l):
     for s in b(o):a[p+k][t+s]=a[q+k][g+s]
 return a