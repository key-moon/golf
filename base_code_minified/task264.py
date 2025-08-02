def p(A):
	H,I=len(A),len(A[0]);B=[(B,C,D)for B in range(H-2)for C in range(I-2)for D in[tuple(A[B+D][C+E]for D in range(3)for E in range(3))]if any(D)];D={}
	for(L,C)in B:D[C]=D.get(C,0)+1
	B=[(B,C,A)for(B,C,A)in B if D[A]==1];B.sort(key=lambda L:(-L[0],-L[1]));F=[[0]*9 for A in range(9)]
	for(G,(M,N,C))in enumerate(B):
		J=G//3*3;K=G%3*3
		for E in range(9):F[J+E//3][K+E%3]=C[E]
	return F