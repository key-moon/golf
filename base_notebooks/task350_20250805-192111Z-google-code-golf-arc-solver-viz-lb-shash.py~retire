def p(g,h=range):
 G=[r[:]for r in g]
 for c in h(1,10):
  V=[(i,j)for i in h(len(g))for j in h(len(g[0]))if g[i][j]==c]
  for i in h(len(V)):
   for j in h(i+1,len(V)):
    s,b=V[i]
    F,K=V[j]
    if s==F:
     for x in h(min(b,K),max(b,K)+1):G[s][x]=8
    elif b==K:
     for y in h(min(s,F),max(s,F)+1):G[y][b]=8
  for s,F in V:G[s][F]=1
 return G