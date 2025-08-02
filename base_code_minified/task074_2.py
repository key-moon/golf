def p(A):
	E=max(map(max,A));D=len(A)
	for B in range(D):
		for C in range(D):
			if A[B][C]==E:A[B][C]=A[C][B]
	return A