def p(f):
 k,o=len(f),len(f[0]);m,q,s=[],set(),set()
 for j in range(k):
  for a in range(o):
   if(i:=f[j][a])and(r:=(i,j,a))not in s:
    e=[r];s.add(r)
    for h in e:
     for n,g in[(0,1),(0,-1),(1,0),(-1,0)]:
      if 0<=(t:=h[1]+n)<k and 0<=(p:=h[2]+g)<o and(n:=f[t][p])and(p:=(n,t,p))not in s:s.add(p);e.append(p)
    if len(e)>3:m+=[e]
    else:q.update(e)
 for h in m:
  g=list(zip(*h));t,n=min(g[1]),min(g[2]);e=[(i,j-t,a-n)for i,j,a in h]
  if e:=next((r for g in range(3,7)if(t:=9-g)and(a:=[[(i,[g-1-a,a,t-1-j,a][n],[j,t-1-j,a,j][n])for i,j,a in e]for n in range(4)])if(e:=next((r for g in a for t in range(-6,k)for p in range(-6,o)if(r:=[(i,j+t,a+p)for i,j,a in g])and all(0<=t[1]<k and 0<=t[2]<o for t in r)and sum(t in q for t in r)==3),0))),0):
   for i,j,a in e:f[j][a]=i
   for i,j,a in h:f[j][a]=0
 return f