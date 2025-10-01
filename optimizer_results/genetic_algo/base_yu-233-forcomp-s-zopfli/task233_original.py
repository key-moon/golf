def p(g):
 u=[[*s]for s in g]
 for _ in range(80):u=[[*s]for s in zip(*u[('2, '*7in str(u[-1]))-2::-1])]
 for _ in range(8):
  for y in range(len(u)-2):
   for x in range(len(u[0])-2):
    if(u+[[1]*80]*3)[y-1][x+1]*(u+[[1]*80]*3)[y+3][x+1]:
     for i in range(len(g)-2):
      for j in range(len(g[0])-2):
       if all([2==g[i+k][j+m],2!=g[i+k][j+m]|2][u[y+k][x+m]>0]for k in range(3)for m in range(3)):
        for k in range(3):
         for m in range(3):u[y+k][x+m]=g[i+k][j+m];g[i+k][j+m]=0
  u=[[*s]for s in zip(*u[::-1])]
 return u