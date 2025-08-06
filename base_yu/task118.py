def p(g):
 h,w=len(g),len(g[0])
 for i in range(3,h-3):
  for j in range(3,w-3):
   if all(any(g[i+(abs(k-1)-1)*l][j+(abs(k-2)-1)*l]&2 for l in range(1,4)) for k in range(4)):
    g[i][j] = 8
 return g