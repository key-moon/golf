def p(t,g=len,o=range):
 a,i=len(t),len(t[0])
 for p in o(a):
  g=0
  for n in o(i):
   if t[-(p+1)][n]>0:g=t[-(p+1)][n]
   t[-(p+1)][n]=g
  g=0
  for p in o(a):
   if t[p][-1]>0:g=t[p][-1]
   t[p][-1]=g
 return t