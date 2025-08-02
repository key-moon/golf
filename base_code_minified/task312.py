def p(g):
	for A in g:
		for(B,C)in enumerate(A):
			if C==5:A[B]=A[0]
	return g