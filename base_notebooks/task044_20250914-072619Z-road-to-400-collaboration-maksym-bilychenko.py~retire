def p(g):
 v=set();R=[]
 for i in range(100):
  r,c=i//10,i%10
  if(r,c)in v:continue
  V=g[r][c];q=[(r,c)];C={(r,c)};v|={q[0]}
  for x,y in q:
   for n in[(x+d,y+e)for d,e in[(0,1),(0,-1),(1,0),(-1,0)]]:
    if 0<=n[0]<10>n[1]>=0 and n not in v and g[n[0]][n[1]]==V:v|={n};q+=[n];C|={n}
  R+=[(V,C)]
 F=[c for v,c in R if v==5];H=[];P=[]
 for v,c in R:
  if v==0:
   b=lambda s,i:[min,max][i>1](x[i%2]for x in s)
   if any(all(b(c,i)>=b(f,i)if i<2 else b(c,i)<=b(f,i)for i in range(4))for f in F):H+=[c]
  elif v>0 and v!=5:P+=[(v,c)]
 N=lambda s:frozenset((r-(m:=min(s))[0],c-m[1])for r,c in s)
 h={};p={}
 for x in H:k=N(x);h[k]=h.get(k,[])+[x]
 for v,x in P:k=N(x);p[k]=p.get(k,[])+[(v,x)]
 C={v:sum(1 for x,_ in P if x==v)for v,_ in P}
 for k,L in h.items():
  if k in p:
   Q=p[k]
   if len(Q)>1 and C:Q=[x for x in Q if x[0]!=max(C,key=C.get)]or Q
   for a,(v,b)in zip(L,Q):
    for r,c in b:g[r][c]=0
    for r,c in a:g[r][c]=v
 return g