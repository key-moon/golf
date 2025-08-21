def p(g,R=range,L=len):
 X=[r[:]for r in g]
 n,m=L(g),L(g[0])
 C=g[0][2]
 for i in R(n):
  for j in R(m):
    if g[i][j]==C:
     X[i][j]=C
     g[i][j]=0
    else:X[i][j]=0
 Z=[r[:]for r in g]
 for c in R(n):
  P=[(i,j)for i in R(n)for j in R(m)if g[i][j]==c]
  for i in R(len(P)):
   for j in R(i+1,len(P)):
    u,J=P[i]
    N,p=P[j]
    if u==N:
     for x in R(min(J,p),max(J,p)+1):Z[u][x]=c
    elif J==p:
     for y in R(min(u,N),max(u,N)+1):Z[y][J]=c
 for i in R(n):
  for j in R(m):
   if X[i][j]>0:Z[i][j]=C
 return Z