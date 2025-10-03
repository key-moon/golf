C=any
B=len
A=range
def p(g):
 for c in A(10):
  for d in A(10):
   u=[(i,j)for i in A(B(g))for j in A(B(g[0]))if c==g[i][j]];v=[(i,j)for i in A(B(g))for j in A(B(g[0]))if d==g[i][j]];a=[(i,j)for i in A(B(g))for j in A(B(g[0]))if c!=g[i][j]>0if C((i+k,j+l)in u for k in A(-1,2)for l in A(-1,2))];b=[(i,j)for i in A(B(g))for j in A(B(g[0]))if d!=g[i][j]>0if C((i+k,j+l)in v for k in A(-1,2)for l in A(-1,2))];b=[(i,j)for i in A(B(g))for j in A(B(g[0]))if d!=g[i][j]>0if C((i+k,j+l)in b+v for k in A(-1,2)for l in A(-1,2))];b=[(i,j)for i in A(B(g))for j in A(B(g[0]))if d!=g[i][j]>0if C((i+k,j+l)in b+v for k in A(-1,2)for l in A(-1,2))];b=[(i,j)for i in A(B(g))for j in A(B(g[0]))if d!=g[i][j]>0if C((i+k,j+l)in b+v for k in A(-1,2)for l in A(-1,2))];s=(B(b)^6)%6
   for(i,j)in u*(B(a)==1<B(u)and B(v)==B(b)):
    for k in A(s):
     for l in A(s):g[(i-a[0][0])*s+b[0][0]+k][(j-a[0][1])*s+b[0][1]+l]=d
 return g