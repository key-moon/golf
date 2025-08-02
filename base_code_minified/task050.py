def p(A):
	for D in A:
		if(B:=[A for(A,B)in enumerate(D)if B==8])[1:]:
			for C in range(B[0]+1,B[-1]):D[C]=3
	for(E,F)in enumerate(zip(*A)):
		if(B:=[A for(A,B)in enumerate(F)if B==8])[1:]:
			for C in range(B[0]+1,B[-1]):A[C][E]=3
	return A