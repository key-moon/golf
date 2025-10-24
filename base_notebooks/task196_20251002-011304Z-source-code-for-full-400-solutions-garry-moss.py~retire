def p(p):
 n=range;c,t=len(p),len(p[0]);r=set();o=[d[:]for d in p]
 def f(s,a):
  if(s,a)in r or not(0<=s<c and 0<=a<t)or p[s][a]!=1:return[]
  r.add((s,a));return[(s,a)]+sum([f(s+d,a+n)for(d,n)in[(-1,0),(1,0),(0,-1),(0,1)]],[])
 for s in n(c):
  for m in n(t):
   if p[s][m]==1and(s,m)not in r:
    d=f(s,m);s,m,l,y=min(d[0]for d in d),max(d[0]for d in d),min(d[1]for d in d),max(d[1]for d in d)
    if len(d)==2*(m-s+y-l)and m>s and y>l and any(p[d][r]==0for d in n(s+1,m)for r in n(l+1,y)):
     for(e,y)in d:o[e][y]=3
 return o