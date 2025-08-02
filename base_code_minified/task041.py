def p(g):
	for A in g:
		for B in A:
			if B:
				for C in range(A.index(B),len(A)-1-A[::-1].index(B)+1):A[C]=B
	return g