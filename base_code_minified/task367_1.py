def p(A):
	for(D,B)in zip(A,A[1:]):
		for(C,E)in enumerate(B):
			if not E and D[C]:B[C]=4
	return A