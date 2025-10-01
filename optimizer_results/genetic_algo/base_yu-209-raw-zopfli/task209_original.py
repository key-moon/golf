def p(g):
 (u,l),*_,(d,r)=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==4]
 G=[g[i][l:r+1]for i in range(u,d+1)]
 for i in range(u,d+1):
  g[i][l:r+1]=[0]*(r+1-l)
 for s in range(2,6):
  for y in range(6,68):
   for x in range(-6,68):
    if all(len(g)>(i+y)//s>-1<(j+x)//s<len(g[0])and g[(i+y)//s][(j+x)//s]==G[i][j]for i in range(len(G))for j in range(len(G[0]))if G[i][j]|4!=4):
     for i in range(len(G)):
      for j in range(len(G[0])):
       if G[i][j]<1 and len(g)>(i+y)//s>-1<(j+x)//s<len(g[0]):
        G[i][j]=g[(i+y)//s][(j+x)//s]
     return G