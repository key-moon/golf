def p(A):
	F,G=len(A),len(A[0])
	for C in(1,2):
		D=min(A for(A,B)in enumerate(A)for D in B if D==C);E=min(B for A in A for(B,D)in enumerate(A)if D==C)
		for B in range(10):
			if D-B>=0 and E-B>=0:A[D-B][E-B]=C
			if D+1+B<F and E+1+B<G:A[D+1+B][E+1+B]=C
	return A