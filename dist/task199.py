def p(j,A=enumerate):
 for(c,C)in A(j):
  for(k,B)in A(C):
   if B and B^4:
    j[c+1][k]=B
    for l in range(c+1):j[l][k&1::2]=[4]*len(j[l][k&1::2])
    return j