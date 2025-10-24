def p(f,g=range):
 i,l=len(f),len(f[0]);b,e,a,t=i,0,l,0
 for r in g(i):
  for p in g(l):
   if f[r][p]-1:
    if r<b:b=r
    if r>e:e=r
    if p<a:a=p
    if p>t:t=p
 return[[g-(g==1)for g in g[a:t+1]]for g in f[b:e+1]]