L=len
R=range
E=enumerate
def M(m,C,Z):
 P=[[x,y] for y,r in E(m) for x,c in E(r) if c==C]
 f=sum(P,[]);x=f[::2];y=f[1::2]
 X=m[min(y):max(y)+1]
 X=[r[min(x):max(x)+1] for r in X]
 return sum(X,[]).count(Z)
def p(g):
 f=sum(g,[]);Z=sorted([[f.count(k),k] for k in set(f)])
 Z=[x[1] for x in Z]
 P=[M(g,Z[i],Z[0]) for i in R(1,L(Z))]
 return [[Z[P.index(max(P))+1]]]