def p(A):
	E=len(A[0])&1^1
	for B in A:
		for(C,D)in enumerate(B):B[C]=D-2*(D==5 and C&1==E)
	return A