def p(s,F=range):
 A=len(s)
 m=len(s[0])
 N=[[0 for _ in F(m)]for _ in F(A)]
 for r in F(A):
  for c in F(m):
   if r==0 or r==A-1 or c==0 or c==m-1:
    N[r][c]=8
   else:
    N[r][c]=0      
 return N