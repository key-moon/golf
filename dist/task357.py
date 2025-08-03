def p(A):
 D=len(A[0]);B=D-1;E=2*B;F=(B-len(A)+1)%E
 for C in range(len(A)):G=abs((C+F)%E-B);A[C]=[8]*D;A[C][G]=1
 return A