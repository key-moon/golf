def p(A):
	C,I,J=len(A[0]),0,0;C,E=len(A[0]),0
	for F in A:
		for(B,D)in enumerate(F):
			if D:C=min(C,B);E=max(E,B)
	G=C+E
	for(H,F)in enumerate(A):
		for(B,D)in enumerate(F):
			if D and not A[H][G-B]:A[H][G-B]=D
	return A