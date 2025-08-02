def p(val_g):
	A=val_g
	for B in range(3):
		for(C,D)in enumerate(A[B]):
			if D==8:A[B][8-C]=8
	return A