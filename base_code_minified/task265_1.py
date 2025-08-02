def p(A):
	for B in range(len(A)-1):
		for C in range(len(A[0])-1):
			if not A[B][C]and not A[B][C+1]and not A[B+1][C]and not A[B+1][C+1]:A[B][C]=A[B][C+1]=A[B+1][C]=A[B+1][C+1]=2
	return A