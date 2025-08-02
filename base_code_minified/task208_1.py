def p(A):
	F,G=len(A),len(A[0]);B={}
	for D in A:
		for C in D:B[C]=B.get(C,0)+1
	E=min(B,key=B.get)
	for(H,D)in enumerate(A):
		for(I,C)in enumerate(D):
			if C==E:A[F-1-H][G-1-I]=E
	return A