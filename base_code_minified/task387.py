def p(A):
	F=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]];B,C=min(F);D,E=max(F);G=A[B][C];H=[A[B][C]for(B,C)in F if A[B][C]!=G][0]
	for(K,L,M)in((B,C,H),(B,E,G),(D,C,G),(D,E,H)):
		for N in(-1,0,1):
			for O in(-1,0,1):A[K+N][L+O]=M
	for I in range(C+2,E-1,2):A[B][I]=A[D][I]=5
	for J in range(B+2,D-1,2):A[J][C]=A[J][E]=5
	return A