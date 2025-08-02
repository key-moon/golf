def p(val_g):
	B=val_g
	for A in B:
		C=[A for(A,B)in enumerate(A)if B]
		for(E,F)in zip(C,C[1:]):
			for D in range(E+1,F):
				if A[D]==0:A[D]=1
	return B