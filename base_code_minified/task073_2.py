def p(A):
	for B in A[:-1]:
		for(C,D)in enumerate(B):
			if D==1:B[C]=0;A[-1][C]=1
	return A