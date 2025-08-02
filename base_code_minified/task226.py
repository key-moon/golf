def p(A):
	F=len(A);D=len(A[0]);K=[A for(A,B)in enumerate(A)if B.count(5)==D];L=[B for B in range(D)if all(A[C][B]==5 for C in range(F))];B=[-1]+K+[F];C=[-1]+L+[D];G=[(B[A]+1,B[A+1]-1)for A in range(len(B)-1)if B[A]+1<B[A+1]];H=[(C[A]+1,C[A+1]-1)for A in range(len(C)-1)if C[A]+1<C[A+1]];I=len(G);J=len(H)
	for E in range(3):
		M=E+1;N=(0,(I-1)//2,I-1)[E];O=(0,(J-1)//2,J-1)[E];P,Q=G[N];R,S=H[O]
		for T in range(P,Q+1):
			for U in range(R,S+1):A[T][U]=M
	return A