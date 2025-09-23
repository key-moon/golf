L=len
R=range
P=[[0,1],[0,-1],[1,0],[-1,0]]
def p(g):
 h,w=L(g),L(g[0])
 f=sum(g,[]);C=sorted([[f.count(k),k]for k in set(f)])
 for r in R(h):
  for c in R(w):
   if g[r][c]==C[1][1]:
    for y,x in P:
     if 0<=r+y<h and 0<=c+x<w and g[r+y][c+x]==C[2][1]:
      for z in R(20):
        if 0<=r+(y*z)<h and 0<=c+(x*z)<w:
         W=g[r+(y*z)][c+(x*z)]
         if W==C[0][1]:g[r][c]=0
 for i in range(4):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(h):
   if g[r].count(0)>0:
    X=0
    for c in R(w):
     if g[r][c]==C[0][1]and g[r].count(0)>0 and g[r].index(0)>c:X=1
     if X:
      if g[r][c]==C[2][1]:g[r][c]=C[0][1]
      elif g[r][c]==0:X=0
 g=[[C[1][1]if c==0 else c for c in r]for r in g]
 return g