L=len
R=range
def p(g):
 C=max(sum(g,[]))
 for i in range(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(h):
   if g[r].count(C)>w/2:
    for c in R(w):
     if g[r][c]==0:g[r][c]=4
 for i in range(10):
  for r in R(h):
   for c in R(w):
    if g[r][c]==4:
     for y,x in [[0,1],[0,-1],[1,0],[-1,0]]:
      if 0<=r+y<h and 0<=c+x<w and g[r+y][c+x]==0:
       g[r+y][c+x]=4
 g=[[3 if c==0 else c for c in r] for r in g]
 return g