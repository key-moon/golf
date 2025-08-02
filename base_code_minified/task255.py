def p(A):
	C=0;K,F=len(A),len(A[0]);G=[0]*F
	for D in range(K):
		H=[0]*F
		for B in range(F):
			if not A[D][B]:
				E=1
				if D*B:E=min(G[B],G[B-1],H[B-1])+1
				H[B]=E
				if E>C:C,I,J=E,D,B
		G=H
	for D in range(I-C+1,I+1):A[D][J-C+1:J+1]=[3]*C
	return A