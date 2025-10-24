def p(r,c=range):
 e,e=len(r),len(r[0]);l={};[[l.update({f:l.get(f,0)+1})for f in f]for f in r];a=max(l,key=l.get);d=[[0]*e for f in c(e)];t=[]
 for u in c(e):
  for j in c(e):
   if not d[u][j]and r[u][j]!=a:
    f=[];p=[(u,j)];l=r[u][j]
    while p:
     j,u=p.pop()
     if 0<=j<e and 0<=u<e and not d[j][u]and r[j][u]==l:d[j][u]=1;f.append((j,u));p.extend([(j+f,u+l)for(f,l)in[(0,1),(1,0),(0,-1),(-1,0)]])
    f and t.append(f)
 j=[]
 for f in t:
  if f:s,n,u,e=min(f[0]for f in f),max(f[0]for f in f),min(f[1]for f in f),max(f[1]for f in f);l=set((f,l)for f in c(s,n+1)for l in c(u,e+1));l=list(l-set(f));l and j.append(l)
 p=[]
 for l in j:
  if l:s,n,u,e=min(f[0]for f in l),max(f[0]for f in l),min(f[1]for f in l),max(f[1]for f in l);e,e=n-s+1,e-u+1;e==e and len(l)==e*e and p.extend(l)
 a=[f[:]for f in r]
 for(u,j)in p:0<=u<len(a)and 0<=j<len(a[0])and a.__setitem__(u,a[u][:j]+[2]+a[u][j+1:])
 return a