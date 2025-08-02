def p(A):
	E,I=len(A),len(A[0])
	for F in range(E):
		G=[B for B in range(I)if A[F][B]==2]
		if G[1:]:
			C,D=G[0],G[-1]
			for B in range(C+1,D):
				if A[F][B]!=2:A[F][B]=8
	for B in range(I):
		H=[C for C in range(E)if A[C][B]==2]
		if H[1:]:
			C,D=H[0],H[-1]
			if C>0:A[C-1][B]=8
			if D<E-1:A[D+1][B]=8
	return A