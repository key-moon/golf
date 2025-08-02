def p(g):
	D,E=[A for(A,B)in enumerate(zip(*g))if 2 in B];F=[A for(A,B)in enumerate(g)if B[D]==2][0];G=[A for(A,B)in enumerate(g)if B[E]==2][0]
	for(H,A)in enumerate(g):
		for(B,I)in enumerate(A):
			if I==8:
				for C in range(D+1,B):A[C]=8
				A[B]=4;J=G+H-F
				for C in range(B+1,E):g[J][C]=8
	return g