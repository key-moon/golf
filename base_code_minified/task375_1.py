def p(A):
	for(B,C)in enumerate(A):C[B]=C[~B]=0
	return A