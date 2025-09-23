R=range
L=len
def p(g):
 for i in R(4):
  g=list(map(list,zip(*g[::-1])))
  h,w,I=L(g),L(g[0]),0
  for r in R(h):
   if len(set(g[r]))>2 and 8 not in g[r]:
    S=C=0
    if I>0:
     for c in R(w):
      if g[r][c]>0 and C==0 and not S:S=1;C=g[r][c]
      if g[r][c]>0 and g[r][c]!=C:S=0
      if S==1 and g[r][c]==0:g[r][c]=8
    I+=1
   elif I>0:
    for c in R(w):
     if g[r-1][c]==8:g[r-1][c]=0
    I=0
 return g