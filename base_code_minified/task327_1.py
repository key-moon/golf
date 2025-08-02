def p(A):
	B=len(A);E=[[0]*(B*2)for A in range(B*2)]
	for C in range(B):
		for D in range(B):
			for F in range(B*2-max(C,D)):E[C+F][D+F]=A[C][D]
	return E