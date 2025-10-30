C=any
B=len
A=range
def p(g):
 D=max({*sum(g,[])}-{0},key=sum(g,[]).count)
 for(y,x,c)in[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]==D]:
  v=[(y,x,g[y][x])];v=[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]if C(2>i-y>-2<j-x<2for(i,j,c)in v)];v=[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]if C(2>i-y>-2<j-x<2for(i,j,c)in v)];v=[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]if C(2>i-y>-2<j-x<2for(i,j,c)in v)];v=[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]if C(2>i-y>-2<j-x<2for(i,j,c)in v)];v=[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]if C(2>i-y>-2<j-x<2for(i,j,c)in v)];v=[(y,x,g[y][x])for y in A(B(g))for x in A(B(g[0]))if g[y][x]if C(2>i-y>-2<j-x<2for(i,j,c)in v)]
  for d in[-1,-1,-1,1,-1,-1,-1,1]:
   for y in A(-22,22):
    for x in A(-22,22):
     if all(i+y in A(B(g))and j+x in A(B(g[0]))and g[i+y][j+x]==c for(i,j,c)in v if c!=D):
      for(i,j,c)in v:g[i+y][j+x]=c
   g=[[*s]for s in zip(*g[::d])]
  for(i,j,c)in v:g[i][j]=0
 return g