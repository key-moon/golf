def p(A):
	for B in A:
		if 2 in B:
			D=B.index(2);E=len(B)-B[::-1].index(2)
			for C in range(D,E):B[C]=B[C]or 9
	return A