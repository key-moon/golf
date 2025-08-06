R=range
def p(g):
 for w in R(8,16):
  x,y,h=w%4,w//4,len(g)
  if all(g[i][j]==g[i-y][j-x]for i in R(y,h)for j in R(x,10)):
   return g+[[0]*(v:=i//y*x)+g[i%y][:10-v]for i in R(h,10)]