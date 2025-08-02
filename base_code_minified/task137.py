def p(A):
	C=len(A);B=[]
	for(I,J)in enumerate(A):
		for(K,O)in enumerate(J):
			if O:B.append((I,K));G=O
	D=sorted({A for(A,B)in B});E=sorted({A for(B,A)in B});H=max(D[1]-D[0],D[-1]-D[-2],E[1]-E[0],E[-1]-E[-2]);R=D[0]%H;S=E[0]%H;T=range(R,C,H);U=range(S,C,H);F=[[0]*C for A in range(C)]
	for J in T:F[J]=[G]*C
	for I in range(C):
		for K in U:F[I][K]=G
	B=sorted(B)
	for((P,L),(M,Q))in zip(B,B[1:]):
		for N in range(min(P,M),max(P,M)+1):F[N][L]=G
		for N in range(min(L,Q),max(L,Q)+1):F[M][N]=G
	return F