def p(g):
 a=range;q,y=len(g),len(g[0]);e={}
 for m in a(q):
  for i in a(y):
   if g[m][i]:e[g[m][i]]=e.get(g[m][i],0)+1
 d,f=max(e,key=e.get),min(e,key=e.get);h,r=0,None
 for m in a(q-2):
  for t in a(y-2):
   for u in a(m+2,q):
    for i in a(t+2,y):
     if all(g[m][a]==d for a in a(t,i+1))and all(g[u][a]==d for a in a(t,i+1))and all(g[a][t]==d for a in a(m,u+1))and all(g[a][i]==d for a in a(m,u+1)):
      p=(u-m+1)*(i-t+1)
      if p>h:h,r=p,(m,t,u,i)
 m,t,u,i=r;return[[f if g[m+u][t+a]==d else g[m+u][t+a]for a in a(i-t+1)]for u in a(u-m+1)]