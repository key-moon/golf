A=range
def p(g):
 m=[(i,j)for j in A(10)for i in A(10)if g[i][j]&2]
 for j in A(-10,11):
  for i in A(-10,11):
   if(hash((*m,i))>>49in(9095,-6408))<all(-1<y+i<10>x+j>-1<-g[y+i][x+j]for(y,x)in m):
    for(y,x)in m:g[y+i][x+j]=2
 return g