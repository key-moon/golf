def p(g):
 for i in range(9):
  for j in range(9):
   if g[i][j]==5:
    for di in(-1,0,1):
     for dj in(-1,0,1):
      try:g[i+di][j+dj]=g[i+di][j+dj]or 1
      except:pass
 return g