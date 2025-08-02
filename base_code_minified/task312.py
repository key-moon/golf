def p(A):
	for B in A:
		for(C,D)in enumerate(B):
			if D==5:B[C]=B[0]
	return A