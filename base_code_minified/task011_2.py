def p(A):
	D=len(A)
	for B in range(D):
		for C in range(D):
			if A[B][C]!=5:A[B][C]=A[B//4*4][C//4*4]
	return A