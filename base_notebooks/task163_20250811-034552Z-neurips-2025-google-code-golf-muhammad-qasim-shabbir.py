def p(j):
 A=range
 for c in A(3):
  for E in A(3):
   k=[[j[4*c+W][4*E+l]for l in A(3)]for W in A(3)]
   for W in A(3):
    for l in A(3):
     if k[W][l]==4:
      J=[[0]*11for _ in A(11)]
      for a in A(3):
       for C in A(3):J[4*W+a][4*l+C]=k[a][C]
      for e in A(11):J[e][3]=J[e][7]=J[3][e]=J[7][e]=5
      return J