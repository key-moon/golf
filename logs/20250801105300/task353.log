def p(g):
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==3:a,b=i,j
   if v==4:c,d=i,j
 dr=(c>a)-(c<a);dc=(d>b)-(d<b);g[a][b]=0;g[a+dr][b+dc]=3;return g