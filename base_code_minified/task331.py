def p(A):
	D=len(A)
	for B in range(D):
		for C in range(D):
			if A[B][C]==1:
				if B:A[B-1][C]=2
				if C:A[B][C-1]=7
				if B+1<D:A[B+1][C]=8
				if C+1<D:A[B][C+1]=6
	return A