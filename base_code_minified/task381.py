def p(g):
	for A in g:
		if 2 in A:
			C=A.index(2);D=len(A)-A[::-1].index(2)
			for B in range(C,D):A[B]=A[B]or 9
	return g