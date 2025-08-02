def p(A):
	for B in A:
		for(D,C)in enumerate(B):
			if C:
				for E in range(D+1,len(B)):B[E]=C+(5-C)*(E-D&1)
	return A