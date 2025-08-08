A=len
def p(g):
 n=A(g[0]);m=n-1;p=2*m;k=(m-A(g)+1)%p
 for i in range(A(g)):j=abs((i+k)%p-m);g[i]=[8]*n;g[i][j]=1
 return g