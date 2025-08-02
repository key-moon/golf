def p(A):
	B,C=zip(*[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==8]);F,G=min(B),max(B);H,I=min(C),max(C)
	for D in range(F,G+1):
		for E in range(H,I+1):
			if A[D][E]^8:A[D][E]=3
	return A