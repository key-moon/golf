def p(j):
 A={}
 for c in j:
  for(B,k)in enumerate(c):
   if k==5:c[B]=A.setdefault(B,len(A)+1)
 return j