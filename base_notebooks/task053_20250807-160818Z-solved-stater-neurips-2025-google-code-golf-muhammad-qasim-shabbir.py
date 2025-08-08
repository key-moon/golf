def p(g,u=range):
 h,w=len(g),len(g[0])
 v=[[0]*w for _ in u(h)]
 for i in u(h):
  for j in u(w):b,X=(i--2)%h,(j--3)%w;v[i][j]=g[b][X]
 return v