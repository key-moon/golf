d=range
e=len
def p(b):
 i,i,t=e(b),e(b[0]),5
 for p in d(1,i-1):
  if sum(b[p])<1:t+=1
  for f in d(1,i-1):
   if b[p][f]and b[p-1][f]and b[p+1][f]and b[p][f-1]and b[p][f+1]==4:b[p][f]=t
 a=sum(b,[]);u=sorted([[a.count(p),p]for p in set(a)if p>4])
 for p in d(i):
  for f in d(i):
   if b[p][f]==u[0][1]:b[p][f]=1
   if b[p][f]==u[1][1]:b[p][f]=2
 return b