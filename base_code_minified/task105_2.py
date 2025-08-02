def p(A):
	for D in A:
		B=[A for(A,B)in enumerate(D)if B]
		if B:
			for C in range(B[0],B[-1]+1):D[C]or D.__setitem__(C,2)
	for C in range(len(A[0])):
		B=[A for(A,B)in enumerate(A)if B[C]]
		if B:
			for E in range(B[0],B[-1]+1):A[E][C]or A[E].__setitem__(C,2)
	return A