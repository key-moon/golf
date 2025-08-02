def p(A):
	for B in A:
		C=[A for(A,B)in enumerate(B)if B]
		for(E,F)in zip(C,C[1:]):
			for D in range(E+1,F):
				if B[D]==0:B[D]=1
	return A