C=any
B=len
A=range
def p(g):
 u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==1];u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in u)];u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in u)];c=[[],[],[],[]]
 for i in A(B(g)):
  for j in A(B(g[0])):
   if g[i][j]==2and(i,j)not in u:v=[(i,j)];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];c[(B(v)^9)%3^3]+=(i,j),
 return[[g[y][x]or C(g[i][j]==1==all((y+(a-i)*s,x+(b-j)*s)in c[s]for(a,b)in u)for i in A(B(g))for j in A(B(g[0]))for s in A(1,4))for x in A(B(g[0]))]for y in A(B(g))]