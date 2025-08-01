def p(g):
 t=range
 x=m=0
 for d in t(len(g)+1):
  for r in t(len(g[0])+1):
   for l in t(r):
    for u in t(d):
     s=[t[l:r]for t in g[u:d]]
     b=s[-1]+s[0]+[min(v[0],v[-1])for v in s]
     # m<(r-l)*(d-u) and len(set(b)) == 1 and 1 <= b[0]
     if (m<(r-l)*(d-u))==len(set(b))<=b[0]:
      m,x=(r-l)*(d-u),s
 c,n=sum(set(sum(x,[])))-x[0][0],len(x)
 for i in t(m):
  x[i%n][i//n]=x[i%n][i//n]and c
 return x
