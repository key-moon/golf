B=range
A=len
def p(g):
 r,c=next((i,j)for i in B(A(g))for j in B(A(g[0]))if g[i][j]==2);g[r][c]=0
 for(C,D,v)in(-1,-1,3),(-1,1,6),(1,1,7),(1,-1,8):
  i,j=r+C,c+D
  if 0<=i<A(g)and 0<=j<A(g[0]):g[i][j]=v
 return g