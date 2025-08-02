def p(A):
	for(D,B)in enumerate(A):
		for(C,E)in enumerate(B):
			if E==0:B[C]=A[~D][~C]
	return A