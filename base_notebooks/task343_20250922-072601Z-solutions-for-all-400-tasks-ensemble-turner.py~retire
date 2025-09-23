def p(x):
 s=max({e:sum(o.count(e)for o in x)for e in sum(x,[])}.items(),key=lambda e:e[1])[0];i=[[0]*15for p in range(5)];v=[]
 for o in range(5):
  for r in range(15):
   if not i[o][r]and x[o][r]!=s:
    y=[(o,r)];u=[]
    while y:
     e,f=y.pop()
     if 5>e>=0<=f<15and not i[e][f]and x[e][f]!=s:i[e][f]=1;u+=[(e,f)];y+=[(e+n,f+q)for n,q in[(0,1),(0,-1),(1,0),(-1,0)]]
    if u:v.append({(x[o][v],(o,v))for o,v in u})
 t=v[0];i,s=min(k[0]for p,k in t),min(k[1]for p,k in t);v={(i,(k[0]-i,k[1]-s))for i,k in t};c=max(k[1]for p,k in v)+1;k=next((r for r in range(1,c)if {(i,(e,f-r))for i,(e,f)in v if f-r>=0}.issubset(v)),c)
 for i,(e,f)in t:
  b=k
  while f+b<15:x[e][f+b]=i;b+=k
 return x