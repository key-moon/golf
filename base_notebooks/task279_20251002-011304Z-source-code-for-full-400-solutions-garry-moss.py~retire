from collections import deque
def p(l,t=range):
 i,r=len(l),len(l[0]);z=[[0]*r for n in t(i)];g={}
 for s in t(i):
  for p in t(r):
   if not z[s][p]:
    e=l[s][p];a=deque([(s,p)]);z[s][p]=1;f=[]
    while a:
     n,o=a.popleft();f.append((n,o))
     for(c,y)in((1,0),(-1,0),(0,1),(0,-1)):
      q,m=n+c,o+y
      if 0<=q<i and 0<=m<r and not z[q][m]and l[q][m]==e:z[q][m]=1;a.append((q,m))
    g.setdefault(e,[]).append(set(f))
 c=[n for n in g.get(9,[])if not any(n==0 or o==0 or n==i-1or o==r-1for(n,o)in n)];m=set()
 for q in c:m|=q
 f=[n[:]for n in l];e=g.get(1,[])
 if e and c:
  a=m
  for q in e:
   u=False
   for(n,o)in q:
    for(c,y)in((1,0),(-1,0),(0,1),(0,-1)):
     if(n+c,o+y)in a:u=True;break
    if u:break
   if u:
    for(n,o)in q:f[n][o]=8
 return f