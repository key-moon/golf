def p(g,k=range):
 X=[r[:]for r in g]
 for c in k(1,10):
  v=[(i,j)for i in k(len(g))for j in k(len(g[0]))if g[i][j]==c]
  for i in k(len(v)):
   for j in k(i+1,len(v)):
    K,D=v[i]
    n,B=v[j]
    if K==n:
     for x in k(min(D,B),max(D,B)+1):X[K][x]=c
    elif D==B:
     for y in k(min(K,n),max(K,n)+1):X[y][D]=c
 return X