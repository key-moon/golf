def p(r):
 p=[u[:]for u in r];t,s=len(r),len(r[0])
 for q in range(1,t):
  for u in range(1,s-1):
   if r[q][u]==0and r[q][u-1]and r[q][u+1]and r[q][u-1]==r[q][u+1]and r[q-1][u]==r[q][u-1]:p[t-1][u]=4
 return p