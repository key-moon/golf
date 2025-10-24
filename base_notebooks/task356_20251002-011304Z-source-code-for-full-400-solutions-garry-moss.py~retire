def p(o,d=range):
 o=[d[:]for d in o]
 for r in d(1,10):
  n=[(n,i)for n in d(len(o))for i in d(len(o[0]))if o[n][i]==r]
  for g in d(len(n)):
   for f in d(g+1,len(n)):
    i,m=n[g];e,f=n[f]
    if i==e:
     for e in d(min(m,f),max(m,f)+1):o[i][e]=r
    elif m==f:
     for i in d(min(i,e),max(i,e)+1):o[i][m]=r
 return o