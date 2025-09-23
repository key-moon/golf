i=lambda r:[[r[n][x]for n in range(len(r))]for x in range(len(r[0]))]
def p(r):
 c,x=len(r),len(r[0])
 if x>c:return i(p(i(r)))
 d,e,l=0,c,0
 for n,a in enumerate(r):
  if a[0]==2:d=n
  if any(n==3 for n in a):e,l=min(e,n),n
 if e<d:return p(r[::-1])[::-1]
 return r[:d+1]+r[e:l+1]+[[8]*x]+[[0]*x]*(c-d+e-l-3)