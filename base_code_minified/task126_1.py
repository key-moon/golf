def p(g):
	for A in g:
		for B in range(len(A)-2):
			if A[B]and A[B]==A[B+1]==A[B+2]:g[-1][B+1]=4
	return g