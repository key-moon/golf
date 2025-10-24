n=range
x=len
def p(i):
 f,f=x(i),x(i[0])
 for e in n(1,f-1):
  for d in n(1,f-1):
   r=[i[e+l][d+a]for l,a in[[0,0],[0,1],[1,0],[1,1]]]
   t=max(r)
   if sum([1for u in r if u>0])>2:
    m=r.index(0)
    for u in n(1,10):
     if m<2:l=e-u
     else:l=e+u+1
     if m%2:a=d+u+1
     else:a=d-u
     if 0<=l<f and 0<=a<f:i[l][a]=t
 return i