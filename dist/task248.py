def p(A):
 D=len(A[0]);C=A[-1].index(1);B=1;E=[[0]*D for A in A]
 for G in E[::-1]:G[C]=1;F=C+B;(F<0 or F>=D)and(B:=-B);C+=B
 return E