def p(A):
	F=len(A);D=0
	for(B,H)in enumerate(A):
		for(C,I)in enumerate(H):
			if I and B+C+1>D:D=B+C+1
	E=F*D;G=[[0]*E for A in range(E)]
	for B in range(E):
		J,K=divmod(B,F)
		for C in range(E):
			L,M=divmod(C,F)
			if J+L<D:G[B][C]=A[K][M]
	return G