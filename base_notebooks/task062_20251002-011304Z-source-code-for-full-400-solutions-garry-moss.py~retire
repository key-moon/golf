i=len
o=range
def p(l):
 n=sum(l,[]).count(2)
 for e in range(4):
  z,e=i(l),i(l[0]);l=list(map(list,zip(*l[::-1])))
  for e in o(z):
   if l[e].count(2)==n and sum(l[e])==2*n:
    for t in range(max(e,z-e)):
     if 0<=e+t<z and sum(l[e+t])>0and 2not in l[e+t]:
      if 0<=e-t+1<z and 0<=e+t<z:l[e-t+1]=l[e+t][:]
     elif 0<=e-t-1<z and 0<=e+t<z:l[e+t]=l[e-t-1][:]
 l=[[3if e==0else e for e in e]for e in l];return l