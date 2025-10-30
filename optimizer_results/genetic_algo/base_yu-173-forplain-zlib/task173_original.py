B=len
A=range
def p(g):
 for i in A(B(g)-2):
  for j in A(B(g[0])-2):
   for y in A(B(g)-2):
    for x in A(B(g[0])-2):
     for k in A(9*(sum(a:=[g[i+k//3][k%3+j]for k in A(9)])>a[4]>0<(sum(g[y+k//3][k%3+x]==g[i+k//3][k%3+j]for k in A(9))>7or a[4]==g[y+1][1+x])and a==a[::-1])):g[y+k//3][k%3+x]=g[i+k//3][k%3+j]
 return g