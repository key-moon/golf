def p(O,s=range):
 z=len(O)
 y=len(O[0])
 h=[[0 for _ in s(y)]for _ in s(z)]
 for r in s(z):
  for c in s(y):
   if r==0 or r==z-1 or c==0 or c==y-1:
    h[r][c]=8
   else:
    h[r][c]=0
 return h