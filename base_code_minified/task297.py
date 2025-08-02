def p(g):
	A=g[0];B=len(A)
	for C in range(len(g)-2):g[C+2]=B*[A[C%B]]
	return g