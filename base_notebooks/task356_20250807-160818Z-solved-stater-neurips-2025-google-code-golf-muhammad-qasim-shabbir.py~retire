def p(g,u=range):
 X=[r[:]for r in g]
 for c in u(1,10):
  W=[(i,j)for i in u(len(g))for j in u(len(g[0]))if g[i][j]==c]
  for i in u(len(W)):
   for j in u(i+1,len(W)):
    v,b=W[i]
    G,J=W[j]
    if v==G:
     for x in u(min(b,J),max(b,J)+1):X[v][x]=c
    elif b==J:
     for y in u(min(v,G),max(v,G)+1):X[y][b]=c
 return X