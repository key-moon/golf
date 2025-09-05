def p(g):
 o={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:t=o.setdefault(v,[i,i,j,j]);t[0]=min(t[0],i);t[1]=max(t[1],i);t[2]=min(t[2],j);t[3]=max(t[3],j)
 for v,(a,b,c,e) in o.items():
  for i in range(a,b+1):
   for j in range(c,e+1):g[i][j]=v
 return g