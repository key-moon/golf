def p(l):
 from collections import deque,Counter as c;f,p=range,len;z,z=p(l),p(l[0]);g=[[0]*z for i in f(z)];g=[[0]*z for i in f(z)]
 for a in f(z):
  for i in f(z):
   if l[a][i]and not g[a][i]:
    r=deque([(a,i)]);g[a][i]=1;p=[];m=c()
    while r:
     i,y=r.popleft();p.append((i,y));m[l[i][y]]+=1
     for(j,s)in((1,0),(-1,0),(0,1),(0,-1)):
      i,n=i+j,y+s
      if 0<=i<z and 0<=n<z and l[i][n]and not g[i][n]:g[i][n]=1;r.append((i,n))
    b,j=[i for(i,y)in m.most_common(2)];d=[(i,y)for(i,y)in p if l[i][y]==j];t,o,n=min(i for(i,y)in d),min(i for(y,i)in d),max(i for(i,y)in d)-min(i for(i,y)in d)+1
    for i in f(t-n-1,t+2*n+1):
     for y in f(o-n-1,o+2*n+1):
      if(i<t-1or i>t+n)and(y<o-1or y>o+n):continue
      g[i][y]=b
    for i in f(t-1,t+n+1):
     for y in f(o-1,o+n+1):g[i][y]=j
    for i in f(t,t+n):
     for y in f(o,o+n):g[i][y]=b
 return g