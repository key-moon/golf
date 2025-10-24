f=range
t=len
def p(r):
 for l in f(4):
  r=list(map(list,zip(*r[::-1])))
  for l in f(t(r)):
   if len(set(r[l]))>2:e=[l for l in r[l]if l>0];g=r[l].index(e[0])%t(e);r[l]=e[-g:]+e*20;r[l]=r[l][:t(r[0])]
 return r