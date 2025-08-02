def p(A):
	C=next(A for(A,B)in enumerate(A[9])if B);F=A[9][C]
	for(D,G)in enumerate(A):
		for E in range(10):B=E-C;G[E]=(D<1 and B&3==1 or D==9 and B&3==3)and 5 or F*(B&1^1)
	return A