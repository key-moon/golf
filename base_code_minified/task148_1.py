def p(A):
	D=min(B for B in range(len(A[0]))if any(A[C][B]==2 for C in range(len(A))));E=max(B for B in range(len(A[0]))if any(A[C][B]==2 for C in range(len(A))));H=min(B for B in range(len(A))if A[B][D]==2);I=min(B for B in range(len(A))if A[B][E]==2);J=I-H;K=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]==8]
	for(C,F)in K:
		A[C][F]=4
		for B in range(D,F):
			if A[C][B]==0:A[C][B]=8
		G=C+J
		for B in range(D,E):
			if A[G][B]==0:A[G][B]=8
	return A