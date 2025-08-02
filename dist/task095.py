def p(A):
 for B in range(9):
  for C in range(9):
   if A[B][C]==5:
    for D in(-1,0,1):
     for E in(-1,0,1):
      try:A[B+D][C+E]=A[B+D][C+E]or 1
      except:pass
 return A