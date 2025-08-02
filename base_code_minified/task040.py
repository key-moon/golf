def p(A):
	E=len(A)
	for(B,C)in enumerate(A):
		for(D,F)in enumerate(C):
			if F==3:C[D]=A[(0,-1)[B>=E-1-B]][D]
	return A