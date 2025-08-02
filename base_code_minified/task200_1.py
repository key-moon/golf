def p(A):
	C=next(filter(None,A[-1]));D=A[-1].index(C)
	for B in range(D,10,2):
		for E in range(10):A[E][B]=C
	for(F,B)in enumerate(range(D+1,10,2)):A[(F&1)*9][B]=5
	return A