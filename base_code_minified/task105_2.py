def p(val_g):
	B=val_g
	for D in B:
		A=[A for(A,B)in enumerate(D)if B]
		if A:
			for C in range(A[0],A[-1]+1):D[C]or D.__setitem__(C,2)
	for C in range(len(B[0])):
		A=[A for(A,B)in enumerate(B)if B[C]]
		if A:
			for E in range(A[0],A[-1]+1):B[E][C]or B[E].__setitem__(C,2)
	return B