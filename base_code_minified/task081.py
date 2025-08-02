def p(A):
	D=len(A)-1
	for B in range(D):
		for C in range(D):
			if A[B][C]+A[B][C+1]+A[B+1][C]+A[B+1][C+1]==24:
				if not A[B][C]:A[B][C]=1
				elif not A[B][C+1]:A[B][C+1]=1
				elif not A[B+1][C]:A[B+1][C]=1
				else:A[B+1][C+1]=1
	return A