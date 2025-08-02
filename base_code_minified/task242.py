def p(g):
	for(C,A)in enumerate(g):
		for(B,D)in enumerate(A):
			if D==0:A[B]=g[~C][~B]
	return g