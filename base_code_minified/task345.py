def p(g):
	for(B,D)in enumerate(g[-1]):
		if D==2:
			try:C=next(A for(A,C)in enumerate(g)if C[B]==5)
			except StopIteration:
				for A in g:A[B]=2
			else:
				for A in g[:C+2]:A[B+1]=2
				for A in g[C+1:]:A[B]=2
	return g