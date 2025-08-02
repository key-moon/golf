def p(g):
	for(C,A)in zip(g,g[1:]):
		for(B,D)in enumerate(A):
			if not D and C[B]:A[B]=4
	return g