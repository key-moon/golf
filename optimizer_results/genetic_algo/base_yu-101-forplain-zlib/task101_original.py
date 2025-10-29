C=any
B=range
A=len
def p(g):
 u=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==1];u=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in u)];u=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in u)];c=[]
 for i in B(A(g)):
  c+=[0]*A(g[0]),
  for j in B(A(g[0])):
   if g[i][j]==2and(i,j)not in u:v=[(i,j)];v=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];v=[(i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2if C((i-y)*(i-y)+(j-x)*(j-x)<3for(y,x)in v)];c[i][j]=(A(v)^9)%3^3
 return[[g[y][x]or C(g[i][j]==1and all(y+(a-i)*s in B(A(g))and x+(b-j)*s in B(A(g[0]))and c[y+(a-i)*s][x+(b-j)*s]==s for(a,b)in u)for i in B(A(g))for j in B(A(g[0]))for s in B(1,4))for x in B(A(g[0]))]for y in B(A(g))]