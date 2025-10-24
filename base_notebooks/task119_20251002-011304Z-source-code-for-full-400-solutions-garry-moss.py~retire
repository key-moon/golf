def p(b,d=range):
 o,o=len(b),len(b[0]);l=[e[:]for e in b];n=lambda e,n:e[::-1]if n>=2else e;n=lambda e,n:[list(e)for e in zip(*n(e,n))]if n%2else n(e,n);h=[(e,m)for e in d(o)for m in d(o)if b[e][m]==8]
 if not h:return l
 s,a=None,0
 for u in[0,1,2,3]:
  for c in[0,1]:
   for n in d(1,min(o//2,o//2)):
    for z in d(o):
     e=[[0]*o for e in d(o)]
     for r in d(n):
      for m in d(o):e[r][m]=2
     y=len(h)
     for m in d(o):
      r=n+abs(z-m)
      if 0<=r<o:e[r][m]=8if m<y else 3
     if c:e=[e[::-1]for e in e]
     e=e[::-1]if u>=2else e;e=[list(e)for e in zip(*e)]if u%2else e;f=sum(1for(m,o)in h if e[m][o]==8);g=[(e,m)for e in d(o)for m in d(o)if b[e][m]==2];i=sum(1for(m,o)in g if e[m][o]==2);f+=i/len(g)if g else 0
     if f>a:a,s=f,(u,c,n,z,y,e)
 if s:
  y,y,y,y,y,e=s
  for r in d(o):
   for m in d(o):
    if e[r][m]==3and b[r][m]==0:l[r][m]=3
 return l