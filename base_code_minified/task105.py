def p(g):
	for B in g:
		A=[A for(A,B)in enumerate(B)if B]
		for(C,D)in zip(A,A[1:]):
			for E in range(C+1,D):B[E]=2
	for(F,B)in enumerate(zip(*g)):
		A=[A for(A,B)in enumerate(B)if B]
		for(C,D)in zip(A,A[1:]):
			for E in range(C+1,D):g[E][F]=2
	return g