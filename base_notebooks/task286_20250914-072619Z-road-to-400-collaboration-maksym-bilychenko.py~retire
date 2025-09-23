L=len
R=range
def p(g):
 h,w=L(g),L(g[0])
 f=sum(g,[]);C=sorted([[f.count(k),k] for k in set(f)])[:2]
 d={C[0][1]:C[1][1],C[1][1]:C[0][1]}
 for i in range(50):
  for r in R(h):
   for c in R(w):
    if g[r][c] in d:
     for y,x in [[0,1],[0,-1],[1,0],[-1,0]]:
      if 0<=r+y<h and 0<=c+x<w and g[r+y][c+x]==0:
       g[r+y][c+x]=d[g[r][c]]
 return g