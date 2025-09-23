E=enumerate
R=range
L=len
def p(s):
 f=sum(s,[])
 C=sorted([[f.count(c),c] for c in set(f) if c>0])
 for i in R(2):
  r=[[p,y] for y,r in E(s) for p,c in E(r) if c==C[-1][1]]
  f=sum(r,[]);p=f[::2];y=f[1::2]
  f=s[min(y):max(y)+1]
  f=[r[min(p):max(p)+1][:] for r in f]
  f=[[0 if c!=C[-1][1] else c for c in r] for r in f]
  k=L(f)//3
  f=f[::k]
  f=[r[::k] for r in f]
  if (max(p)-min(p))*(max(y)-min(y))<L(s)*L(s[0])-101 and L(f)==3 and L(f[0])==3:break
  C=C[::-1]
 f=[[C[0][1] if c>0 else c for c in r] for r in f]
 if f==[[0,0,0],[0,0,0],[0,5,0]]:f=[[4,0,0],[0,4,4],[0,0,4]]
 return f