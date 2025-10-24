def p(e,c=range):
 d,m=len(e),len(e[0]);g=sum(e,[]);l={};[l.update({s:l.get(s,0)+1})for s in g];b=max(l,key=l.get);z=[[0]*m for s in c(d)];y=[]
 for p in c(d):
  for x in c(m):
   if not z[p][x]and e[p][x]!=b:
    g=[];n=[(p,x)];s=e[p][x]
    while n:
     r,f=n.pop()
     if r<0 or r>=d or f<0 or f>=m or z[r][f]or e[r][f]!=s:continue
     z[r][f]=1;g.append((r,f));n.extend([(r+s,f+t)for(s,t)in[(0,1),(0,-1),(1,0),(-1,0)]])
    g and y.append(frozenset((s,t)for t in g))
 u,i=[],[]
 for t in y:
  p=[s for(t,s)in t]
  if p:z,p,y,a=min(s[0]for s in p),max(s[0]for s in p),min(s[1]for s in p),max(s[1]for s in p);n,p=p-z+1,a-y+1;o=[[e[z+s][y+t]if 0<=z+s<d and 0<=y+t<m else 0for t in c(p)]for s in c(n)];l=[[o[s][t]for t in c(1,p-1)]for s in c(1,n-1)]if n>2and p>2else[];z=set(sum(l,[]));3in z and u.append(t);len(t)==n+p-1and i.append(t)
 b=[[6if s==3else s for s in s]for s in e]
 for t in u:
  for(p,(t,s))in t:0<=t<d and 0<=s<m and b.__setitem__(t,b[t][:s]+[2]+b[t][s+1:])
 for t in i:
  for(p,(t,s))in t:0<=t<d and 0<=s<m and b.__setitem__(t,b[t][:s]+[1]+b[t][s+1:])
 return b