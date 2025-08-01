def p(g):
 t,j=range,len
 x=m=0
 for d in t(j(g)+1):
  for r in t(j(g[0])+1):
   for l in t(r):
    for u in t(d):
     s=[t[l:r]for t in g[u:d]]
     b=s[-1]+s[0]+[min(v[0],v[-1])for v in s]
     # m<(r-l)*(d-u) and len(set(b)) == 1 and 1 <= b[0]
     if (m<(r-l)*(d-u))==j({*b})<=b[0]:
      m,x=(r-l)*(d-u),s
 c,n=sum({*sum(x,[])})-x[0][0],j(x)
 for i in t(m):
  x[i%n][i//n]=x[i%n][i//n]and c
 return x
