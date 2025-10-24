def p(e,x=enumerate):
 z=[[0]*len(e[0])for a in e]
 for r in{*sum(e,[])}-{0}:
  o=[(q,a)for q,a in x(e)for a,e in x(a)if e==r];p,n=map(max,zip(*o))
  for q,a in o:z[q][a+(q<p)*(a<n)]=r
 return z