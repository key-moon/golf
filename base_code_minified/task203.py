def p(A):
	B=len(A);E=[A[B][B]for B in range((B+1)//2)]
	for C in range(B):
		for D in range(B):A[C][D]=E[-1-min(C,D,B-1-C,B-1-D)]
	return A