def p(g):
 r=[[0]*3 for _ in[0]*3];m=[(0,0),(0,2),(1,1),(2,0),(2,2)];n=len(g);k=0
 for i in range(n):
  for j in range(n):
   if g[i][j]==2:
    a,b=m[k];r[a][b]=1;k+=1;s=[(i,j)]
    while s:
     x,y=s.pop()
     if g[x][y]!=2:continue
     g[x][y]=0
     if x:s+=[(x-1,y)]
     if x+1<n:s+=[(x+1,y)]
     if y:s+=[(x,y-1)]
     if y+1<n:s+=[(x,y+1)]
 g=r
 return g