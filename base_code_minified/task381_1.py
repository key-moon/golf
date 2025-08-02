def p(g):
	for A in g:
		if 2 in A:
			C=A.index(2);D=len(A)-1-A[::-1].index(2)
			for B in range(C+1,D):
				if not A[B]:A[B]=9
	return g