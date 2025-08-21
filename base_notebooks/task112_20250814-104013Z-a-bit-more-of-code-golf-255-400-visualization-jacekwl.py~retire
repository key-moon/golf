def p(j,A=enumerate):
 c=E=0
 for k,W in A(j):
  for l,J in A(W):c+=k*(J==3);E+=l*(J==3)
 c//=2;E//=2
 for k,W in A(j):
  for l,J in A(W):
   if J==2:
    for a,C in(k,l),(c-k,l),(k,E-l),(c-k,E-l):j[a][C]=2
 return j