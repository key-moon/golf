R=range
L=len
def p(g,S=1):
 for i in R(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  if S:
   for r in R(h):
    if g[r][0]==8 and g[0].count(2)+g[-1].count(2)>0:
     y=0
     for c in R(w):
      if g[0][c]==2:y+=1
      if g[-1][c]==2:y-=1
      if 0<=r+y<h:g[r+y][c]=8
     S=0
 return g