def p(r):
 n=[d[:]for d in r];k,k=len(r),len(r[0])
 for l in range(k):
  for p in range(k):
   if r[l][p]:
    m=r[l][p]
    for d in[(-1,-1),(-1,1),(1,1),(1,-1)]:
     g,i=l+d[0],p+d[1]
     while 0<=g<k and 0<=i<k:n[g][i]=m;g+=d[0];i+=d[1]
 return n