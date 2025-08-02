def p(g):
	for(A,C)in zip(g[1:],g):
		for B in range(len(A)):A[B]=A[B]or C[B]
	return g