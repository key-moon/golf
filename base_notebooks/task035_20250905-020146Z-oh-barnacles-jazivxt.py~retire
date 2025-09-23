L=len
R=range
P=[[0,1],[0,-1],[1,0],[-1,0]]
def p(g):
 h,w=L(g),L(g[0])
 for r in R(h):
  for c in R(w):
   if g[r][c]==8:
    for y,x in P:
     if g[r+y][c+x]==0:
      for z in R(20):
        if 0<=r+(y*z)<h and 0<=c+(x*z)<w:
         W=g[r+(y*z)][c+(x*z)]
         if W>0:g[r][c]=W
 return g