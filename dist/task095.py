A=range
def p(g):
 for i in A(9):
  for j in A(9):
   if g[i][j]==5:
    for B in-1,0,1:
     for C in-1,0,1:
      try:g[i+B][j+C]=g[i+B][j+C]or 1
      except:pass
 return g