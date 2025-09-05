def p(g):
	for A in g:
		for B in{*A}-{0}:
			D=A.index(B);E=len(A)-A[::-1].index(B)
			for C in range(D,E):
				if~A[C]:A[C]=B
	return g