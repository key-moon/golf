def p(j):
 A=3;c=[]
 for E in zip(*j):
  for k in E:
   if k:c+=[k];break
 c+=[0]*(A*A-len(c))
 return[c[i*A:i*A+A][::1-2*(i%2)]for i in range(A)]