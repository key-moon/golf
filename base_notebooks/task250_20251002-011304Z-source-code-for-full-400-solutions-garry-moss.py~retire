from itertools import*
n=len
l=range
t=list(product([0,1,-1],repeat=2))
def p(p):
 d,d=n(p),n(p[0])
 for o in l(d):
  for r in l(d):
   if p[o][r]==2:
    for(e,m)in t:
     if 0<=o+e<d and 0<=r+m<d:
      for s in l(20):
       if 0<=o+e*s<d and 0<=r+m*s<d:
        a=p[o+e*s][r+m*s]
        if a==5and p[o+e][r+m]==0:p[o+e][r+m]=5;p[o+e*s][r+m*s]=0
 return p