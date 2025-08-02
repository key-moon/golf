def p(g):
	for A in g:
		for B in range(len(A)-2):
			if A[B]==A[B+2]==1 and not A[B+1]:A[B+1]=2
	return g