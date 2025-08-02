def p(A):
	B,C=zip(*[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==5]);D,E=min(B)+1,max(B)-1;F,G=min(C)+1,max(C)-1;H=next(A for B in A for A in B if A%5)
	for I in range(F,G+1):A[D][I]=A[E][I]=H
	for J in range(D,E+1):A[J][F]=A[J][G]=H
	return A