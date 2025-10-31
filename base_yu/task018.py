# best: 275(ox jam) / others: 286(jailctf merger), 299(FuunAgent), 301(Code Golf International), 311(HIMAGINE THE FUTURE.), 322(ALE-Agent)
def p(g):
 C=max({*sum(g,[])}-{0},key=sum(g,[]).count)
 for y,x,c in [(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]==C]:
  v=[(y,x,g[y][x])]
  v=[(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]if any(2>i-y>-2<j-x<2 for i,j,c in v)]
  v=[(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]if any(2>i-y>-2<j-x<2 for i,j,c in v)]
  v=[(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]if any(2>i-y>-2<j-x<2 for i,j,c in v)]
  v=[(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]if any(2>i-y>-2<j-x<2 for i,j,c in v)]
  v=[(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]if any(2>i-y>-2<j-x<2 for i,j,c in v)]
  v=[(y,x,g[y][x])for y in range(len(g))for x in range(len(g[0]))if g[y][x]if any(2>i-y>-2<j-x<2 for i,j,c in v)]
  for d in [-1,-1,-1,1,-1,-1,-1,1]:
   for y in range(-22,22):
    for x in range(-22,22):
     if all(i+y in range(len(g)) and j+x in range(len(g[0])) and g[i+y][j+x]==c for i,j,c in v if c!=C):
      for i,j,c in v:
       g[i+y][j+x]=c
  #  g[:]=map(list,zip(*g[::d]))
   g=[[*s]for s in zip(*g[::d])]
  for i,j,c in v:
   g[i][j]=0
 return g
