def p(g):
	for(A,B)in enumerate(g):B[A]=B[~A]=0
	return g