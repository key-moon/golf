def p(g):
 for A in range(9):
  for B in range(9):
   if g[A][B]==5:
    for C in(-1,0,1):
     for D in(-1,0,1):
      try:g[A+C][B+D]=g[A+C][B+D]or 1
      except:pass
 return g