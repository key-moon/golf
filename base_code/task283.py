def p(g):
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==5:
    k=0
    for di,dj in (1,0),(-1,0),(0,1),(0,-1):
     x,y=i+di,j+dj
     if x<0 or y<0 or x>=len(g) or y>=len(g[0]) or g[x][y]!=5:k+=1
    r[j]=(2,4,1)[k]
 return g