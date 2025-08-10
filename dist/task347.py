def p(j,A=range(3)):
 for c in A:
  for B in A:
   j[c][B]+=j[c][B+3]
   if j[c][B]>0:j[c][B]=6
 return[A[:3]for A in j]