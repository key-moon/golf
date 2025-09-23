R=range
L=len
def p(g):
 h,w,C=L(g),L(g[0]),5
 for r in R(1,h-1):
  if sum(g[r])<1:C+=1
  for c in R(1,w-1):
   if g[r][c] and g[r-1][c] and g[r+1][c] and g[r][c-1] and g[r][c+1]==4:
    g[r][c]=C
 f=sum(g,[])
 Z=sorted([[f.count(c),c] for c in set(f) if c>4])
 for r in R(h):
  for c in R(w):
   if g[r][c]==Z[0][1]:g[r][c]=1
   if g[r][c]==Z[1][1]:g[r][c]=2
 return g