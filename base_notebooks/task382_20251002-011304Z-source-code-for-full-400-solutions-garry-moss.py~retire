d=range
o=len
def p(r,p=1):
 for t in d(4):
  r=list(map(list,zip(*r[::-1])))
  f,i=o(r),o(r[0])
  if p:
   for t in d(f):
    if r[t][0]==8and r[0].count(2)+r[-1].count(2)>0:
     p=0
     for e in d(i):
      if r[0][e]==2:p+=1
      if r[-1][e]==2:p-=1
      if 0<=t+p<f:r[t+p][e]=8
     p=0
 return r