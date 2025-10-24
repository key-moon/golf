R=range
n=len
def p(i):
 o,r,t=n(i),n(i[0]),5
 for l in R(1,o-1):
  if sum(i[l])<1:t+=1
  for e in R(1,r-1):
   if i[l][e]and i[l-1][e]and i[l+1][e]and i[l][e-1]and i[l][e+1]==4:i[l][e]=t
 h=sum(i,[]);E=sorted([[h.count(l),l]for l in set(h)if l>4])
 for l in R(o):
  for e in R(r):
   if i[l][e]==E[0][1]:i[l][e]=1
   if i[l][e]==E[1][1]:i[l][e]=2
 return i