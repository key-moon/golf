def p(A):
	B=next(B for(B,C)in enumerate(A)if C[0]!=A[0][0]);C=next(B for(B,C)in enumerate(A[0])if C!=A[0][0]);E=[A[0][0],A[0][C],A[B][0],A[B][C]];D=[0,0,0,0]
	for(G,H)in enumerate(A):
		for(I,J)in enumerate(H):F=(G>=B)<<1|(I>=C);D[F]+=J!=E[F]
	return[[E[D.index(max(D))]]]