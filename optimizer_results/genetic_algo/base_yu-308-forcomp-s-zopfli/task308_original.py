D=min
C=len
B=max
A=range
def p(g):
 *E,b=sorted({*sum(g,[])},key=sum(g,[]).count);u=0
 for c in E:
  y=[i for i in A(C(g))for j in A(C(g[0]))if g[i][j]==c];x=[j for i in A(C(g))for j in A(C(g[0]))if g[i][j]==c];s=B(B(y)-D(y),B(x)-D(x))+1
  if u==0:u=[[b]*s for _ in A(s)]
  for(i,j)in zip(y,x):u[i+(s-B(y)-D(y))//2][j+(s-B(x)-D(x))//2]=c
 return u