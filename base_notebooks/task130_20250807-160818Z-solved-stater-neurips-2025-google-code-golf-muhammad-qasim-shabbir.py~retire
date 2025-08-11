def p(g):
 q=range
 r=[[0]*3for _ in q(3)]
 for i in q(3):
  for j in q(3):
   c={}
   for x in q(3):
    for y in q(3):
     v=g[i*3+x][j*3+y]
     c[v]=c.get(v,0)+1
   r[i][j]=max(c,key=c.get)
 return r
