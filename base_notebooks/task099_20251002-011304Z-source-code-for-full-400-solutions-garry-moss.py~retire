def p(r,p=range):
 from collections import deque,Counter as N;k,f=len(r),len(r[0]);l=N(n for e in r for n in e).most_common(1)[0][0];m=[e[:]for e in r];t=[[0]*f for e in p(k)]
 for n in p(k):
  for n in p(f):
   if r[n][n]==1and not t[n][n]:
    o=deque([(n,n)]);t[n][n]=1;e=[]
    while o:
     b,n=o.popleft();e.append((b,n))
     for(j,d)in((1,0),(-1,0),(0,1),(0,-1)):
      q,c=b+j,n+d
      if 0<=q<k and 0<=c<f and not t[q][c]and r[q][c]==1:t[q][c]=1;o.append((q,c))
    u=min(e for(e,n)in e);j=max(e for(e,n)in e);i=min(e for(n,e)in e);x=max(e for(n,e)in e);g=set(e);s=[r[e][n]for e in p(u,j+1)for n in p(i,x+1)if(e,n)not in g]
    if not s:continue
    e=N(s);g=min(e.values());s=min(e for(e,n)in e.items()if n==g)
    for b in p(u,j+1):
     M=b-1
     if 0<=M<k:
      for n in p(i,x+1):
       if m[M][n]==l:m[M][n]=s
 return m