D=any
C=abs
B=len
A=range
def p(g):
 u=[];u=[(i,j,g[i][j])for i in A(B(g))for j in A(B(g[0]))if g[i][j]|2==3or g[i][j]*D(C(y-i)<2>C(x-j)for(y,x,_)in u)];u=[(i,j,g[i][j])for i in A(B(g))for j in A(B(g[0]))if g[i][j]|2==3or g[i][j]*D(C(y-i)<2>C(x-j)for(y,x,_)in u)];u=[(i,j,g[i][j])for i in A(B(g))for j in A(B(g[0]))if g[i][j]|2==3or g[i][j]*D(C(y-i)<2>C(x-j)for(y,x,_)in u)];u=[(i,j,g[i][j])for i in A(B(g))for j in A(B(g[0]))if g[i][j]|2==3or g[i][j]*D(C(y-i)<2>C(x-j)for(y,x,_)in u)];u=[(i,j,g[i][j])for i in A(B(g))for j in A(B(g[0]))if g[i][j]|2==3or g[i][j]*D(C(y-i)<2>C(x-j)for(y,x,_)in u)]
 for _ in A(12):
  for i in A(-12,13):
   for j in A(-12,13):
    if sorted(g[y+i][x+j]for(y,x,v)in u if B(g)>y+i>-1<x+j<B(g[0])if v==g[y+i][x+j]>0)[:6]==[2,4,4,4,4,4]:
     for(y,x,v)in u:g[y+i][x+j]=v
  g[:]=map(list,zip(*g[::1-_%3|1]))
 return g