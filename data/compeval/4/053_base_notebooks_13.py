def p(g,u=range):
 h,w=len(g),len(g[0])
 Q=[[0]*w for _ in u(h)]
 for i in u(h):
  for j in u(w):R,T=(i--2)%h,(j--3)%w;Q[i][j]=g[R][T]
 return Q