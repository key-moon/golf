E=enumerate
R=range
L=len
def p(g):
 P=[[x,y] for y,r in E(g) for x,c in E(r) if c==3]
 f=sum(P,[]);x=f[::2];y=f[1::2]
 M=[min(y)+1,max(y)-1,min(x)+1,max(x)-1]
 P=[[x,y] for y,r in E(g) for x,c in E(r) if c==2]
 f=sum(P,[]);x=f[::2];y=f[1::2]
 M[0]-=min(y)
 M[1]-=max(y)
 M[2]-=min(x)
 M[3]-=max(x)
 X=[r[:] for r in g]
 g=[[0 if c!=3 else 3 for c in r] for r in g]
 for r in R(L(g)):
  for c in R(L(g[0])):
   if X[r][c]==2:
    g[r-min([M[0],0])+max([M[1],0])][c-min([M[2],0])+max([M[3],0])]=2
 return g