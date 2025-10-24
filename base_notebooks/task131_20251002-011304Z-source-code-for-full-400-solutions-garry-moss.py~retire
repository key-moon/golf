i=lambda d:[[d[n][b]for n in range(len(d))]for b in range(len(d[0]))]
def p(d):
 m,b=len(d),len(d[0])
 if b>m:return i(p(i(d)))
 t,e,u=0,m,0
 for n,r in enumerate(d):
  if r[0]==2:t=n
  if any(n==3for n in r):e,u=min(e,n),n
 if e<t:return p(d[::-1])[::-1]
 return d[:t+1]+d[e:u+1]+[[8]*b]+[[0]*b]*(m-t+e-u-3)