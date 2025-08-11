def p(g):
 R=range
 h,w=len(g),len(g[0])
 r=[[g[i][j]for j in R(w)]for i in R(h)]
 for i in R(h):
  for j in R(w):
   if g[i][j]==2:
    if j+1<w and g[i][j+1]==2 and(j<1 or g[i][j-1]!=2)and(j>w-3 or g[i][j+2]!=2):
     for a in R(-1,2):
      for b in R(-1,3):
       x,y=i+a,j+b
       if 0<=x<h and 0<=y<w and r[x][y]==0:r[x][y]=3
    if i+1<h and g[i+1][j]==2 and(i<1 or g[i-1][j]!=2)and(i>h-3 or g[i+2][j]!=2):
     for a in R(-1,3):
      for b in R(-1,2):
       x,y=i+a,j+b
       if 0<=x<h and 0<=y<w and r[x][y]==0:r[x][y]=3
 return r