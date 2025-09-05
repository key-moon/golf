j=lambda A:[[A[E][W]for E in range(len(A))]for W in range(len(A[0]))]
def l(A):c=[i for i,r in enumerate(A)if any(r)];return c[0],c[-1]
def p(A):
 E,k=l(A)
 W,p=l(j(A))
 def s(c,l,J,a):A[c][l],A[J][a]=A[J][a],A[c][l]
 s(E+1,W+1,k+1,p+1)
 s(E+1,p-1,k+1,W-1)
 s(k-1,W+1,E-1,p+1)
 s(k-1,p-1,E-1,W-1)
 return A