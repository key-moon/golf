C=any
B=len
A=range
def p(g):
 u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==1];u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in u for y in A(-1,2)for x in A(-1,2))];u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in u for y in A(-1,2)for x in A(-1,2))];c=[]
 for i in A(B(g)):
  c+=[0]*B(g[0]),
  for j in A(B(g[0])):
   if g[i][j]==2and(i,j)not in u:v=[(i,j)];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in v for y in A(-1,2)for x in A(-1,2))];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in v for y in A(-1,2)for x in A(-1,2))];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in v for y in A(-1,2)for x in A(-1,2))];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in v for y in A(-1,2)for x in A(-1,2))];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i+y,j+x)in v for y in A(-1,2)for x in A(-1,2))];c[i][j]=(B(v)^9)%3^3
 return[[g[y][x]or C(g[i][j]==1and all(B(g)>y+(a-i)*s>-1<x+(b-j)*s<B(g[0])and c[y+(a-i)*s][x+(b-j)*s]==s for(a,b)in u)for i in A(B(g))for j in A(B(g[0]))for s in A(1,4))for x in A(B(g[0]))]for y in A(B(g))]