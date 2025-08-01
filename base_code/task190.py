def p(g):
 a,b=next((i,j)for i in range(9)for j in range(9)
           if g[i][j]==g[i][j+1]==g[i+1][j]==g[i+1][j+1]and g[i][j])
 c=g[a][b]
 for i in range(10):
  for j in range(10):
   if g[i][j]==c and not(a<=i<=a+1and b<=j<=b+1):
    d=(i>a+1)-(i<a);e=(j>b+1)-(j<b);x,y=i+d,j+e
    while 0<=x<10and0<=y<10:
     g[x][y]=c;x+=d;y+=e
 return g
