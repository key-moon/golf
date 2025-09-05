def p(L,v=range):
 b=len(L)
 D=len(L[0])
 E=[[0 for _ in v(D)]for _ in v(b)]
 for r in v(b):
  for c in v(D):
   if r==0 or r==b-1 or c==0 or c==D-1:
    E[r][c]=8
   else:
    E[r][c]=0      
 return E