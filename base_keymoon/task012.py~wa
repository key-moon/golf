def p(g):
 a=len(g);r=[[0]*a for _ in g]
 for i in range(a-2):
  for j in range(a-2):
   t=g[i][j+1];u=g[i+1][j];v=g[i+1][j+1];w=g[i+1][j+2];x=g[i+2][j+1]
   if t==u==w==x and v and t:
    for y,(k,l) in enumerate([(0,1),(1,0),(1,1),(1,2),(2,1)]):r[i+k][j+l]=(v,[t,u,w,x][y%4])[y!=2]
 return r
