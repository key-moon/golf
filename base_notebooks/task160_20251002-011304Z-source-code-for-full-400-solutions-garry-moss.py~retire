u=range
d=len
def p(p):
 q,q=d(p),d(p[0])
 for l in u(q-2):
  for i in u(q-2):
   if p[l][i]==1and sum(p[l][i:i+3]+p[l+1][i:i+3]+p[l+2][i:i+3])==8:
    for k in u(3):
     for t in u(3):p[l+k][i+t]=2
     p[l][i]=0;p[l][i+2]=0;p[l+2][i]=0;p[l+2][i+2]=0
 return p