def p(A):
	D,K=len(A),len(A[0]);E=[B for B in range(D)if 5 in A[B]];F=[B for B in range(K)if any(A[C][B]==5 for C in range(D))];L,M=min(E),max(E);N,O=min(F),max(F);G=[A[B][N+1:O]for B in range(L+1,M)];B=[(A,C)for(A,B)in enumerate(G)for(C,D)in enumerate(B)if D==8]
	if not B:return[[0]*3 for A in range(3)]
	P,Q=min(A for(A,B)in B),max(A for(A,B)in B);R,S=min(A for(B,A)in B),max(A for(B,A)in B);C=[A[R:S+1]for A in G[P:Q+1]];T,U=len(C),len(C[0]);H=[[0]*3 for A in range(3)]
	for I in range(3):
		for J in range(3):
			if C[int(I*T/3)][int(J*U/3)]==8:H[I][J]=8
	return H