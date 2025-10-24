m=len
s=range
def p(u):
 f,a=m(u),m(u[0]);t=sum(u,[]);t=sorted([[t.count(e),e]for e in set(t)])[:2];i={t[0][1]:t[1][1],t[1][1]:t[0][1]}
 for e in range(50):
  for e in s(f):
   for r in s(a):
    if u[e][r]in i:
     for(g,n)in[[0,1],[0,-1],[1,0],[-1,0]]:
      if 0<=e+g<f and 0<=r+n<a and u[e+g][r+n]==0:u[e+g][r+n]=i[u[e][r]]
 return u