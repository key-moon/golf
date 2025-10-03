C=min
B=len
A=range
def p(g):u=C(i for i in A(B(g))for j in A(B(g[i]))if g[i][j]==8);v=C(j for i in A(B(g))for j in A(B(g[i]))if g[i][j]==8);y=C(i for i in A(B(g))for j in A(B(g[i]))if g[i][j]%8);x=C(j for i in A(B(g))for j in A(B(g[i]))if g[i][j]%8);n=g[y][x+1:].index(0);return[[0<i<n+1>j>0and g[u-1+i][v-1+j]and((i+j==n+1or i==j)*8or g[y+(i+j>n)*n+(i>j)][x+(i+j>n)*n+(i<j)])or g[y+i][x+j]for j in A(n+2)]for i in A(n+2)]