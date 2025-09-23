def p(g,r=enumerate):
 def f():
  s=[0]*10
  for i,u in r(g):
   for j,v in r(u):
    if v!=8 and v:s[j]=v;g[i][j]=0
    if v==8:s=[k for k in s if k];g[i][j],g[i][j+1]=s[0],s[1];return
 for _ in 0,1:f();g=g[::-1]
 return g
