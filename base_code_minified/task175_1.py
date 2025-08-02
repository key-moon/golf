def p(A):
	D,E=len(A),len(A[0])
	for B in range(D):
		for C in range(E):
			if A[B][C]==0:A[B][C]=A[B][C-1]or A[B][C+1]or A[B-1][C]or A[B+1][C]
	return A