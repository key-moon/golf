def p(A):
	E,F=[A for(A,B)in enumerate(zip(*A))if 2 in B];G=[A for(A,B)in enumerate(A)if B[E]==2][0];H=[A for(A,B)in enumerate(A)if B[F]==2][0]
	for(I,B)in enumerate(A):
		for(C,J)in enumerate(B):
			if J==8:
				for D in range(E+1,C):B[D]=8
				B[C]=4;K=H+I-G
				for D in range(C+1,F):A[K][D]=8
	return A