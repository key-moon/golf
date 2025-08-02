def p(A):
	for C in A:
		D=[A for(A,B)in enumerate(C)if B==2]
		if D:
			for B in range(D[0],D[-1]+1):
				if C[B]!=2:C[B]=8
	for E in range(len(A[0])):
		F=[B for B in range(len(A))if A[B][E]==2]
		if F:
			for B in range(F[0],F[-1]+1):
				if A[B][E]!=2:A[B][E]=8
	return A