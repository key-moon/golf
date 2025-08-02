def p(A):
	for(B,C)in enumerate(zip(*A[:-1])):
		if len(A)-1-C.count(0)&1:A[-1][B]=4
	return A