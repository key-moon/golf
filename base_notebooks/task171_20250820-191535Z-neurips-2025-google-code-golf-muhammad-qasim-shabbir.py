def p(T,u=range):
 Q=len(T)
 R=len(T[0])
 s=[[0 for _ in u(R)]for _ in u(Q)]
 for r in u(Q):
  for c in u(R):
   if r==0 or r==Q-1 or c==0 or c==R-1:
    s[r][c]=8
   else:
    s[r][c]=0      
 return s