def p(val_g):
	D=val_g;A=len(D);E=[[0]*(A*2)for B in range(A*2)]
	for B in range(A):
		for C in range(A):
			for F in range(A*2-max(B,C)):E[B+F][C+F]=D[B][C]
	return E