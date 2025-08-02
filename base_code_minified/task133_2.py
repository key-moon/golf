def p(A):
	I=[A[:]for A in A];B={}
	for(F,S)in enumerate(A):
		for(G,J)in enumerate(S):B[J]=B.get(J,[])+[(F,G)]
	T,U,H=[A for A in B if len(B[A])in(1,4)][0],[A for A in B if len(B[A])==4 and A!=[A for A in B if len(B)==1][0]][0],[A for A in B if len(B[A])>4][0];V,K=B[T][0];D=next((0,A-K)for(B,A)in B[U]if B==V and A!=K);D=0,D;L=-D[1],D[0];M=[A for(A,B)in B[H]];N=[A for(B,A)in B[H]];O,P=min(M),max(M);Q,R=min(N),max(N);E=P-O+1;W=R-Q+1
	for C in list(range(W))+[-E,E]:
		if C and abs(C)!=E:continue
		X,Y=D[0]*C+L[0]*(C//abs(C)if abs(C)==E else 0),D[1]*C+L[1]*(C//abs(C)if abs(C)==E else 0)
		for F in range(O,P+1):
			for G in range(Q,R+1):
				if A[F][G]==H:I[F+X][G+Y]=H
	return I