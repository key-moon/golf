def p(A):
	G=len(A)
	for E in A:
		B=[A for(A,B)in enumerate(E)if B==1]
		for(C,D)in zip(B,B[1:]):
			for H in range(C+1,D):E[H]=8
	for F in range(len(A[0])):
		B=[B for B in range(G)if A[B][F]==1]
		for(C,D)in zip(B,B[1:]):
			for I in range(C+1,D):A[I][F]=8
	return A