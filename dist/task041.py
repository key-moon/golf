def p(j,A=0):
 for c in j:
  for(B,k)in enumerate(c):
   if k:A=(not A)*k
   else:c[B]=A
 return j