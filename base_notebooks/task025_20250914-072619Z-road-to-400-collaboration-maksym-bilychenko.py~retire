L=len
R=range
def p(g):
 D=[0]
 for i in range(8):
  g=list(map(list,zip(*g[::-1])))
  h,w=L(g),L(g[0])
  for r in R(h):
   if len(set(g[r]))<2 and g[r][0]>0:
    C=g[r][0];D+=[C]
    for y in R(0,r-1):
     P=0
     for c in R(w):
      if g[y][c]==C:g[y][c]=0;P-=1;g[r+P][c]=C
    for y in R(r+1,h):
     P=0
     for c in R(w):
      if g[y][c]==C:g[y][c]=0;P+=1;g[r+P][c]=C
 g=[[c if c in D else 0 for c in r] for r in g]
 return g