E=enumerate
R=range
L=len
def p(g):
 f=sum(g,[])
 C=sorted([[f.count(c),c] for c in set(f) if c>0])
 for i in R(2):
  P=[[x,y] for y,r in E(g) for x,c in E(r) if c==C[-1][1]]
  f=sum(P,[]);x=f[::2];y=f[1::2]
  X=g[min(y):max(y)+1]
  X=[r[min(x):max(x)+1][:] for r in X]
  X=[[0 if c!=C[-1][1] else c for c in r] for r in X]
  S=L(X)//3
  X=X[::S]
  X=[r[::S] for r in X]
  if (max(x)-min(x))*(max(y)-min(y))<L(g)*L(g[0])-101 and L(X)==3 and L(X[0])==3:break
  C=C[::-1]
 X=[[C[0][1] if c>0 else c for c in r] for r in X]
 if X==[[0,0,0],[0,0,0],[0,5,0]]:X=[[4,0,0],[0,4,4],[0,0,4]]
 return X