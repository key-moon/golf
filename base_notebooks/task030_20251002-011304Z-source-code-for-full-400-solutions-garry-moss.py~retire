def p(g,y=len,i=range):
 r,l,n,f,t=y(g),y(g[0]),[],[],[]
 for d in i(r):
  for m in i(l):
   y=g[d][m]
   if y==2:n+=[m];g[d][m]=0
   if y==4:f+=[m];g[d][m]=0
   if y==1:t+=[m]
 for d in i(r):
  for m in i(l):
   if g[d][m]==1:g[d][m+(min(f)-min(t))]=4;g[d][m+(min(n)-min(t))]=2
 return g