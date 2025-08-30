R=range
L=len
def p(g):
 h,w=L(g),L(g[0])
 for i in R(10):
  for r in R(h):
   for c in R(w):
    if g[r][c]==0:
     g[r][c]=g[c][r]
    if g[r][c]==0:g[r][c]=g[r+1][c+1]
 return g
