def p(A):
	for(B,D)in zip(A[1:],A):
		for C in range(len(B)):B[C]=B[C]or D[C]
	return A