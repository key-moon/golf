def p(A):
	for(C,D)in zip(A,A[1:]):
		for(B,E)in enumerate(C[:-1]):
			if not E|C[B+1]|D[B]|D[B+1]:C[B]=C[B+1]=D[B]=D[B+1]=2
	return A