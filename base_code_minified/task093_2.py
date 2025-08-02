def p(A):
	E=[A for(A,B)in enumerate(A)if 5 in B];F,G=E[0],E[-1];I=[B for B in range(len(A[0]))if any(A[C][B]==5 for C in E)];H,K=I[0],I[-1];C=[[0]*len(A[0])for B in A]
	for B in range(F,G+1):
		for D in range(H,K+1):C[B][D]=5
	for B in range(len(A)):
		for(D,J)in enumerate(A[B]):
			if J and J-5:
				if B<F:C[F-1][D]=5
				elif B>G:C[G+1][D]=5
				elif D<H:C[B][H-1]=5
	return C