def p(g):
	for(B,C)in zip(g,g[1:]):
		for(A,D)in enumerate(B[:-1]):
			if not D|B[A+1]|C[A]|C[A+1]:B[A]=B[A+1]=C[A]=C[A+1]=2
	return g