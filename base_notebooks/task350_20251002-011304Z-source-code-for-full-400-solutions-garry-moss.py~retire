def p(a,m=range):
 l=[m[:]for m in a]
 for e in m(1,10):
  f=[(n,f)for n in m(len(a))for f in m(len(a[0]))if a[n][f]==e]
  for i in m(len(f)):
   for e in m(i+1,len(f)):
    n,o=f[i];e,x=f[e]
    if n==e:
     for e in m(min(o,x),max(o,x)+1):l[n][e]=8
    elif o==x:
     for n in m(min(n,e),max(n,e)+1):l[n][o]=8
  for(n,e)in f:l[n][e]=1
 return l