R=range
L=len
def p(g):
 h,w=L(g),L(g[0])
 for r in R(1,h-1):
  for c in R(1,w-1):
   M=[g[r+y][c+x]for y,x in[[0,0],[0,1],[1,0],[1,1]]]
   C=max(M)
   if sum([1 for i in M if i>0])>2:
    I=M.index(0)
    for i in R(1,10):
     if I<2:y=r-i
     else:y=r+i+1
     if I%2:x=c+i+1
     else:x=c-i
     if 0<=y<h and 0<=x<w:g[y][x]=C
 return g